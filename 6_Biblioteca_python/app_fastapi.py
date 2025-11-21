"""
Aplicación Backend con FastAPI
Sistema de Biblioteca - CRUD completo

Este archivo implementa una API REST usando FastAPI para gestionar libros.
FastAPI incluye validación automática y documentación interactiva.
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import List, Optional
from Libro import Libro

# Crear instancia de FastAPI
app = FastAPI(
    title="API de Biblioteca",
    description="Sistema de gestión de libros con operaciones CRUD completas",
    version="1.0.0"
)

# Base de datos en memoria (lista de libros)
libros = []


# ==================== MODELOS PYDANTIC ====================
# Pydantic valida automáticamente los datos de entrada

class LibroInput(BaseModel):
    """Modelo para crear o actualizar un libro"""
    titulo: str = Field(..., min_length=1, description="Título del libro")
    isbn: str = Field(..., min_length=10, description="Código ISBN único")
    autor: str = Field(..., min_length=1, description="Nombre del autor")
    anio: int = Field(..., ge=1000, le=2100, description="Año de publicación")
    paginas: int = Field(..., gt=0, description="Número de páginas")
    disponible: bool = Field(True, description="Estado de disponibilidad")
    
    class Config:
        schema_extra = {
            "example": {
                "titulo": "Cien Años de Soledad",
                "isbn": "978-0-307-47472-3",
                "autor": "Gabriel García Márquez",
                "anio": 1967,
                "paginas": 417,
                "disponible": True
            }
        }


class LibroOutput(BaseModel):
    """Modelo para devolver información de un libro"""
    isbn: str
    titulo: str
    autor: str
    anio: int
    paginas: int
    disponible: bool


class LibroUpdateInput(BaseModel):
    """Modelo para actualizaciones parciales (todos los campos opcionales)"""
    titulo: Optional[str] = None
    autor: Optional[str] = None
    anio: Optional[int] = Field(None, ge=1000, le=2100)
    paginas: Optional[int] = Field(None, gt=0)
    disponible: Optional[bool] = None


# ==================== FUNCIONES AUXILIARES ====================

def libro_to_dict(libro: Libro) -> dict:
    """Convierte un objeto Libro a diccionario"""
    return {
        "isbn": libro.isbn,
        "titulo": libro.title,
        "autor": libro.author,
        "anio": libro.publication_year,
        "paginas": libro.total_num_pages,
        "disponible": libro.is_available
    }


def buscar_libro_por_isbn(isbn: str) -> Optional[Libro]:
    """Busca un libro por ISBN, retorna None si no existe"""
    for libro in libros:
        if libro.isbn == isbn:
            return libro
    return None


# ==================== ENDPOINTS ====================

@app.get("/", tags=["Root"])
async def root():
    """
    Endpoint principal con información de la API
    """
    return {
        "mensaje": "API de Biblioteca - Sistema de Gestión de Libros",
        "version": "1.0.0",
        "documentacion": "/docs",
        "documentacion_alternativa": "/redoc",
        "endpoints": {
            "GET /libros": "Obtener todos los libros",
            "GET /libros/{isbn}": "Obtener un libro específico",
            "POST /libros": "Crear un nuevo libro",
            "PUT /libros/{isbn}": "Actualizar un libro existente",
            "PATCH /libros/{isbn}": "Actualización parcial de un libro",
            "DELETE /libros/{isbn}": "Eliminar un libro",
            "POST /libros/{isbn}/prestar": "Prestar un libro",
            "POST /libros/{isbn}/devolver": "Devolver un libro"
        }
    }


@app.get("/libros", response_model=List[LibroOutput], tags=["Libros"])
async def obtener_libros():
    """
    Obtiene la lista completa de libros
    
    Returns:
        Lista de todos los libros en la biblioteca
    """
    lista_libros = [libro_to_dict(libro) for libro in libros]
    return lista_libros


@app.get("/libros/{isbn}", response_model=LibroOutput, tags=["Libros"])
async def obtener_libro(isbn: str):
    """
    Obtiene un libro específico por su ISBN
    
    Args:
        isbn: Código ISBN del libro
        
    Returns:
        Información del libro solicitado
        
    Raises:
        HTTPException: 404 si el libro no existe
    """
    libro = buscar_libro_por_isbn(isbn)
    
    if libro is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Libro con ISBN {isbn} no encontrado"
        )
    
    return libro_to_dict(libro)


@app.post("/libros", response_model=LibroOutput, status_code=status.HTTP_201_CREATED, tags=["Libros"])
async def crear_libro(libro_input: LibroInput):
    """
    Crea un nuevo libro en la biblioteca
    
    Args:
        libro_input: Datos del libro a crear
        
    Returns:
        El libro creado
        
    Raises:
        HTTPException: 400 si el ISBN ya existe
    """
    # Verificar que el ISBN no exista
    if buscar_libro_por_isbn(libro_input.isbn):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ya existe un libro con ese ISBN"
        )
    
    # Crear instancia de Libro
    nuevo_libro = Libro(
        title=libro_input.titulo,
        isbn=libro_input.isbn,
        author=libro_input.autor,
        year=libro_input.anio,
        num_pages=libro_input.paginas,
        available=libro_input.disponible
    )
    
    # Agregar a la lista
    libros.append(nuevo_libro)
    
    return libro_to_dict(nuevo_libro)


@app.put("/libros/{isbn}", response_model=LibroOutput, tags=["Libros"])
async def actualizar_libro_completo(isbn: str, libro_input: LibroInput):
    """
    Actualiza completamente un libro existente
    
    Args:
        isbn: ISBN del libro a actualizar
        libro_input: Nuevos datos del libro
        
    Returns:
        El libro actualizado
        
    Raises:
        HTTPException: 404 si el libro no existe
    """
    libro = buscar_libro_por_isbn(isbn)
    
    if libro is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Libro con ISBN {isbn} no encontrado"
        )
    
    # Actualizar todos los campos
    libro.title = libro_input.titulo
    libro.author = libro_input.autor
    libro.publication_year = libro_input.anio
    libro.total_num_pages = libro_input.paginas
    libro.is_available = libro_input.disponible
    
    return libro_to_dict(libro)


@app.patch("/libros/{isbn}", response_model=LibroOutput, tags=["Libros"])
async def actualizar_libro_parcial(isbn: str, libro_update: LibroUpdateInput):
    """
    Actualiza parcialmente un libro existente (solo campos especificados)
    
    Args:
        isbn: ISBN del libro a actualizar
        libro_update: Campos a actualizar
        
    Returns:
        El libro actualizado
        
    Raises:
        HTTPException: 404 si el libro no existe
    """
    libro = buscar_libro_por_isbn(isbn)
    
    if libro is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Libro con ISBN {isbn} no encontrado"
        )
    
    # Actualizar solo los campos que no sean None
    if libro_update.titulo is not None:
        libro.title = libro_update.titulo
    if libro_update.autor is not None:
        libro.author = libro_update.autor
    if libro_update.anio is not None:
        libro.publication_year = libro_update.anio
    if libro_update.paginas is not None:
        libro.total_num_pages = libro_update.paginas
    if libro_update.disponible is not None:
        libro.is_available = libro_update.disponible
    
    return libro_to_dict(libro)


@app.delete("/libros/{isbn}", status_code=status.HTTP_200_OK, tags=["Libros"])
async def eliminar_libro(isbn: str):
    """
    Elimina un libro de la biblioteca
    
    Args:
        isbn: ISBN del libro a eliminar
        
    Returns:
        Mensaje de confirmación
        
    Raises:
        HTTPException: 404 si el libro no existe
    """
    libro = buscar_libro_por_isbn(isbn)
    
    if libro is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Libro con ISBN {isbn} no encontrado"
        )
    
    libros.remove(libro)
    
    return {
        "mensaje": "Libro eliminado exitosamente",
        "isbn": isbn
    }


@app.post("/libros/{isbn}/prestar", response_model=LibroOutput, tags=["Operaciones"])
async def prestar_libro(isbn: str):
    """
    Marca un libro como prestado
    
    Args:
        isbn: ISBN del libro a prestar
        
    Returns:
        El libro actualizado
        
    Raises:
        HTTPException: 404 si el libro no existe, 400 si ya está prestado
    """
    libro = buscar_libro_por_isbn(isbn)
    
    if libro is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Libro con ISBN {isbn} no encontrado"
        )
    
    if not libro.is_available:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El libro ya está prestado"
        )
    
    libro.loan()
    
    return libro_to_dict(libro)


@app.post("/libros/{isbn}/devolver", response_model=LibroOutput, tags=["Operaciones"])
async def devolver_libro(isbn: str):
    """
    Marca un libro como devuelto
    
    Args:
        isbn: ISBN del libro a devolver
        
    Returns:
        El libro actualizado
        
    Raises:
        HTTPException: 404 si el libro no existe, 400 si ya está disponible
    """
    libro = buscar_libro_por_isbn(isbn)
    
    if libro is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Libro con ISBN {isbn} no encontrado"
        )
    
    if libro.is_available:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El libro ya está disponible"
        )
    
    libro.return_book()
    
    return libro_to_dict(libro)


@app.get("/libros/filtro/disponibles", response_model=List[LibroOutput], tags=["Filtros"])
async def obtener_libros_disponibles():
    """
    Obtiene solo los libros que están disponibles
    
    Returns:
        Lista de libros disponibles
    """
    disponibles = [libro_to_dict(libro) for libro in libros if libro.is_available]
    return disponibles


@app.get("/libros/filtro/prestados", response_model=List[LibroOutput], tags=["Filtros"])
async def obtener_libros_prestados():
    """
    Obtiene solo los libros que están prestados
    
    Returns:
        Lista de libros prestados
    """
    prestados = [libro_to_dict(libro) for libro in libros if not libro.is_available]
    return prestados


# ==================== INICIALIZACIÓN ====================

@app.on_event("startup")
async def startup_event():
    """
    Se ejecuta al iniciar la aplicación
    Carga datos de ejemplo
    """
    libros_ejemplo = [
        Libro("Cien Años de Soledad", "978-0-307-47472-3", "Gabriel García Márquez", 1967, 417, True),
        Libro("Don Quijote de la Mancha", "978-0-06-093434-7", "Miguel de Cervantes", 1605, 863, True),
        Libro("El Principito", "978-0-15-601219-1", "Antoine de Saint-Exupéry", 1943, 96, False),
        Libro("1984", "978-0-452-28423-4", "George Orwell", 1949, 328, True),
    ]
    libros.extend(libros_ejemplo)
    
    print("\n" + "="*60)
    print("🚀 Servidor FastAPI iniciado")
    print("="*60)
    print("📍 URL: http://localhost:8000")
    print("📚 Documentación interactiva:")
    print("   - Swagger UI: http://localhost:8000/docs")
    print("   - ReDoc:      http://localhost:8000/redoc")
    print("="*60)
    print("💡 Prueba en tu navegador:")
    print("   - http://localhost:8000/libros")
    print("   - http://localhost:8000/docs (interfaz interactiva)")
    print("="*60 + "\n")


# Para ejecutar:
# uvicorn app_fastapi:app --reload

