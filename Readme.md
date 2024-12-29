# Quadra - Descubre la Mejor Comida Callejera

Quadra es una aplicación web que permite a los usuarios descubrir, calificar y compartir puestos de comida callejera. La plataforma facilita la conexión entre amantes de la comida callejera y los mejores puestos de su área, creando una comunidad activa de entusiastas gastronómicos.

## Características Principales

La aplicación ofrece las siguientes funcionalidades:

- Geolocalización de puestos de comida con mapas interactivos
- Sistema de reseñas y calificaciones
- Galería de fotos para cada puesto
- Perfiles de usuario personalizados
- Búsqueda avanzada por tipo de comida y ubicación
- Interfaz responsive adaptable a diferentes dispositivos

## Requisitos Previos

Para ejecutar Quadra en su entorno local, necesitará:

- Python 3.8 o superior
- PostgreSQL 12 o superior
- pip (gestor de paquetes de Python)

## Instrucciones de Ejecución

Siga estos pasos para ejecutar el proyecto en su entorno local:

1. Clone el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/quadra.git
   cd quadra
   ```

2. Cree y active un entorno virtual:
   ```bash
   python -m venv venv

   # En Windows:
   .\venv\Scripts\activate

   # En Unix o MacOS:
   source venv/bin/activate
   ```

3. Instale las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure la base de datos:
   ```sql
   CREATE DATABASE quadra;
   ```

5. Configure las variables de entorno:
   ```bash
   # Copie el archivo de ejemplo
   cp .env.example .env

   # Edite el archivo .env con sus configuraciones
   # DATABASE_URL=postgresql://usuario:contraseña@localhost/quadra
   ```

6. Inicialice la base de datos:
   ```bash
   flask db upgrade
   ```

7. Ejecute la aplicación:
   ```bash
   flask run
   ```

La aplicación estará disponible en `http://localhost:5000`

## Estructura del Proyecto

```
quadra/
├── app/
│   ├── __init__.py
│   ├── models/          # Modelos de la base de datos
│   ├── routes/          # Rutas y controladores
│   ├── templates/       # Plantillas HTML
│   └── static/          # Archivos estáticos
├── migrations/          # Migraciones de la base de datos
├── tests/              # Pruebas unitarias
├── config.py           # Configuración del proyecto
├── requirements.txt    # Dependencias del proyecto
└── run.py             # Punto de entrada de la aplicación
```

## Uso del Sistema

Una vez que la aplicación esté en ejecución, podrá:

1. Crear una cuenta de usuario nueva
2. Explorar puestos de comida en el mapa
3. Ver detalles de cada puesto
4. Agregar reseñas y calificaciones
5. Subir fotos de los puestos
6. Buscar puestos por tipo de comida o ubicación

## Problemas Comunes

Si encuentra algún problema durante la instalación o ejecución:

1. Asegúrese de que todas las dependencias estén instaladas correctamente
2. Verifique que PostgreSQL esté en ejecución
3. Confirme que las variables de entorno estén configuradas correctamente
4. Revise que el puerto 5000 esté disponible

## Contacto

Para cualquier consulta sobre el proyecto, puede contactar a:

[Tu Nombre]
Correo: [tu-correo@ejemplo.com]