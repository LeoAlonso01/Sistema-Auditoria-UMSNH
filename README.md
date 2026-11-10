# Sistema Auditoría UMSNH

Sistema web para la gestión y seguimiento de auditorías en la UMSNH.

## Tecnologías

- Python
- Django
- Base de datos local (SQLite) para desarrollo

## Requisitos

- Python 3.x

## Instalación (desarrollo)

```bash
python -m venv .venv
# En Windows PowerShell:
#   .venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Estructura

- `core/`: configuración principal del proyecto
- `admin_panel/`: funcionalidades del panel administrativo
- `solicitudes/`: módulos relacionados con solicitudes/procesos
- `templates/`, `static/`, `media/`: recursos de frontend y archivos

## Notas

- `db.sqlite3` se ignora en Git para evitar conflictos entre entornos.
