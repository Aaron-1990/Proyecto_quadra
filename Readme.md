# Quadra - Descubre la Mejor Comida Callejera

Quadra es una aplicación web que permite a los usuarios descubrir, calificar y compartir puestos de comida callejera. La plataforma facilita la conexión entre amantes de la comida callejera y los mejores puestos de su área.

## Características Implementadas

- Sistema de autenticación completo (registro e inicio de sesión)
- Geolocalización de puestos de comida con mapas interactivos usando Leaflet
- Sistema de reseñas y calificaciones
- Galería de fotos para cada puesto
- Búsqueda y filtrado de puestos por tipo de comida
- Visualización de ubicación actual del usuario
- Interfaz responsive con Tailwind CSS

## Requisitos Previos

Para ejecutar Quadra necesitará:

- Python 3.10 o superior
- SQLite (incluido en Python)
- pip (gestor de paquetes de Python)
- Navegador web moderno con soporte para geolocalización
- Conexión a Internet (para cargar mapas y estilos)

## Dependencias Externas (CDN)

El proyecto utiliza las siguientes bibliotecas que se cargan automáticamente vía CDN:

- **Tailwind CSS v3.x**
  - CDN: https://cdn.tailwindcss.com
  - Uso: Framework CSS para estilos y diseño responsive

- **Leaflet v1.9.4**
  - CSS: https://unpkg.com/leaflet@1.9.4/dist/leaflet.css
  - JavaScript: https://unpkg.com/leaflet@1.9.4/dist/leaflet.js
  - Uso: Visualización y manejo de mapas interactivos

Estas dependencias se cargan automáticamente desde los CDN y no requieren instalación local.

## Instrucciones de Instalación y Ejecución

1. Clone el repositorio:
   ```bash
   git clone <URL-del-repositorio>
   cd quadra
   ```

2. Cree y active un entorno virtual:
   ```bash
   python -m venv venv

   # En Windows:
   venv\Scripts\activate

   # En Unix o MacOS:
   source venv/bin/activate
   ```

3. Instale las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Inicialice la base de datos:
   ```bash
   flask db upgrade
   ```

5. Ejecute la aplicación:
   ```bash
   python src/run.py
   ```

La aplicación estará disponible en `http://127.0.0.1:5000/`

## Estructura del Proyecto

```
quadra/
├── src/
│   ├── __init__.py
│   ├── models/          # Modelos de la base de datos (User, Spot, Review, Photo)
│   ├── routes/          # Rutas (auth, spots, main)
│   ├── templates/       # Plantillas HTML
│   │   ├── auth/       # Plantillas de autenticación
│   │   ├── spots/      # Plantillas de puestos
│   │   └── base.html   # Plantilla base
│   └── static/         # Archivos estáticos (CSS, JS, imágenes)
├── migrations/         # Migraciones de la base de datos
├── docs/              # Documentación
├── tests/             # Pruebas
├── config.py         # Configuración
└── requirements.txt  # Dependencias
```

## Funcionalidades Principales

1. **Sistema de Usuarios**
   - Registro de nuevos usuarios
   - Inicio de sesión
   - Persistencia de sesiones

2. **Gestión de Puestos**
   - Creación de nuevos puestos
   - Carga de múltiples fotos
   - Geolocalización precisa
   - Información detallada (horarios, tipo de comida)

3. **Sistema de Reseñas**
   - Calificación con estrellas (1-5)
   - Comentarios detallados
   - Promedio de calificaciones
   - Validación para evitar reseñas duplicadas

4. **Búsqueda y Filtrado**
   - Filtro por tipo de comida
   - Búsqueda por nombre
   - Visualización en mapa
   - Lista de resultados actualizada en tiempo real

## Observaciones para la Evaluación

1. **Base de Datos**
   - El proyecto usa SQLite por simplicidad
   - La base de datos se crea automáticamente en `src/quadra.db`
   - Las migraciones están incluidas en el directorio `migrations/`

2. **Archivos Estáticos**
   - Las imágenes subidas se guardan en `src/static/uploads/`
   - Se incluyen algunas imágenes de ejemplo

3. **Dependencias Externas**
   - Leaflet para mapas
   - Tailwind CSS para estilos
   - Flask y sus extensiones para el backend

## Solución de Problemas Comunes

1. **Error al crear la base de datos**
   - Asegúrese de tener permisos de escritura en el directorio `src/`
   - Ejecute `flask db upgrade` para aplicar las migraciones

2. **Problemas con las imágenes**
   - Verifique que existe el directorio `src/static/uploads/`
   - Asegúrese de tener permisos de escritura en ese directorio

3. **Error en el mapa**
   - Verifique su conexión a internet (necesaria para cargar Leaflet)
   - Permita el acceso a su ubicación en el navegador
   - Si el mapa no carga, verifique la consola del navegador para errores

4. **Problemas con los estilos**
   - Verifique su conexión a internet (necesaria para cargar Tailwind CSS)
   - Si los estilos no cargan, intente limpiar la caché del navegador

## Contacto y Soporte

Para cualquier consulta sobre el proyecto o problemas de ejecución, puede contactar a:

[Aaron Zapata Trejo]
Matrícula: [2312055]
Correo: [aaron2312055@hybridge.education]