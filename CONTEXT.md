# Contexto del proyecto: Sistema de Solicitud de Auditoría UMSNH

## Resumen
Sistema web Django para el proceso de entrega-recepción de funcionarios de la Universidad Michoacana de San Nicolás de Hidalgo (UMSNH). Permite a funcionarios solicitar una auditoría mediante un oficio, con dos perfiles: usuario-funcionario y administrador.

## Stack
- Python 3.9, Django 4.2.28
- SQLite (db.sqlite3)
- Pillow 11.3.0
- fpdf2 2.8.4 (generación de PDF)
- Templates HTML propias + CSS minimalista (static/css/style.css)

## Estructura
```
proyecto_auditoria/  (raíz: C:\Users\alons\Documents\Proyecto predeterminado)
├── manage.py
├── config/            # settings, urls, wsgi
├── core/              # home, auth, dashboard
├── solicitudes/       # modelo SolicitudAuditoria, formularios, vistas usuario
├── admin_panel/       # panel admin, FormatoOficio, generación PDF, edición
├── templates/         # base.html + templates por app
├── static/css/style.css
├── media/             # archivos subidos (nombramientos)
├── requirements.txt
└── CONTEXT.md
```

## Modelos
- SolicitudAuditoria: usuario(FK), nombre, unidad_responsable, fecha_inicio_encargo, fecha_final_encargo, solicitud_especial, nombramiento(FileField), estado, observaciones_admin, timestamps.
- FormatoOficio: nombre, plantilla_html, activo, creado_por, timestamps.

## Roles
- is_staff/is_superuser = administrador (panel /panel/)
- Usuarios normales = funcionarios (/solicitudes/)

## Rutas principales
- / (home), /login/, /registro/, /dashboard/
- /solicitudes/nueva/, /solicitudes/mis/, /solicitudes/<pk>/, /solicitudes/<pk>/pdf/
- /panel/, /panel/solicitudes/, /panel/solicitudes/<pk>/, /panel/solicitudes/<pk>/editar/, /panel/solicitudes/<pk>/pdf/
- /panel/formatos/, /panel/formatos/nuevo/, /panel/formatos/<pk>/editar/

## Credenciales de prueba
- Superusuario: LeoAlonso01 / Chumel.0526 (alonsoledesmal@gmail.com)
- También existe: admin / admin123

## Notas importantes
- PDF se genera con fpdf2; usar bytes(pdf.output(dest='S')) (no .encode).
- Archivos subidos en media/nombramientos/%Y/%m/.
- Validación: solo PDF/JPG, máx 5MB; fecha final >= fecha inicio.
- Idioma es-MX, zona America/Mexico_City.
- PocketBase: pendiente para migración solo de carga de archivos; actualmente storage local.

## Pendientes
- Pruebas automatizadas.
- Dockerfile.
- Migración de carga de archivos a PocketBase.