# 🌐 Ejemplos de cURL para Probar la API

Esta guía contiene ejemplos de comandos `curl` para probar todos los endpoints de la API.

## 📋 Configuración Inicial

```bash
# Para Flask
export BASE_URL="http://localhost:5000"

# Para FastAPI
export BASE_URL="http://localhost:8000"
```

---

## 1️⃣ Información de la API

```bash
curl $BASE_URL/
```

---

## 2️⃣ Obtener Todos los Libros (GET)

```bash
curl $BASE_URL/libros
```

**Con formato legible:**
```bash
curl $BASE_URL/libros | python -m json.tool
```

---

## 3️⃣ Obtener un Libro Específico (GET)

```bash
curl $BASE_URL/libros/978-0-307-47472-3
```

---

## 4️⃣ Crear un Nuevo Libro (POST)

```bash
curl -X POST $BASE_URL/libros \
  -H "Content-Type: application/json" \
  -d '{
    "titulo": "Harry Potter y la Piedra Filosofal",
    "isbn": "978-0-439-70818-8",
    "autor": "J.K. Rowling",
    "anio": 1997,
    "paginas": 309,
    "disponible": true
  }'
```

**Versión en una línea:**
```bash
curl -X POST $BASE_URL/libros -H "Content-Type: application/json" -d '{"titulo":"El Señor de los Anillos","isbn":"978-0-544-00341-5","autor":"J.R.R. Tolkien","anio":1954,"paginas":1178,"disponible":true}'
```

---

## 5️⃣ Actualizar un Libro Completo (PUT)

```bash
curl -X PUT $BASE_URL/libros/978-0-439-70818-8 \
  -H "Content-Type: application/json" \
  -d '{
    "titulo": "Harry Potter y la Piedra Filosofal (Edición Especial)",
    "isbn": "978-0-439-70818-8",
    "autor": "J.K. Rowling",
    "anio": 1997,
    "paginas": 320,
    "disponible": true
  }'
```

---

## 6️⃣ Actualizar Parcialmente (PATCH - solo FastAPI)

```bash
curl -X PATCH $BASE_URL/libros/978-0-439-70818-8 \
  -H "Content-Type: application/json" \
  -d '{
    "paginas": 350,
    "disponible": false
  }'
```

---

## 7️⃣ Prestar un Libro (POST)

```bash
curl -X POST $BASE_URL/libros/978-0-439-70818-8/prestar
```

---

## 8️⃣ Devolver un Libro (POST)

```bash
curl -X POST $BASE_URL/libros/978-0-439-70818-8/devolver
```

---

## 9️⃣ Eliminar un Libro (DELETE)

```bash
curl -X DELETE $BASE_URL/libros/978-0-439-70818-8
```

---

## 🔟 Filtrar Libros Disponibles (solo FastAPI)

```bash
curl $BASE_URL/libros/filtro/disponibles
```

---

## 1️⃣1️⃣ Filtrar Libros Prestados (solo FastAPI)

```bash
curl $BASE_URL/libros/filtro/prestados
```

---

## 📊 Ver Códigos de Estado HTTP

```bash
# Agregar -i para ver headers (incluye el código de estado)
curl -i $BASE_URL/libros

# Agregar -v para modo verbose (más información)
curl -v $BASE_URL/libros
```

---

## 🎯 Ejemplos Completos de Flujo

### Flujo 1: Crear, Consultar, Prestar y Eliminar

```bash
# 1. Crear un libro
curl -X POST $BASE_URL/libros \
  -H "Content-Type: application/json" \
  -d '{"titulo":"1984","isbn":"978-0-452-28423-4","autor":"George Orwell","anio":1949,"paginas":328,"disponible":true}'

# 2. Verificar que se creó
curl $BASE_URL/libros/978-0-452-28423-4

# 3. Prestar el libro
curl -X POST $BASE_URL/libros/978-0-452-28423-4/prestar

# 4. Verificar que está prestado
curl $BASE_URL/libros/978-0-452-28423-4

# 5. Devolver el libro
curl -X POST $BASE_URL/libros/978-0-452-28423-4/devolver

# 6. Eliminar el libro
curl -X DELETE $BASE_URL/libros/978-0-452-28423-4
```

### Flujo 2: Probar Errores

```bash
# Intentar obtener un libro que no existe (Error 404)
curl $BASE_URL/libros/999-9-999-99999-9

# Intentar crear un libro sin todos los campos (Error 400 o 422)
curl -X POST $BASE_URL/libros \
  -H "Content-Type: application/json" \
  -d '{"titulo":"Libro Incompleto"}'

# Intentar prestar un libro ya prestado (Error 400)
curl -X POST $BASE_URL/libros/978-0-15-601219-1/prestar
curl -X POST $BASE_URL/libros/978-0-15-601219-1/prestar
```

---

## 💡 Tips Útiles

### Guardar respuesta en archivo
```bash
curl $BASE_URL/libros > libros.json
```

### Medir tiempo de respuesta
```bash
curl -w "\nTiempo: %{time_total}s\n" $BASE_URL/libros
```

### Seguir redirecciones
```bash
curl -L $BASE_URL/libros
```

### Mostrar solo el código de estado
```bash
curl -s -o /dev/null -w "%{http_code}\n" $BASE_URL/libros
```

---

## 🛠️ Alternativas a cURL

### HTTPie (más amigable)
```bash
# Instalar: pip install httpie

# GET
http $BASE_URL/libros

# POST
http POST $BASE_URL/libros titulo="Libro" isbn="123" autor="Autor" anio:=2023 paginas:=200 disponible:=true
```

### Wget
```bash
wget -qO- $BASE_URL/libros
```

---

## 🎓 Recordatorios

- **GET**: No necesita `-X GET` (es el método por defecto)
- **POST/PUT/DELETE**: Siempre especificar con `-X`
- **JSON**: Siempre incluir header `Content-Type: application/json`
- **Datos**: Usar `-d` para el body

---

## 🔗 Documentación

- **cURL:** https://curl.se/docs/
- **HTTPie:** https://httpie.io/docs
- **REST API:** https://restfulapi.net/

---

¡Feliz testing! 🚀

