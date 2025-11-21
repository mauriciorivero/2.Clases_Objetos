"""
Aplicación Backend con Flask
Sistema de Biblioteca - CRUD completo

Este archivo implementa una API REST usando Flask para gestionar libros.
"""

from flask import Flask, jsonify, request
from Libro import Libro

# Crear instancia de la aplicación Flask
app = Flask(__name__)

# Base de datos en memoria (lista de libros)
# En producción, esto sería una base de datos real (PostgreSQL, MySQL, etc.)
libros = []

# Función auxiliar para convertir un objeto Libro a diccionario
def libro_to_dict(libro):
    """Convierte un objeto Libro a diccionario para serialización JSON"""
    return {
        "isbn": libro.isbn,
        "titulo": libro.title,
        "autor": libro.author,
        "anio": libro.publication_year,
        "paginas": libro.total_num_pages,
        "disponible": libro.is_available
    }

# Función auxiliar para encontrar un libro por ISBN
def buscar_libro_por_isbn(isbn):
    """Busca un libro en la lista por su ISBN"""
    for libro in libros:
        if libro.isbn == isbn:
            return libro
    return None


# ==================== ENDPOINTS ====================

# Ruta raíz - Información de la API
@app.route('/')
def home():
    """Endpoint principal que muestra información de la API"""
    return jsonify({
        "mensaje": "API de Biblioteca - Sistema de Gestión de Libros",
        "version": "1.0",
        "endpoints": {
            "GET /libros": "Obtener todos los libros",
            "GET /libros/<isbn>": "Obtener un libro específico",
            "POST /libros": "Crear un nuevo libro",
            "PUT /libros/<isbn>": "Actualizar un libro existente",
            "DELETE /libros/<isbn>": "Eliminar un libro",
            "POST /libros/<isbn>/prestar": "Prestar un libro",
            "POST /libros/<isbn>/devolver": "Devolver un libro"
        }
    })


# CREATE - Crear un nuevo libro
@app.route('/libros', methods=['POST'])
def crear_libro():
    """
    Crea un nuevo libro en la biblioteca
    Espera un JSON con: titulo, isbn, autor, anio, paginas, disponible
    """
    try:
        # Obtener datos del cuerpo de la solicitud
        data = request.get_json()
        
        # Validar que vengan todos los campos necesarios
        campos_requeridos = ['titulo', 'isbn', 'autor', 'anio', 'paginas', 'disponible']
        for campo in campos_requeridos:
            if campo not in data:
                return jsonify({"error": f"Falta el campo '{campo}'"}), 400
        
        # Verificar que el ISBN no exista ya
        if buscar_libro_por_isbn(data['isbn']):
            return jsonify({"error": "Ya existe un libro con ese ISBN"}), 400
        
        # Crear instancia de Libro
        nuevo_libro = Libro(
            title=data['titulo'],
            isbn=data['isbn'],
            author=data['autor'],
            year=data['anio'],
            num_pages=data['paginas'],
            available=data['disponible']
        )
        
        # Agregar a la lista
        libros.append(nuevo_libro)
        
        return jsonify({
            "mensaje": "Libro creado exitosamente",
            "libro": libro_to_dict(nuevo_libro)
        }), 201
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# READ - Obtener todos los libros
@app.route('/libros', methods=['GET'])
def obtener_libros():
    """
    Devuelve la lista completa de libros en formato JSON
    """
    lista_libros = [libro_to_dict(libro) for libro in libros]
    return jsonify({
        "total": len(lista_libros),
        "libros": lista_libros
    })


# READ - Obtener un libro específico por ISBN
@app.route('/libros/<string:isbn>', methods=['GET'])
def obtener_libro(isbn):
    """
    Devuelve la información de un libro específico buscado por ISBN
    """
    libro = buscar_libro_por_isbn(isbn)
    
    if libro is None:
        return jsonify({"error": "Libro no encontrado"}), 404
    
    return jsonify(libro_to_dict(libro))


# UPDATE - Actualizar un libro existente
@app.route('/libros/<string:isbn>', methods=['PUT'])
def actualizar_libro(isbn):
    """
    Actualiza la información de un libro existente
    """
    libro = buscar_libro_por_isbn(isbn)
    
    if libro is None:
        return jsonify({"error": "Libro no encontrado"}), 404
    
    try:
        data = request.get_json()
        
        # Actualizar solo los campos que vengan en la solicitud
        if 'titulo' in data:
            libro.title = data['titulo']
        if 'autor' in data:
            libro.author = data['autor']
        if 'anio' in data:
            libro.publication_year = data['anio']
        if 'paginas' in data:
            libro.total_num_pages = data['paginas']
        if 'disponible' in data:
            libro.is_available = data['disponible']
        
        return jsonify({
            "mensaje": "Libro actualizado exitosamente",
            "libro": libro_to_dict(libro)
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# DELETE - Eliminar un libro
@app.route('/libros/<string:isbn>', methods=['DELETE'])
def eliminar_libro(isbn):
    """
    Elimina un libro de la biblioteca
    """
    libro = buscar_libro_por_isbn(isbn)
    
    if libro is None:
        return jsonify({"error": "Libro no encontrado"}), 404
    
    libros.remove(libro)
    
    return jsonify({
        "mensaje": "Libro eliminado exitosamente",
        "isbn": isbn
    })


# CUSTOM - Prestar un libro
@app.route('/libros/<string:isbn>/prestar', methods=['POST'])
def prestar_libro(isbn):
    """
    Marca un libro como prestado (no disponible)
    """
    libro = buscar_libro_por_isbn(isbn)
    
    if libro is None:
        return jsonify({"error": "Libro no encontrado"}), 404
    
    if not libro.is_available:
        return jsonify({"error": "El libro ya está prestado"}), 400
    
    libro.loan()
    
    return jsonify({
        "mensaje": "Libro prestado exitosamente",
        "libro": libro_to_dict(libro)
    })


# CUSTOM - Devolver un libro
@app.route('/libros/<string:isbn>/devolver', methods=['POST'])
def devolver_libro(isbn):
    """
    Marca un libro como devuelto (disponible)
    """
    libro = buscar_libro_por_isbn(isbn)
    
    if libro is None:
        return jsonify({"error": "Libro no encontrado"}), 404
    
    if libro.is_available:
        return jsonify({"error": "El libro ya está disponible"}), 400
    
    libro.return_book()
    
    return jsonify({
        "mensaje": "Libro devuelto exitosamente",
        "libro": libro_to_dict(libro)
    })


# EXTRA - Filtrar libros disponibles
@app.route('/libros/disponibles', methods=['GET'])
def libros_disponibles():
    """
    Devuelve solo los libros que están disponibles
    """
    disponibles = [libro_to_dict(libro) for libro in libros if libro.is_available]
    return jsonify({
        "total": len(disponibles),
        "libros": disponibles
    })


# Inicializar con datos de ejemplo (opcional)
def inicializar_datos():
    """Crea algunos libros de ejemplo para pruebas"""
    libros_ejemplo = [
        Libro("Cien Años de Soledad", "978-0-307-47472-3", "Gabriel García Márquez", 1967, 417, True),
        Libro("Don Quijote de la Mancha", "978-0-06-093434-7", "Miguel de Cervantes", 1605, 863, True),
        Libro("El Principito", "978-0-15-601219-1", "Antoine de Saint-Exupéry", 1943, 96, False),
    ]
    libros.extend(libros_ejemplo)


# Punto de entrada de la aplicación
if __name__ == '__main__':
    # Inicializar con datos de ejemplo
    inicializar_datos()
    
    print("\n" + "="*60)
    print("🚀 Servidor Flask iniciado")
    print("="*60)
    print("📍 URL: http://localhost:5000")
    print("📚 Endpoints disponibles:")
    print("   - GET    http://localhost:5000/")
    print("   - GET    http://localhost:5000/libros")
    print("   - GET    http://localhost:5000/libros/<isbn>")
    print("   - POST   http://localhost:5000/libros")
    print("   - PUT    http://localhost:5000/libros/<isbn>")
    print("   - DELETE http://localhost:5000/libros/<isbn>")
    print("   - POST   http://localhost:5000/libros/<isbn>/prestar")
    print("   - POST   http://localhost:5000/libros/<isbn>/devolver")
    print("="*60)
    print("💡 Abre tu navegador en: http://localhost:5000/libros")
    print("="*60 + "\n")
    
    # Ejecutar servidor
    # debug=True: Recarga automáticamente cuando hay cambios
    # port=5000: Puerto donde corre la aplicación
    app.run(debug=True, port=5000)

