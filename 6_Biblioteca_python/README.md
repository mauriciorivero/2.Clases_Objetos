# 📚 Tutorial Backend Python - Sistema de Biblioteca

Tutorial completo para aprender a crear aplicaciones backend con **Flask** y **FastAPI**, usando Python del lado del servidor.

## 🎯 Objetivos

- Entender los conceptos de backend y APIs REST
- Implementar operaciones CRUD completas
- Comparar Flask y FastAPI en un proyecto real
- Probar endpoints desde el navegador
- Aplicar buenas prácticas de desarrollo

---

## 📋 Contenido del Proyecto

```
6_Biblioteca_python/
├── Libro.py              # Clase de dominio (modelo de negocio)
├── app_flask.py          # Aplicación backend con Flask
├── app_fastapi.py        # Aplicación backend con FastAPI
├── requirements.txt      # Dependencias del proyecto
├── tutorial.html         # Diapositivas interactivas del tutorial
└── README.md            # Este archivo
```

---

## 🚀 Instalación

### Paso 1: Verificar Python

```bash
python --version
# Debe ser Python 3.7 o superior
```

### Paso 2: Crear entorno virtual (recomendado)

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En Windows:
venv\Scripts\activate
# En Mac/Linux:
source venv/bin/activate
```

### Paso 3: Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 🎓 Tutorial Interactivo

Abre el archivo `tutorial.html` en tu navegador para acceder a las **18 diapositivas interactivas** que explican:

1. ¿Qué es el Backend?
2. Arquitectura Cliente-Servidor
3. Métodos HTTP (GET, POST, PUT, DELETE)
4. Comparación Flask vs FastAPI
5. Python del lado del servidor
6. Implementación paso a paso
7. Cómo probar la API
8. Mejores prácticas

**Para abrir el tutorial:**
- **Doble clic** en `tutorial.html`, o
- **Arrastrar** el archivo a tu navegador, o
- **Desde terminal:** `open tutorial.html` (Mac) / `start tutorial.html` (Windows)

---

## 🏃 Ejecutar las Aplicaciones

### Opción 1: Flask

```bash
python app_flask.py
```

**El servidor estará disponible en:**
- 🌐 http://localhost:5000
- 📚 http://localhost:5000/libros

**Detener el servidor:** `Ctrl + C`

### Opción 2: FastAPI

```bash
uvicorn app_fastapi:app --reload
```

**El servidor estará disponible en:**
- 🌐 http://localhost:8000
- 📚 http://localhost:8000/libros
- 📖 **Documentación interactiva:** http://localhost:8000/docs
- 📄 **Documentación alternativa:** http://localhost:8000/redoc

**Detener el servidor:** `Ctrl + C`

---

## 🔗 Endpoints Disponibles

### Ambas aplicaciones (Flask y FastAPI) implementan:

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| **GET** | `/` | Información de la API |
| **GET** | `/libros` | Obtener todos los libros |
| **GET** | `/libros/{isbn}` | Obtener un libro específico |
| **POST** | `/libros` | Crear un nuevo libro |
| **PUT** | `/libros/{isbn}` | Actualizar un libro completo |
| **PATCH** | `/libros/{isbn}` | Actualizar parcialmente (solo FastAPI) |
| **DELETE** | `/libros/{isbn}` | Eliminar un libro |
| **POST** | `/libros/{isbn}/prestar` | Prestar un libro |
| **POST** | `/libros/{isbn}/devolver` | Devolver un libro |

### Solo FastAPI:

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| **GET** | `/libros/filtro/disponibles` | Libros disponibles |
| **GET** | `/libros/filtro/prestados` | Libros prestados |

---

## 🧪 Probar la API

### 1. Desde el Navegador (solo GET)

Abre tu navegador y visita:

```
http://localhost:5000/libros  (Flask)
http://localhost:8000/libros  (FastAPI)
```

### 2. Swagger UI (solo FastAPI)

FastAPI incluye documentación interactiva automática:

```
http://localhost:8000/docs
```

Desde aquí puedes:
- ✅ Ver todos los endpoints
- ✅ Probar cada endpoint con datos de ejemplo
- ✅ Ver las respuestas en tiempo real

### 3. Usando cURL (terminal)

```bash
# Obtener todos los libros
curl http://localhost:8000/libros

# Crear un nuevo libro
curl -X POST http://localhost:8000/libros \
  -H "Content-Type: application/json" \
  -d '{
    "titulo": "El Quijote",
    "isbn": "978-1234567890",
    "autor": "Cervantes",
    "anio": 1605,
    "paginas": 863,
    "disponible": true
  }'

# Obtener un libro específico
curl http://localhost:8000/libros/978-1234567890

# Prestar un libro
curl -X POST http://localhost:8000/libros/978-1234567890/prestar

# Devolver un libro
curl -X POST http://localhost:8000/libros/978-1234567890/devolver

# Eliminar un libro
curl -X DELETE http://localhost:8000/libros/978-1234567890
```

### 4. Herramientas Recomendadas

- **Postman** - https://www.postman.com/
- **Insomnia** - https://insomnia.rest/
- **Thunder Client** (extensión VS Code)
- **REST Client** (extensión VS Code)

---

## 📊 Estructura de Datos

### Ejemplo de Libro (JSON)

```json
{
  "isbn": "978-0-307-47472-3",
  "titulo": "Cien Años de Soledad",
  "autor": "Gabriel García Márquez",
  "anio": 1967,
  "paginas": 417,
  "disponible": true
}
```

### Crear un Libro (POST)

```json
{
  "titulo": "El Principito",
  "isbn": "978-0-15-601219-1",
  "autor": "Antoine de Saint-Exupéry",
  "anio": 1943,
  "paginas": 96,
  "disponible": true
}
```

---

## 🎓 Conceptos Clave

### 1. API REST
**REST** (Representational State Transfer) es un estilo arquitectónico para crear APIs usando HTTP. Las operaciones se realizan mediante métodos HTTP:

- **GET:** Leer datos
- **POST:** Crear nuevos recursos
- **PUT/PATCH:** Actualizar recursos existentes
- **DELETE:** Eliminar recursos

### 2. JSON
**JSON** (JavaScript Object Notation) es el formato estándar para intercambiar datos entre cliente y servidor.

### 3. Endpoint
Una **URL específica** que realiza una acción determinada. Ejemplo: `/libros` para obtener todos los libros.

### 4. CRUD
Acrónimo de las operaciones básicas:
- **C**reate (Crear)
- **R**ead (Leer)
- **U**pdate (Actualizar)
- **D**elete (Eliminar)

### 5. Códigos de Estado HTTP
- **200:** OK - Solicitud exitosa
- **201:** Created - Recurso creado
- **400:** Bad Request - Datos inválidos
- **404:** Not Found - Recurso no encontrado
- **500:** Internal Server Error - Error del servidor

---

## ⚖️ Flask vs FastAPI - Comparación

| Característica | Flask | FastAPI |
|----------------|-------|---------|
| **Año de creación** | 2010 | 2018 |
| **Rendimiento** | Bueno | Excelente |
| **Validación** | Manual | Automática |
| **Documentación** | Manual | Automática |
| **Curva de aprendizaje** | Fácil | Media |
| **Mejor para** | Proyectos pequeños/medianos | APIs modernas profesionales |

### ¿Cuál usar?

- **Flask:** Ideal para **aprender** los conceptos básicos, proyectos pequeños o cuando necesitas máxima flexibilidad.
- **FastAPI:** Ideal para **producción**, APIs modernas, cuando necesitas alto rendimiento y validación automática.

---

## 💡 Diferencias Clave en el Código

### Flask

```python
@app.route('/libros', methods=['POST'])
def crear_libro():
    data = request.get_json()
    # Validación manual necesaria
    if 'titulo' not in data:
        return jsonify({"error": "Falta titulo"}), 400
    # ...
    return jsonify(resultado), 201
```

### FastAPI

```python
@app.post("/libros", status_code=201)
async def crear_libro(libro: LibroInput):
    # Pydantic valida automáticamente
    # Si falta un campo, responde automáticamente con 422
    # ...
    return resultado
```

**Ventajas FastAPI:**
- ✅ Validación automática con Pydantic
- ✅ Documentación interactiva en `/docs`
- ✅ Mejor rendimiento (asíncrono)
- ✅ Type hints modernos

---

## 📚 Estructura de la Clase Libro

La clase `Libro.py` usa **encapsulamiento** con atributos privados:

```python
class Libro:
    def __init__(self, title, isbn, author, year, num_pages, available):
        self.__title = title        # Atributo privado
        self.__isbn = isbn
        # ...
    
    @property
    def title(self):               # Getter
        return self.__title
    
    @title.setter
    def title(self, value):        # Setter
        self.__title = value
    
    def loan(self):                # Método de negocio
        self.__is_available = False
```

**Conceptos:**
- `__attribute`: Atributo privado (encapsulamiento)
- `@property`: Getter (obtener valor)
- `@attribute.setter`: Setter (modificar valor)
- Métodos de negocio: `loan()`, `return_book()`

---

## 🔧 Extensiones Posibles

### 1. Base de Datos Real
Reemplazar la lista en memoria con SQLAlchemy:

```python
from sqlalchemy import create_engine
# Conectar a PostgreSQL, MySQL, SQLite, etc.
```

### 2. Autenticación
Agregar JWT (JSON Web Tokens) para proteger endpoints:

```python
from fastapi.security import HTTPBearer
```

### 3. Paginación
Para listas grandes:

```python
@app.get("/libros")
def obtener_libros(skip: int = 0, limit: int = 10):
    return libros[skip:skip+limit]
```

### 4. Búsqueda y Filtros
```python
@app.get("/libros/buscar")
def buscar_libros(autor: str = None, anio: int = None):
    # Implementar búsqueda
```

### 5. Tests Automatizados
```python
import pytest
from fastapi.testclient import TestClient

def test_obtener_libros():
    response = client.get("/libros")
    assert response.status_code == 200
```

---

## 🎓 Recursos de Aprendizaje

### Documentación Oficial
- **Flask:** https://flask.palletsprojects.com/
- **FastAPI:** https://fastapi.tiangolo.com/
- **Python:** https://docs.python.org/es/

### Tutoriales Recomendados
- Real Python - Flask Tutorial
- FastAPI Official Tutorial
- REST API Best Practices

### Videos
- Buscar en YouTube: "Flask tutorial español"
- Buscar en YouTube: "FastAPI tutorial español"

---

## ❓ Solución de Problemas

### Error: "ModuleNotFoundError: No module named 'flask'"
**Solución:** Instalar dependencias
```bash
pip install -r requirements.txt
```

### Error: "Address already in use"
**Solución:** El puerto está ocupado. Cambiar el puerto:
```bash
# Flask
python app_flask.py  # Modificar port=5001 en el código

# FastAPI
uvicorn app_fastapi:app --reload --port 8001
```

### Error: "No module named 'Libro'"
**Solución:** Ejecutar desde el directorio correcto:
```bash
cd 6_Biblioteca_python
python app_flask.py
```

### Flask no recarga automáticamente
**Solución:** Verificar que debug=True esté activo en el código

---

## 📝 Ejercicios Propuestos

### Nivel Básico
1. ✅ Agregar un endpoint para contar total de libros
2. ✅ Crear un endpoint para buscar por autor
3. ✅ Agregar validación de año (no permitir años futuros)

### Nivel Intermedio
4. ✅ Implementar paginación (skip, limit)
5. ✅ Agregar un campo "editorial" a la clase Libro
6. ✅ Crear endpoint para obtener estadísticas (total disponibles, prestados, etc.)

### Nivel Avanzado
7. ✅ Conectar a base de datos SQLite
8. ✅ Implementar autenticación con JWT
9. ✅ Agregar tests con pytest
10. ✅ Desplegar en Heroku o DigitalOcean

---

## 🤝 Contribuir

Este es un proyecto educativo. Siéntete libre de:
- Reportar errores
- Sugerir mejoras
- Crear pull requests
- Compartir con otros estudiantes

---

## 📄 Licencia

Este proyecto es de uso educativo para el SENA 2025.

---

## ✨ Autor

**SENA 2025 - Programación Web**
Ficha: 3287281
Tema: Python Django - Clases y Objetos

---

## 🎉 ¡Éxito en tu Aprendizaje!

Recuerda:
1. 📖 Lee las diapositivas (`tutorial.html`)
2. 💻 Practica con el código
3. 🧪 Prueba los endpoints
4. 🔍 Experimenta y modifica
5. 🚀 Construye tus propios proyectos

**¡La práctica hace al maestro! 🎯**

