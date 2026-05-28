# Django-L3

## Descripción

Este proyecto es una **landing page** educativa desarrollada con Django. Incluye varias secciones accesibles desde el menú principal:
- Inicio
- Servicios
- Precios
- Clientes
- Contacto

Cada sección corresponde a una vista y plantilla diferente. El objetivo es mostrar cómo estructurar una aplicación Django básica con rutas, vistas y plantillas personalizadas.

## Estructura del proyecto

- `landing/` — Proyecto principal de Django
  - `manage.py` — Comando principal para gestionar el proyecto
  - `landing/settings.py` — Configuración general
  - `landing/urls.py` — Rutas principales
  - `web_landing/` — Aplicación principal con las vistas
  - `templates/` — Plantillas HTML
  - `static/` — Archivos estáticos (CSS)

## Requisitos previos

- Python 3.10+
- Django 6.x

## Instalación y uso paso a paso

1. **Clona el repositorio o descarga el código.**

2. **Crea un entorno virtual (opcional pero recomendado):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instala Django:**
   ```bash
   pip install django
   ```

4. **Accede a la carpeta del proyecto:**
   ```bash
   cd landing
   ```

5. **Ejecuta las migraciones iniciales:**
   ```bash
   python manage.py migrate
   ```

6. **Inicia el servidor de desarrollo:**
   ```bash
   python manage.py runserver
   ```

7. **Abre tu navegador y visita:**
   [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## ¿Qué hace la aplicación?

- Muestra una landing page con navegación entre secciones.
- Cada sección tiene su propia URL y plantilla.
- El diseño es responsivo y utiliza CSS personalizado.

## Estructura de URLs principales

- `/` — Inicio
- `/servicios/` — Servicios
- `/precios/` — Precios
- `/clientes/` — Clientes
- `/contacto/` — Contacto

## Personalización

Puedes modificar las plantillas en la carpeta `templates/web_landing/` y los estilos en `static/css/styles.css`.

---

Proyecto educativo para aprender los fundamentos de Django.
