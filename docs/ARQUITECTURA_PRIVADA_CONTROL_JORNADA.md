# Arquitectura de acceso privado — Control Jornada Empresa

**Propuesta técnica, no implantación.** Corte: 26/10/2026. Versión actual en `main`: 0.9.0. PR de referencia: #1, borrador.

## 1. Observaciones verificadas del código actual

- `index.html` incluye `data.js` como archivo estático; el navegador recibe el conjunto completo de la demo.
- `data.js` contiene 12 trabajadores ficticios; el paquete público no debe sustituirse por fichas reales.
- `app.js` es una aplicación de consulta: `persist()` no escribe datos, aunque hay exportaciones JSON/CSV y una interfaz global `window.CJBridge.setData` que permite sustituir los datos cargados **en la sesión del navegador**. No constituye autenticación ni persistencia oficial.
- La revisión PDF se efectúa en el navegador, con extractor experimental y exportación local de CSV. No es una importación validada al Excel.
- El `sw.js` actual almacena `./data.js` en Cache Storage para uso offline. **Esto es aceptable para la demo ficticia, no para expedientes laborales sin una revisión específica**.
- No se ha identificado un backend de empleados ni control de acceso entre personas en esta PWA. Un formulario de contraseña solo en JavaScript no protegería los archivos públicos.
- Estado de publicación: GitHub comunica `has_pages: true`, pero ni el sitio efectivo ni su configuración han podido validarse en este trabajo.

## 2. Diferenciar dos modelos de operación

### A. Consulta administrativa local (piloto sin backend compartido)
- Solo un equipo administrado, con acceso a sus archivos locales mediante las autorizaciones del sistema operativo.
- Excel/PDF de origen conservados en dispositivo/almacenamiento empresarial autorizados; importación y vista previa **estrictamente local** y sin subir los datos a la web pública.
- La demo pública separada conserva exclusivamente datos ficticios.
- Ventaja: menor superficie remota. Limitaciones: no es multiusuario, no resuelve revocación remota, depende de gestión y protección del equipo y no sustituye registros oficiales.
- Antes de implementar, validar cifrado del dispositivo, copias, bloqueo de pantalla, gestión de descargas y limpieza de archivos temporales.

### B. Consulta empresarial multiusuario (si acceden empleados y responsables)
- Frontend servido por un entorno autorizado; backend privado con **autenticación por usuario**, sesiones revocables y permisos en servidor/BD.
- Roles mínimos propuestos: `administrador` (importa, valida y administra), `responsable` (solo equipo autorizado) y `empleado` (únicamente sus datos), si estos roles son confirmados.
- Ningún Excel/PDF real ni `data.js` con empleados reales se publica como asset estático. Los datos se sirven desde una API autenticada con filtros obligatorios aplicados en el servidor, nunca solo escondiendo botones.
- Importación: subida autorizada, vista previa, comprobación de correspondencias, aprobación humana, versión del archivo, quién importa y cuándo, y registro de cambios. Los valores oficiales de horas y vacaciones se leen del Excel sin recalcularse en la app.
- Documentos PDF privados: almacenamiento con permisos por objeto, límites de tamaño y tipo, tratamiento de errores y prohibición de enlaces públicos permanentes.
- Sesiones: MFA para administradores cuando sea posible, revocación individual, caducidad, cierre de sesión y respuesta a pérdida de dispositivo.
- Caché: separar recursos públicos (HTML/CSS/JS) de datos personales. Para peticiones autenticadas fijar `Cache-Control: no-store` donde corresponda, revisar Service Worker, Cache Storage, navegadores compartidos y exportaciones/descargas. Deshabilitar caché offline de datos personales hasta validar un diseño seguro.
- Auditoría: quién consulta/cambia información, cuándo y motivo/operación; retención definida con asesoramiento jurídico y política empresarial. No registrar contraseñas, tokens, contenido íntegro de fichajes ni datos sensibles en logs.

## 3. Matriz de autorización propuesta, NO implementada

| Recurso | Empleado | Responsable | Administrador |
|---|---|---|---|
| Ficha propia | Leer | Leer solo equipo autorizado | Leer según función |
| Ficha de otro trabajador | Denegado | Solo equipo asignado | Según necesidad operativa |
| Vacaciones y ausencias personales | Leer | Leer solo equipo asignado | Leer/gestionar según permisos |
| Importar Excel/PDF | Denegado | Denegado por defecto | Permitido con validación y trazabilidad |
| Exportar datos de toda la empresa | Denegado | Denegado por defecto | Bajo permiso específico |
| Alta/revocación de usuarios | Denegado | Denegado | Solo administración autorizada |

La matriz requiere aprobación funcional y evaluación de protección de datos antes de escribir permisos reales.

## 4. Pruebas obligatorias antes de pasar a producción

1. Acceso anónimo a rutas `/data.js`, documentos, APIs, archivos exportados y cachés: **no debe revelar datos reales**.
2. Un empleado no puede recuperar datos ajenos manipulando ID, filtro, URL, petición o interfaz.
3. Revocar sesión/usuario inutiliza nuevas consultas; pérdida de terminal documentada y probada.
4. Los valores importados coinciden con el Excel oficial; diferencias se muestran como incidencias, no se corrigen silenciosamente.
5. PDF corrupto, de origen desconocido, muy grande o con formato inesperado no introduce datos en el histórico sin revisión humana.
6. Cachés, Service Worker, exportaciones CSV/JSON y la gestión de actualización PWA se prueban con datos ficticios antes de almacenar nada real.
7. No hay datos personales ni secretos en repositorio, GitHub Pages, ramas, artefactos ni CI.
8. Los tests de privacidad automatizados y controles humanos se ejecutan antes de cualquier publicación; la validación actual solo protege **la plantilla ficticia de `data.js`**.

## 5. Decisiones y dependencias aún abiertas

- ¿Será herramienta usada solo por personal de administración o también por cada empleado? Esto determina si basta un piloto local o se requiere autenticación multiusuario y permisos por fila.
- ¿Cuál es el entorno corporativo autorizado para alojar la versión privada? No se ha verificado ninguno.
- ¿Qué datos concretos de Excel se deben consultar y quién valida cambios? No implementar sincronización automática ni cálculos oficiales nuevos sin definición.
- Confirmar política empresarial de conservación, derechos de acceso, copias y pérdida de dispositivos.
- Elegir método de autenticación/backend **solo después** de confirmar el alcance. No conectar por defecto los datos con el Supabase de otro proyecto.
- Mantener como referencia la versión ficticia 0.9.0; no presentar esta propuesta como sistema privado terminado.

**Bloqueo para producción:** hasta cerrar esas decisiones y verificar infraestructura, no cargar información laboral real, fusionar PR de privacidad ni publicar una versión multiusuario.
