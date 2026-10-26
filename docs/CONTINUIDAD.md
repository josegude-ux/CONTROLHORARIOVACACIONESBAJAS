# CONTROL HORARIO VACACIONES BAJAS — Continuidad de desarrollo

**Fecha:** 2026-10-26  
**Aplicación:** control empresarial de jornada, vacaciones y bajas.  
**Proyecto de organización:** EXCELL  
**Repositorio comprobado:** https://github.com/josegude-ux/CONTROLHORARIOVACACIONESBAJAS  
**Rama operativa comprobada:** `main` — commit `7e119417cd8db948d9a8ce239691612de68de042`  
**Versión declarada en `version.json` y `app.js`:** `0.9.0` (2026-10-22).  
**Estado de este archivo:** propuesta documental aislada en `docs/jornada-empresa-continuidad-20261026`. No implica fusionar ni desplegar.

## 1. Identidad de la conversación

- Chat de desarrollo anterior identificado en el historial: **CONTROL HORARIO VACACIONES BAJAS** (trabajo del 22/10/2026).
- Nombre recomendado para el sucesor, si el anterior está agotado o se dedica únicamente a consulta: **JORNADA · EMPRESA · DEV 01**.
- El nombre de chat es orientativo: no se ha renombrado, movido ni archivado ninguna conversación de ChatGPT desde GitHub.
- **NO mezclar** con la aplicación personal **Mi Jornada** del repositorio independiente `josegude-ux/mi-jornada`.
- **NO mezclar** con el libro de **Control Horario Excel** ni sus flujos de importación/revisión anteriores: la aplicación puede consultar resultados de ese libro, pero no reemplazarlo ni recalcular sus datos.
- Mantener prioridad general de EXCELL para **VISURA AUTO-DEV**; esta línea empresarial continúa con cambios aislados y sin solapar sus ramas.

## 2. Auditoría de solo lectura de GitHub (26/10/2026)

- Repositorio accesible y público. Rama encontrada: `main`. No se encontraron PR existentes.
- Último commit observado: `7e119417cd8db948d9a8ce239691612de68de042` — "Add files via upload".
- No existe `docs/CONTINUIDAD.md` en `main` antes de este trabajo.
- Archivos principales: `index.html`, `app.js`, `styles.css`, `data.js`, `manifest.webmanifest`, `sw.js`, `version.json`.
- `data.js` contiene **12 empleados ficticios**, sin fichajes de empresa ni calendario laboral real; no equivale a integrar el Excel real.
- `app.js` declara `CJ_VERSION='0.9.0'`. La página carga `manifest.webmanifest`, y `sw.js` usa caché `control-jornada-mobile-v0.9.0`.
- `app.js` ofrece consulta de calendario, empleado, resumen, fichajes, vacaciones, cobertura, ajustes e importación/revisión experimental de PDF.
- Actualizador móvil y alojamiento privado descritos en documentos, pero **no se ha verificado instalación real en iPhone, HTTPS privado ni actualización funcional desde un despliegue**.
- Los datos reales de trabajadores **NO deben subirse al repositorio público ni servirse desde GitHub Pages público**.

## 3. Decisiones anteriores a conservar

1. La aplicación empresarial es una **PWA de consulta**, no una segunda fuente oficial de cálculos de horas, saldos y vacaciones.
2. Los cálculos oficiales proceden del **Excel de origen**. La app puede mostrarlos, pero no inventarlos ni recalcularlos.
3. La revisión de PDFs de fichajes es **experimental y manual**: extracción básica, sin OCR y sin validar para cualquier diseño de PDF; revisar cada fila contra el documento original.
4. Mantener la demo **sin datos personales reales** en GitHub. Para uso real hace falta un canal autorizado y privado o importación local que no publique los datos.
5. Proteger las aplicaciones existentes: no reutilizar indebidamente el repositorio `mi-jornada`, no alterar el Excel original ni cambiar recursos de otro proyecto.
6. Sin publicar, fusionar, cambiar datos reales ni contratar servicios de pago sin autorización expresa.

## 4. Hallazgos que no deben pasar por funciones terminadas

- `manifest.json` conserva el nombre y la descripción **Mi Bowling · Analítica**; es material heredado. `index.html` enlaza el manifiesto correcto `manifest.webmanifest`. Investigar y corregir el manifiesto legado en una rama de revisión, sin alterar la app publicada.
- `LEEME.txt` contiene advertencias sobre un ZIP con información laboral original, mientras `LEEME_GITHUB.txt` describe una demo pública con 12 empleados ficticios. Distinguir claramente el paquete privado anterior de la demo actual para evitar publicar datos por error.
- El código de importación PDF es una ayuda de revisión, no una integración automática ni una garantía de lectura fiable.
- No se han validado en este control las pruebas automáticas, seguridad de hosting, presencia de usuarios reales ni comportamiento físico en dispositivos.
- La evidencia de GitHub no demuestra el contenido total ni la ubicación de todos los chats dentro de ChatGPT.

## 5. Plan de continuación segura

**Hito 1 — completado:** recuperar el repositorio real, rama, último commit y versión; distinguir los tres productos relacionados y dejar la continuidad en una rama documental aislada.

**Hito 2 — siguiente tarea técnica independiente:** inspección y corrección mínima de metadatos PWA legados (`manifest.json` y coherencia con `manifest.webmanifest`), con comprobaciones automáticas del JSON y de referencias desde `index.html`. Debe hacerse en rama propia, sin cambiar los datos ni desplegar.

**Hito 3:** verificar de forma reproducible que el paquete de demostración no contiene nombres ni registros reales, y documentar qué archivos son aptos para alojamiento público. Si aparecen indicios de datos reales, detener la publicación, no exponer el contenido y solicitar instrucciones para sanitizar.

**Hito 4:** revisar limitaciones del importador PDF con ejemplos sintéticos representativos y reglas de revisión humana; no suponer compatibilidad con documentos empresariales reales.

**Hito 5:** validar en entorno privado autorizado las actualizaciones PWA y el flujo de iPhone antes de anunciar instalación empresarial.

## 6. Política de cambios

Antes de comenzar cada tarea: comprobar HEAD remoto, ramas, PR, diferencias, archivos de continuidad y cambios paralelos. Mantener un solo escritor por rama o fichero. Para cada hito registrar SHA y pruebas realmente ejecutadas; no deducir éxito del despliegue a partir de tests. No realizar `merge`, `push --force`, borrados, despliegues ni cambios de datos reales sin autorización.

**Al reanudar desde otro chat:** «Continuamos CONTROL HORARIO VACACIONES BAJAS, repo `josegude-ux/CONTROLHORARIOVACACIONESBAJAS`. Leer `docs/CONTINUIDAD.md` en la rama documental más reciente, contrastar el HEAD con `main` y verificar datos demostrativos antes de programar. No confundir con `mi-jornada` ni con el libro Control Horario Excel. Mantener la prioridad general de VISURA AUTO-DEV y trabajar sin solapamientos».

## 7. Hito posterior de corrección aislada (2026-10-26)

Se corrigió la identidad heredada del **`manifest.json` legado** en la rama independiente `fix/jornada-empresa-manifest-20261026`, commit `fc5d22714be771b375d40ee9944ba038b904e979`. La identidad pasa de `Mi Bowling · Analítica` a `Control Jornada Empresa`. Se mantuvieron los iconos existentes y se igualaron nombre, inicio, ámbito, visualización y colores con el manifiesto `manifest.webmanifest` realmente enlazado por `index.html`.

**Verificaciones realizadas:** JSON válido; coincidencia de campos comunes con `manifest.webmanifest`; `index.html` sigue apuntando al manifiesto operativo; commit de corrección afecta exclusivamente a `manifest.json`; `main` conserva intacto su SHA anterior. **Sin merge, despliegue, actualización en iPhone ni cambio de versión.**

La tarea siguiente pasa a ser **revisar los paquetes de demo y documentación de privacidad, comprobar que ninguna vía de publicación expone datos laborales reales y validar posteriormente el flujo de actualización en entorno de prueba**. Antes de integrar, volver a inspeccionar HEAD y si aparecieron cambios ajenos.

## 8. Auditoría preventiva de demo pública (2026-10-26)

**PR en borrador, sin fusionar:** https://github.com/josegude-ux/CONTROLHORARIOVACACIONESBAJAS/pull/1

- Rama: `audit/jornada-demo-privacidad-20261026`, HEAD remoto `f8aa65c78e4a26e1913277fe65bc8d7ee04a3018` al comprobar.
- Destino `main`; estado: **abierta, borrador, no fusionada**.
- Archivos afectados, verificados en PR: `README.md`, `LEEME.txt`, `LEEME_GITHUB.txt`, `LEEME_MOVIL.txt`, `docs/SEGURIDAD_DEMO_PUBLICA.md`, `scripts/verificar_demo_publica.py`.
- `data.js` de `main` analizado: 12 empleados ficticios con identificador/nombre secuencial; cero fichajes, calendario, festivos o auditoría. La revisión de archivos de texto en la raíz no encontró patrones comunes de tokens/claves ni identificadores nacionales. **No prueba que no haya datos personales en archivos no revisados, commits históricos, otros artefactos o hosting.**
- Validador: Python 3, solo lee `data.js`, comprueba el JSON y restringe estrictamente la plantilla ficticia. Probado con `py_compile` y seis fixtures sintéticos (uno aceptado, cinco rechazados). Reglas contrastadas estructuralmente con `data.js` del repo. El programa Python NO se ha ejecutado dentro de CI ni en un checkout remoto completo.
- CI: consulta de estados heredados del commit `f8aa65c...` devolvió **cero estados**; no interpretar la ausencia como éxito.
- No se han modificado `app.js`, `data.js`, `sw.js`, datos reales, Supabase ni el hosting. No se ha autorizado merge ni despliegue.

**Siguiente tarea independiente:** revisar históricamente la exposición de datos y artefactos existentes antes de proponer publicación; después, con una propuesta de hosting autorizado, evaluar autenticación y revocación individuales. No incorporar fichajes reales al repositorio público. Mantener aparte el PR #1 de privacidad y la rama `fix/jornada-empresa-manifest-20261026` hasta revisión. Respetar prioridad global de VISURA AUTO-DEV.
