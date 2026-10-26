#!/usr/bin/env python3
"""Comprueba solo la plantilla ficticia data.js antes de publicar una demo.

No sustituye una auditoría de datos personales del historial ni del hosting.
No lee PDF, Excel ni escribe ficheros.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

EXPECTED_TOP = {"version", "importedFrom", "employees", "marks", "records", "holidays", "audit", "settings"}
EXPECTED_EMPLOYEE = {
    "id", "name", "status", "pending2026", "planned2026", "used2026",
    "carry2026", "entitlement2027", "used2027", "planned2027",
    "remaining2027", "start", "end",
}
ZERO_FIELDS = EXPECTED_EMPLOYEE - {"id", "name", "status", "start", "end"}
DEMO_SOURCE = "Datos de demostracion ficticios"


def fail(message: str) -> None:
    raise ValueError(message)


def reject_duplicate_keys(pairs: list[tuple[str, object]]) -> dict:
    result = {}
    for key, value in pairs:
        if key in result:
            fail("clave JSON duplicada: " + key)
        result[key] = value
    return result


def validate(path: Path) -> None:
    raw = path.read_bytes()
    if len(raw) > 100_000:
        fail("data.js demasiado grande para una demo controlada")
    source = raw.decode("utf-8")
    match = re.fullmatch(r"\s*window\.INITIAL_DATA\s*=\s*(\{.*\})\s*;\s*", source, re.S)
    if not match:
        fail("data.js no tiene un único objeto JSON asignado a window.INITIAL_DATA")
    data = json.loads(match.group(1), object_pairs_hook=reject_duplicate_keys,
                      parse_constant=lambda value: fail("valor numérico no JSON: " + value))
    if not isinstance(data, dict) or set(data) != EXPECTED_TOP:
        fail("campos principales imprevistos o ausentes")
    if type(data["version"]) is not int or data["version"] != 1:
        fail("versión de esquema inesperada")
    if data["importedFrom"] != DEMO_SOURCE:
        fail("el origen no declara datos ficticios")

    employees = data["employees"]
    if not isinstance(employees, list) or len(employees) != 12:
        fail("la demo debe contener exactamente 12 fichas ficticias")
    for i, employee in enumerate(employees, start=1):
        if not isinstance(employee, dict) or set(employee) != EXPECTED_EMPLOYEE:
            fail(f"empleado {i}: campos imprevistos o ausentes")
        if employee["id"] != str(i) or employee["name"] != f"Empleado de prueba {i:02d}":
            fail(f"empleado {i}: identificador o nombre no ficticio")
        expected_status = "BAJA" if i == 10 else "ACTIVO"
        if employee["status"] != expected_status:
            fail(f"empleado {i}: estado diferente de la plantilla ficticia")
        if employee["start"] is not None or employee["end"] is not None:
            fail(f"empleado {i}: fechas de relación laboral presentes")
        if any(type(employee[field]) is not int or employee[field] != 0 for field in ZERO_FIELDS):
            fail(f"empleado {i}: valores laborales distintos de cero")

    for field in ("records", "holidays", "audit"):
        if data[field] != []:
            fail(f"{field}: existen registros no ficticios o añadidos")
    if data["marks"] != {}:
        fail("marks: existen marcas de calendario")
    settings = data["settings"]
    if not isinstance(settings, dict) or set(settings) != {"maxAbsences", "overtimeFactor", "workdayHours"}:
        fail("configuración inesperada")
    if settings != {"maxAbsences": 3, "overtimeFactor": 1.5, "workdayHours": 8}:
        fail("configuración no coincide con la demo ficticia")


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) == 2 else Path(__file__).resolve().parents[1] / "data.js"
    if len(sys.argv) > 2:
        print("Uso: python scripts/verificar_demo_publica.py [ruta/data.js]", file=sys.stderr)
        return 2
    try:
        validate(path)
    except (ValueError, UnicodeError, OSError, json.JSONDecodeError) as exc:
        print(f"BLOQUEADO: {exc}", file=sys.stderr)
        return 1
    print("OK: data.js contiene solo la plantilla ficticia estrictamente esperada.")
    print("Advertencia: no se han comprobado otros archivos, el historial de Git ni el hosting.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
