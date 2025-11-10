"""
TEMA 3: INSTANCIACIÓN DE CLASES
================================

La INSTANCIACIÓN es el proceso de crear un objeto concreto a partir de una clase.
- La CLASE es el molde o plantilla
- La INSTANCIA u OBJETO es el elemento concreto creado a partir del molde

Este módulo demuestra diferentes formas de instanciar clases en Python,
incluyendo las clases de los ejemplos anteriores.
"""

# Importar las clases de los ejercicios anteriores
import sys
import os

# Agregar las rutas de los módulos anteriores
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '1_Creacion_Clases'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '2_Agregacion_Composicion'))

from persona import Persona
from curso_estudiante import Estudiante, Curso


"""
CONCEPTOS CLAVE SOBRE INSTANCIACIÓN:
=====================================

1. SINTAXIS BÁSICA:
   objeto = NombreClase(argumentos)
   
2. PROCESO INTERNO:
   a) Python crea un nuevo objeto en memoria
   b) Se llama automáticamente al método __init__()
   c) Se retorna la referencia al objeto creado
   
3. CADA INSTANCIA ES ÚNICA:
   - Tiene su propio espacio en memoria
   - Tiene sus propios valores de atributos
   - Puede modificarse independientemente de otras instancias
"""


def demostrar_instanciacion_basica():
    """
    Demuestra la instanciación básica de objetos.
    """
    print("=" * 70)
    print("1. INSTANCIACIÓN BÁSICA - Creando objetos de la clase Persona")
    print("=" * 70)
    
    # FORMA 1: Instanciación directa con argumentos posicionales
    print("\n--- Forma 1: Argumentos posicionales ---")
    persona1 = Persona("Diego Álvarez", 30, "456789123")
    print(f"Objeto creado: {persona1}")
    print(f"Dirección en memoria: {id(persona1)}")
    print(f"Tipo: {type(persona1)}")
    
    # FORMA 2: Instanciación con argumentos nombrados (keyword arguments)
    print("\n--- Forma 2: Argumentos nombrados ---")
    persona2 = Persona(
        nombre="Laura Jiménez",
        edad=28,
        identificacion="789456123"
    )
    print(f"Objeto creado: {persona2}")
    print(f"Dirección en memoria: {id(persona2)}")
    
    # FORMA 3: Instanciación con mezcla de argumentos
    print("\n--- Forma 3: Mezcla de argumentos ---")
    persona3 = Persona("Roberto Silva", edad=35, identificacion="321654987")
    print(f"Objeto creado: {persona3}")
    
    # Demostrar que cada instancia es única
    print("\n--- Verificando que cada instancia es única ---")
    print(f"¿persona1 es persona2? {persona1 is persona2}")
    print(f"¿persona1 es persona3? {persona1 is persona3}")
    print(f"¿Todas son instancias de Persona? {isinstance(persona1, Persona) and isinstance(persona2, Persona)}")
    
    return persona1, persona2, persona3


def demostrar_instanciacion_multiple():
    """
    Demuestra la creación de múltiples instancias y su independencia.
    """
    print("\n" + "=" * 70)
    print("2. INSTANCIACIÓN MÚLTIPLE - Independencia entre objetos")
    print("=" * 70)
    
    # Crear múltiples estudiantes
    print("\n--- Creando múltiples estudiantes ---")
    estudiantes = []
    
    datos_estudiantes = [
        ("Pedro Ramírez", "EST101", "pedro@email.com"),
        ("Sofía López", "EST102", "sofia@email.com"),
        ("Miguel Ángel Castro", "EST103", "miguel@email.com"),
        ("Valentina Ruiz", "EST104", "valentina@email.com"),
        ("Andrés Moreno", "EST105", "andres@email.com")
    ]
    
    # Instanciar estudiantes en un bucle
    for nombre, codigo, correo in datos_estudiantes:
        estudiante = Estudiante(nombre, codigo, correo)
        estudiantes.append(estudiante)
        print(f"✓ Estudiante creado: {estudiante}")
    
    # Demostrar independencia: modificar un objeto no afecta a los demás
    print("\n--- Demostrando independencia entre instancias ---")
    print("Asignando notas diferentes a cada estudiante:")
    
    estudiantes[0].asignar_nota("Matemáticas", 4.5)
    estudiantes[1].asignar_nota("Matemáticas", 3.8)
    estudiantes[2].asignar_nota("Matemáticas", 4.9)
    
    print("\nVerificando que las notas son independientes:")
    for est in estudiantes[:3]:
        print(f"{est.nombre}: Notas = {est.notas}")
    
    return estudiantes


def demostrar_instanciacion_con_valores_por_defecto():
    """
    Demuestra la instanciación usando valores por defecto.
    """
    print("\n" + "=" * 70)
    print("3. INSTANCIACIÓN CON VALORES POR DEFECTO")
    print("=" * 70)
    
    # Definir una clase con parámetros opcionales
    class Producto:
        """Clase con parámetros con valores por defecto."""
        
        def __init__(self, nombre, precio, cantidad=1, categoria="General"):
            """
            Constructor con parámetros opcionales.
            
            Parámetros:
                nombre (str): nombre del producto (obligatorio)
                precio (float): precio del producto (obligatorio)
                cantidad (int): cantidad en stock (opcional, default=1)
                categoria (str): categoría del producto (opcional, default="General")
            """
            self.nombre = nombre
            self.precio = precio
            self.cantidad = cantidad
            self.categoria = categoria
        
        def __str__(self):
            return f"{self.nombre} - ${self.precio} (Stock: {self.cantidad}) [{self.categoria}]"
    
    # Instanciación solo con parámetros obligatorios
    print("\n--- Solo parámetros obligatorios (usa valores por defecto) ---")
    producto1 = Producto("Laptop", 1200.00)
    print(f"Producto 1: {producto1}")
    
    # Instanciación con algunos parámetros opcionales
    print("\n--- Especificando cantidad ---")
    producto2 = Producto("Mouse", 25.00, cantidad=50)
    print(f"Producto 2: {producto2}")
    
    # Instanciación con todos los parámetros
    print("\n--- Especificando todos los parámetros ---")
    producto3 = Producto("Teclado", 75.00, cantidad=30, categoria="Periféricos")
    print(f"Producto 3: {producto3}")
    
    # Usando argumentos nombrados en cualquier orden
    print("\n--- Argumentos nombrados en diferente orden ---")
    producto4 = Producto(categoria="Electrónica", nombre="Monitor", cantidad=15, precio=300.00)
    print(f"Producto 4: {producto4}")


def demostrar_instanciacion_dinamica():
    """
    Demuestra la creación dinámica de instancias basada en datos externos.
    """
    print("\n" + "=" * 70)
    print("4. INSTANCIACIÓN DINÁMICA")
    print("=" * 70)
    
    print("\n--- Creando objetos dinámicamente desde un diccionario ---")
    
    # Datos que podrían venir de una base de datos, API o archivo
    datos_personas = [
        {"nombre": "Alberto Sánchez", "edad": 45, "identificacion": "111222333"},
        {"nombre": "Beatriz Ramos", "edad": 32, "identificacion": "444555666"},
        {"nombre": "Carlos Vega", "edad": 27, "identificacion": "777888999"},
    ]
    
    # Crear instancias dinámicamente usando desempaquetado de diccionarios
    personas = []
    for datos in datos_personas:
        # El operador ** desempaqueta el diccionario como argumentos nombrados
        persona = Persona(**datos)
        personas.append(persona)
        print(f"✓ Creado: {persona}")
    
    # Demostrar el uso de los objetos creados
    print("\n--- Usando los objetos creados dinámicamente ---")
    for persona in personas:
        print(persona.saludar())
    
    return personas


def demostrar_instanciacion_compleja():
    """
    Demuestra la instanciación de objetos complejos que contienen otros objetos.
    """
    print("\n" + "=" * 70)
    print("5. INSTANCIACIÓN COMPLEJA - Objetos que contienen otros objetos")
    print("=" * 70)
    
    # Paso 1: Crear instancias de estudiantes
    print("\n--- Paso 1: Creando estudiantes ---")
    est1 = Estudiante("Gabriela Mendoza", "EST201", "gabriela@email.com")
    est2 = Estudiante("Fernando Ortiz", "EST202", "fernando@email.com")
    est3 = Estudiante("Isabella Cruz", "EST203", "isabella@email.com")
    print(f"✓ {est1}")
    print(f"✓ {est2}")
    print(f"✓ {est3}")
    
    # Paso 2: Crear instancia de curso
    print("\n--- Paso 2: Creando curso ---")
    curso = Curso(
        nombre="Desarrollo Web con Django",
        codigo="WEB401",
        profesor="Ing. Patricia Herrera",
        duracion_semanas=16
    )
    print(f"✓ {curso}")
    
    # Paso 3: Agregar módulos al curso (composición)
    print("\n--- Paso 3: Agregando módulos (composición) ---")
    curso.agregar_modulo(
        numero=1,
        nombre="Fundamentos de Django",
        duracion_horas=25,
        contenido=["MVT", "URLs", "Vistas", "Templates"]
    )
    curso.agregar_modulo(
        numero=2,
        nombre="Base de datos y ORM",
        duracion_horas=30,
        contenido=["Modelos", "Migraciones", "Queries", "Admin"]
    )
    
    # Paso 4: Inscribir estudiantes (agregación)
    print("\n--- Paso 4: Inscribiendo estudiantes (agregación) ---")
    curso.inscribir_estudiante(est1)
    curso.inscribir_estudiante(est2)
    curso.inscribir_estudiante(est3)
    
    # Mostrar el resultado
    print("\n--- Resultado: Objeto complejo creado ---")
    print(curso.obtener_resumen())
    
    return curso


def demostrar_metodos_alternativos_instanciacion():
    """
    Demuestra métodos alternativos de instanciación (factory methods).
    """
    print("\n" + "=" * 70)
    print("6. MÉTODOS ALTERNATIVOS DE INSTANCIACIÓN (Factory Methods)")
    print("=" * 70)
    
    class Fecha:
        """
        Clase que demuestra diferentes formas de crear instancias
        usando métodos de clase (factory methods).
        """
        
        def __init__(self, dia, mes, año):
            """Constructor estándar."""
            self.dia = dia
            self.mes = mes
            self.año = año
        
        @classmethod
        def desde_string(cls, fecha_string):
            """
            Factory method: crea una instancia desde un string.
            
            Parámetros:
                fecha_string (str): fecha en formato "DD-MM-AAAA"
            
            Returns:
                Fecha: nueva instancia de Fecha
            """
            dia, mes, año = map(int, fecha_string.split('-'))
            return cls(dia, mes, año)  # cls() llama al constructor
        
        @classmethod
        def hoy(cls):
            """
            Factory method: crea una instancia con la fecha actual.
            
            Returns:
                Fecha: nueva instancia con la fecha de hoy
            """
            from datetime import datetime
            hoy = datetime.now()
            return cls(hoy.day, hoy.month, hoy.year)
        
        @classmethod
        def año_nuevo(cls, año):
            """
            Factory method: crea una instancia para el 1 de enero del año dado.
            
            Parámetros:
                año (int): año deseado
            
            Returns:
                Fecha: nueva instancia para el 1 de enero
            """
            return cls(1, 1, año)
        
        def __str__(self):
            return f"{self.dia:02d}/{self.mes:02d}/{self.año}"
    
    # FORMA 1: Constructor tradicional
    print("\n--- Forma 1: Constructor tradicional ---")
    fecha1 = Fecha(15, 11, 2025)
    print(f"Fecha 1: {fecha1}")
    
    # FORMA 2: Factory method - desde string
    print("\n--- Forma 2: Factory method desde string ---")
    fecha2 = Fecha.desde_string("25-12-2025")
    print(f"Fecha 2: {fecha2}")
    
    # FORMA 3: Factory method - fecha actual
    print("\n--- Forma 3: Factory method fecha actual ---")
    fecha3 = Fecha.hoy()
    print(f"Fecha 3 (hoy): {fecha3}")
    
    # FORMA 4: Factory method - año nuevo
    print("\n--- Forma 4: Factory method año nuevo ---")
    fecha4 = Fecha.año_nuevo(2026)
    print(f"Fecha 4: {fecha4}")


def verificar_instancias():
    """
    Demuestra cómo verificar instancias y tipos de objetos.
    """
    print("\n" + "=" * 70)
    print("7. VERIFICACIÓN DE INSTANCIAS")
    print("=" * 70)
    
    # Crear instancias de diferentes clases
    persona = Persona("Test Persona", 25, "123")
    estudiante = Estudiante("Test Estudiante", "EST999", "test@email.com")
    numero = 42
    texto = "Hola mundo"
    
    print("\n--- Verificando tipos con isinstance() ---")
    print(f"persona es instancia de Persona: {isinstance(persona, Persona)}")
    print(f"estudiante es instancia de Estudiante: {isinstance(estudiante, Estudiante)}")
    print(f"numero es instancia de int: {isinstance(numero, int)}")
    print(f"texto es instancia de str: {isinstance(texto, str)}")
    
    print("\n--- Verificando tipos con type() ---")
    print(f"type(persona): {type(persona)}")
    print(f"type(estudiante): {type(estudiante)}")
    print(f"type(numero): {type(numero)}")
    print(f"type(texto): {type(texto)}")
    
    print("\n--- Obteniendo información del objeto ---")
    print(f"ID de persona: {id(persona)}")
    print(f"Nombre de la clase: {persona.__class__.__name__}")
    print(f"Módulo: {persona.__class__.__module__}")


# ============================================================================
# PROGRAMA PRINCIPAL
# ============================================================================

if __name__ == "__main__":
    print("\n")
    print("╔" + "═" * 68 + "╗")
    print("║" + "DEMOSTRACIÓN COMPLETA: INSTANCIACIÓN DE CLASES".center(68) + "║")
    print("╚" + "═" * 68 + "╝")
    
    # Ejecutar todas las demostraciones
    demostrar_instanciacion_basica()
    demostrar_instanciacion_multiple()
    demostrar_instanciacion_con_valores_por_defecto()
    demostrar_instanciacion_dinamica()
    demostrar_instanciacion_compleja()
    demostrar_metodos_alternativos_instanciacion()
    verificar_instancias()
    
    # Resumen final
    print("\n" + "=" * 70)
    print("RESUMEN: CONCEPTOS CLAVE DE INSTANCIACIÓN")
    print("=" * 70)
    print("""
    ✓ INSTANCIACIÓN: Proceso de crear objetos a partir de una clase
    
    ✓ CADA INSTANCIA ES ÚNICA:
      - Tiene su propia dirección de memoria
      - Tiene sus propios valores de atributos
      - Es independiente de otras instancias
    
    ✓ FORMAS DE INSTANCIAR:
      - Constructor tradicional: Clase(argumentos)
      - Argumentos posicionales: Clase(arg1, arg2)
      - Argumentos nombrados: Clase(param1=val1, param2=val2)
      - Desempaquetado de diccionario: Clase(**dict)
      - Factory methods: Clase.metodo_factory()
    
    ✓ VERIFICACIÓN:
      - isinstance(objeto, Clase): verifica si es instancia
      - type(objeto): retorna el tipo del objeto
      - id(objeto): retorna la dirección en memoria
    """)
    
    print("\n" + "=" * 70)
    print("¡Demostración completada!")
    print("=" * 70)

