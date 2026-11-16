# Control Horario Vacaciones Bajas — Control Jornada Empresa

Aplicación web/PWA empresarial **en modo presentación**, versión declarada **0.9.0**. Consulta de jornada, calendario, vacaciones, bajas y revisión experimental de fichajes PDF. Los cálculos oficiales de horas y vacaciones proceden del **Excel de origen**; la demo no debe reemplazarlos.

## Seguridad antes de publicar

**Este repositorio es público y su `data.js` actual contiene solamente 12 empleados ficticios y ningún fichaje.** La comprobación se refiere a la revisión auditada; no acredita que una carpeta privada, versiones antiguas, el historial o un alojamiento tengan la misma seguridad. No sustituir `data.js` por información real del personal ni subir Excel, PDFs o copias privadas al repositorio.

Desde la raíz, antes de publicar una demo:

```sh
python scripts/verificar_demo_publica.py
```

Este control limitado bloquea los cambios inesperados de la plantilla ficticia. **No revisa el repositorio completo, el historial ni el servidor.** Consultar [seguridad y alcance de la auditoría](docs/SEGURIDAD_DEMO_PUBLICA.md).

## Documentación

- `LEEME_GITHUB.txt`: instrucciones para la demo pública **ficticia**.
- `LEEME_MOVIL.txt`: instalación PWA y requisitos para una futura instalación empresarial privada.
- `LEEME.txt`: guía **histórica** del paquete local de importación PDF v0.8; no utilizar como instrucciones de publicación.
- `docs/CONTINUIDAD.md`: continuidad y decisiones de desarrollo (en su rama documental hasta integración autorizada).
- `docs/SEGURIDAD_DEMO_PUBLICA.md`: alcance real de esta revisión y pendientes.

**No existe confirmación de un hosting privado operativo**. La demo pública no ofrece autenticación laboral. No publicar ni desplegar datos reales sin aprobación y comprobaciones de seguridad. El importador PDF es experimental y requiere revisión humana.
