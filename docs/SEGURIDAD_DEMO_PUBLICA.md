# Control Jornada — Seguridad de la demo pública

**Fecha del control:** 2026-10-26  
**Repositorio:** `josegude-ux/CONTROLHORARIOVACACIONESBAJAS`  
**Base inspeccionada:** `main` en `7e119417cd8db948d9a8ce239691612de68de042`  
**Rama de esta mejora:** `audit/jornada-demo-privacidad-20261026`  
**Estado:** revisión limitada + prevención local. No es una certificación RGPD, un informe de pentesting ni permiso de despliegue.

## Hallazgos observados

- La versión declarada es `0.9.0` (2026-10-22).
- El archivo `data.js` en la revisión auditada identifica sus datos como demostración ficticia. Se comprobaron 12 empleados con nombres secuenciales del tipo `Empleado de prueba NN`, IDs secuenciales, sin `records`, `marks`, `holidays` ni `audit`. No se observaron patrones de credenciales comunes en los archivos de texto de la raíz revisados. **Este resultado NO descarta datos privados en commits históricos, archivos no inspeccionados, backups o alojamiento.**
- `index.html` carga `data.js` en el navegador; `sw.js` lo añade a la caché local de la PWA. Nunca debe incrustarse información real de plantilla o fichajes en una variante pública.
- `LEEME.txt` documenta la variante privada/experimental de importación PDF; `LEEME_GITHUB.txt` describe la demo ficticia; `LEEME_MOVIL.txt` refería datos reales de una variante privada. Las instrucciones deben distinguirlas explícitamente.
- El repositorio GitHub es **público**. Ni GitHub Pages ni una dirección HTTPS pública convierten por sí mismos los datos en privados. El cacheado de una PWA tampoco da confidencialidad.
- La app **no reemplaza al Excel de origen**, que conserva los cálculos oficiales de jornada y vacaciones. La extracción PDF es experimental, sin OCR y requiere revisión humana.

## Control reproducible, previo a publicar una demo

Desde la raíz del repositorio, con Python 3, ejecutar:

```sh
python scripts/verificar_demo_publica.py
python -m unittest discover -s tests -v
```

El script solo lee `data.js` y devuelve código `0` si coincide con la **plantilla ficticia estricta** auditada. Rechaza nombres diferentes, datos de fichajes/calendario, campos no esperados, duplicados JSON, saldos no nulos y otros cambios de esquema. Rechaza por defecto los futuros cambios de estructura hasta que se revisen de forma consciente. **No elimina archivos ni modifica datos.**

**Pruebas de desarrollo del validador:** se añadió `tests/test_verificar_demo_publica.py` y se ejecutaron **19 pruebas sintéticas** en un entorno Python aislado. Todas finalizaron correctamente. Incluyen un caso válido y rechazos de cambios en nombres, IDs, estado del empleado, saldos, fechas, fichajes, marcas, campos extras, duplicados JSON, JavaScript adjunto, datos excesivamente largos, cambio de configuración y valores JSON no finitos. Además se ejecutó `py_compile` del validador y sus pruebas, y el validador contra una **plantilla sintética reconstruida** que coincide con los campos esperados. El `data.js` remoto se contrastó estructuralmente mediante lectura del contenido; no se ha ejecutado aquí el código desde un checkout remoto completo ni en CI. **Ninguna de estas comprobaciones equivale a protección automática de una publicación:** un operador debe ejecutarlas antes de cada despliegue.

## Reglas obligatorias antes de distribuir

1. Revisar manualmente **todos** los archivos preparados para publicación, su historial accesible, la configuración real de hosting y cualquier copia `data.js` en `main`, ramas o artefactos. El script **no cubre** esos canales.
2. No publicar archivos de Excel, PDF, `.csv`, `.zip`, `.ost`, copias `data-real.js` o datos personales como contenidos estáticos de acceso público.
3. Para datos de empresa, exigir **alojamiento con autenticación y control de acceso verificados**, o una importación local diseñada para no remitir datos a un servidor público. El mero enlace secreto no basta.
4. Si se importan PDFs, la extracción es orientativa. Cada fila debe contrastarse con su original antes de usarla. No enviar estos documentos a la demo pública.
5. No mezclar con `josegude-ux/mi-jornada` ni con el archivo Excel de horas. La web empresarial solo consulta información importada y no recalcula resultados oficiales.
6. Confirmar `main`, último commit, PR y cambios de otros chats antes de fusionar. **No desplegar, fusionar, publicar datos reales ni asumir seguridad porque pase el script.**

## Pendientes técnicos posteriores

- Revisar el historial completo y cualquier artefacto publicado: **no verificado aquí**.
- Inspeccionar y probar la privacidad de una propuesta de hosting empresarial real con credenciales individuales y revocación; hoy **no se ha confirmado ninguna instalación privada**.
- Validar en iPhone físico las actualizaciones PWA y las posibles cachés de versiones anteriores, antes de uso laboral.
- Realizar pruebas del extractor PDF con ejemplos sintéticos representativos.
- La corrección aislada del manifiesto legado está en `fix/jornada-empresa-manifest-20261026`, todavía sin integrar.

## Revisión adicional del historial accesible (26/10/2026)

Se inspeccionaron los **5 commits de `main`** devueltos por GitHub y sus listas de archivos modificados. Solo el commit `7e119417cd8db948d9a8ce239691612de68de042` añade `data.js`, con la plantilla ficticia descrita. En esas listas no se observaron documentos con extensiones habituales de Excel, PDF, CSV, ZIP o claves privadas. La búsqueda básica de patrones de correo, tokens y encabezados de claves privadas en los parches de texto accesibles no arrojó coincidencias.

**Limitación importante:** no se han analizado blobs binarios, referencias borradas no listadas, otros repositorios, copias descargadas ni artefactos ajenos al árbol Git. La ausencia de coincidencias no garantiza privacidad histórica. El historial público, si hubiera contenido sensible, no se sanea borrando el archivo actual.

**Configuración de GitHub:** el repositorio informa `has_pages: true`, por lo que existe indicación de funcionalidad Pages, pero **no se pudo confirmar desde esta auditoría la URL, la publicación efectiva, su configuración ni su contenido servido**. Tratar cualquier sitio Pages como público hasta comprobar lo contrario. El alojamiento privado empresarial continúa sin verificar.
