# ⚡ Guía Rápida - Backend Python

## 🚀 Inicio Rápido en 3 Pasos

### 1️⃣ Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 2️⃣ Ejecutar Servidor

**Opción A: Flask**
```bash
python app_flask.py
```
➡️ Abre: http://localhost:5000/libros

**Opción B: FastAPI**
```bash
uvicorn app_fastapi:app --reload
```
➡️ Abre: http://localhost:8000/libros
➡️ Docs: http://localhost:8000/docs

### 3️⃣ Probar en el Navegador
- Visita la URL del servidor
- Verás los libros en formato JSON

---

## 📚 Tutorial Completo

Abre `tutorial.html` en tu navegador para las 18 diapositivas explicativas.

---

## 🎯 Endpoints Principales

| Método | URL | Acción |
|--------|-----|--------|
| GET | `/libros` | Ver todos |
| GET | `/libros/{isbn}` | Ver uno |
| POST | `/libros` | Crear |
| PUT | `/libros/{isbn}` | Actualizar |
| DELETE | `/libros/{isbn}` | Eliminar |
| POST | `/libros/{isbn}/prestar` | Prestar |
| POST | `/libros/{isbn}/devolver` | Devolver |

---

## 🧪 Probar la API

### Navegador (solo GET)
```
http://localhost:8000/libros
```

### Swagger UI (solo FastAPI)
```
http://localhost:8000/docs
```

### Script Python
```bash
pip install requests
python ejemplo_pruebas.py
```

### cURL
```bash
curl http://localhost:8000/libros
```

Ver más ejemplos en `ejemplos_curl.md`

---

## 📊 Ejemplo de JSON

### Libro
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

### Crear Libro (POST)
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

## 🔧 Solución de Problemas

### "ModuleNotFoundError"
```bash
pip install -r requirements.txt
```

### "Address already in use"
```bash
# Cambiar puerto
uvicorn app_fastapi:app --reload --port 8001
```

### "Connection refused"
Verifica que el servidor esté corriendo.

---

## 📖 Archivos del Proyecto

```
├── tutorial.html          ← 18 diapositivas explicativas
├── app_flask.py          ← Aplicación Flask
├── app_fastapi.py        ← Aplicación FastAPI
├── Libro.py              ← Clase de dominio
├── ejemplo_pruebas.py    ← Script de pruebas
├── ejemplos_curl.md      ← Comandos cURL
├── requirements.txt      ← Dependencias
├── README.md             ← Documentación completa
└── GUIA_RAPIDA.md        ← Este archivo
```

---

## 💡 Conceptos Clave

**API REST**: Interfaz para comunicación entre aplicaciones
**CRUD**: Create, Read, Update, Delete
**JSON**: Formato de intercambio de datos
**Endpoint**: URL que realiza una acción específica

---

## ⚖️ Flask vs FastAPI

| | Flask | FastAPI |
|-|-------|---------|
| **Para aprender** | ✅ Más fácil | 🔶 Medio |
| **Para producción** | ✅ Bueno | ✅ Excelente |
| **Documentación** | ❌ Manual | ✅ Automática |
| **Validación** | ❌ Manual | ✅ Automática |
| **Rendimiento** | ✅ Bueno | ⚡ Excelente |

---

## 🎓 Aprende Más

1. Lee `README.md` para documentación completa
2. Abre `tutorial.html` para el paso a paso
3. Ejecuta `ejemplo_pruebas.py` para ver la API en acción
4. Consulta `ejemplos_curl.md` para comandos de terminal

---

## 🚀 Próximos Pasos

1. ✅ Ejecutar y probar la API
2. ✅ Leer las diapositivas del tutorial
3. ✅ Experimentar con el código
4. ✅ Crear tus propios endpoints
5. ✅ Agregar base de datos real
6. ✅ Implementar autenticación
7. ✅ Desplegar en la nube

---

## 📞 Recursos

- **Flask:** https://flask.palletsprojects.com/
- **FastAPI:** https://fastapi.tiangolo.com/
- **Python:** https://docs.python.org/es/

---

¡Éxito en tu aprendizaje! 🎉

