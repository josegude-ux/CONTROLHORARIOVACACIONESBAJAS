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
```

El script solo lee `data.js` y devuelve código `0` si coincide con la **plantilla ficticia estricta** auditada. Rechaza nombres diferentes, datos de fichajes/calendario, campos no esperados, duplicados JSON, saldos no nulos y otros cambios de esquema. Rechaza por defecto los futuros cambios de estructura hasta que se revisen de forma consciente. **No elimina archivos ni modifica datos.**

**Pruebas de desarrollo del validador:** sintéticas locales: demo válida, nombre cambiado, registro de fichaje, marca de calendario, campo extra y clave JSON duplicada. Las cinco variantes indebidas fueron rechazadas. La comprobación del `data.js` remoto se hizo adicionalmente por inspección estructural del JSON, no ejecutando el programa Python descargado del propio repositorio. No existe CI remoto incorporado a este hito.

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
