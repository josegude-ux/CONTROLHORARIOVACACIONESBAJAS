"""Pruebas de seguridad de la plantilla demo ficticia, sin datos reales."""
import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "verificar_demo_publica.py"
ZERO_FIELDS = (
    "pending2026", "planned2026", "used2026", "carry2026",
    "entitlement2027", "used2027", "planned2027", "remaining2027",
)


def demo():
    return {
        "version": 1,
        "importedFrom": "Datos de demostracion ficticios",
        "employees": [
            {"id": str(i), "name": f"Empleado de prueba {i:02d}", "status": "ACTIVO",
             "start": None, "end": None, **{field: 0 for field in ZERO_FIELDS}}
            for i in range(1, 13)
        ],
        "marks": {}, "records": [], "holidays": [], "audit": [],
        "settings": {"maxAbsences": 3, "overtimeFactor": 1.5, "workdayHours": 8},
    }


class TestPublicDemoGuard(unittest.TestCase):
    def run_guard(self, payload, expected):
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "data.js"
            target.write_text(payload, encoding="utf-8")
            result = subprocess.run([sys.executable, str(SCRIPT), str(target)],
                                    capture_output=True, text=True, timeout=6, check=False)
            self.assertEqual(result.returncode, expected, result.stdout + result.stderr)
            return result

    def js(self, data):
        return "window.INITIAL_DATA = " + json.dumps(data, ensure_ascii=False) + ";\n"

    def test_accepts_only_expected_synthetic_demo(self):
        self.assertIn("OK:", self.run_guard(self.js(demo()), 0).stdout)

    def test_rejects_changed_employee_name(self):
        d = demo(); d["employees"][0]["name"] = "Nombre personal real"
        self.run_guard(self.js(d), 1)

    def test_rejects_employee_id_change(self):
        d = demo(); d["employees"][0]["id"] = "999"
        self.run_guard(self.js(d), 1)

    def test_rejects_nonzero_vacation_amount(self):
        d = demo(); d["employees"][0]["used2026"] = 12
        self.run_guard(self.js(d), 1)

    def test_rejects_employee_work_dates(self):
        d = demo(); d["employees"][0]["start"] = "2026-01-01"
        self.run_guard(self.js(d), 1)

    def test_rejects_employee_extra_field(self):
        d = demo(); d["employees"][0]["email"] = "example@example.com"
        self.run_guard(self.js(d), 1)

    def test_rejects_fichajes(self):
        d = demo(); d["records"].append({"hour": "08:00"})
        self.run_guard(self.js(d), 1)

    def test_rejects_calendar_marks(self):
        d = demo(); d["marks"]["2026-10-26"] = "V"
        self.run_guard(self.js(d), 1)

    def test_rejects_added_top_level_field(self):
        d = demo(); d["private_notes"] = "not for public"
        self.run_guard(self.js(d), 1)

    def test_rejects_wrong_demo_source(self):
        d = demo(); d["importedFrom"] = "Excel original"
        self.run_guard(self.js(d), 1)

    def test_rejects_wrong_employee_count(self):
        d = demo(); d["employees"].pop()
        self.run_guard(self.js(d), 1)

    def test_rejects_boolean_as_numeric_value(self):
        d = demo(); d["employees"][0]["used2026"] = False
        self.run_guard(self.js(d), 1)

    def test_rejects_duplicate_json_keys(self):
        source = self.js(demo()).replace('"version": 1,', '"version": 1, "version": 1,', 1)
        self.assertIn("duplicada", self.run_guard(source, 1).stderr)

    def test_rejects_appended_javascript(self):
        self.run_guard(self.js(demo()) + "alert('injected');", 1)

    def test_rejects_oversized_data(self):
        self.run_guard(self.js(demo()) + (" " * 100001), 1)

    def test_rejects_invalid_status(self):
        d = demo(); d["employees"][0]["status"] = "ADMINISTRADOR"
        self.run_guard(self.js(d), 1)


if __name__ == "__main__":
    unittest.main()
