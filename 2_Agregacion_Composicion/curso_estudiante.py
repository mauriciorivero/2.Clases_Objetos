"""
TEMA 2: AGREGACIÓN Y COMPOSICIÓN
=================================

En POO, la agregación y composición son formas de establecer relaciones entre clases:

AGREGACIÓN:
- Es una relación "tiene-un" donde el objeto contenido puede existir independientemente
- Ejemplo: Un Curso tiene Estudiantes, pero los estudiantes pueden existir sin el curso
- Es una relación más débil

COMPOSICIÓN:
- Es una relación "tiene-un" más fuerte donde el objeto contenido no puede existir sin el contenedor
- Ejemplo: Un Curso tiene Módulos, si el curso se elimina, los módulos también
- Es una relación de dependencia fuerte

Este ejemplo demuestra ambos conceptos usando el contexto educativo.
"""


class Estudiante:
    """
    Clase que representa a un estudiante.
    
    Esta clase puede existir independientemente de un curso,
    lo que la hace apropiada para una relación de AGREGACIÓN.
    """
    
    def __init__(self, nombre, codigo, correo):
        """
        Constructor de la clase Estudiante.
        
        Parámetros:
            nombre (str): nombre completo del estudiante
            codigo (str): código único del estudiante
            correo (str): correo electrónico del estudiante
        """
        self.nombre = nombre
        self.codigo = codigo
        self.correo = correo
        self.cursos_inscritos = []  # Lista de cursos en los que está inscrito
        self.notas = {}  # Diccionario {nombre_curso: nota}
    
    def inscribir_curso(self, nombre_curso):
        """
        Inscribe al estudiante en un curso.
        
        Parámetros:
            nombre_curso (str): nombre del curso a inscribir
        """
        if nombre_curso not in self.cursos_inscritos:
            self.cursos_inscritos.append(nombre_curso)
            print(f"{self.nombre} se ha inscrito en el curso: {nombre_curso}")
        else:
            print(f"{self.nombre} ya está inscrito en: {nombre_curso}")
    
    def asignar_nota(self, nombre_curso, nota):
        """
        Asigna una nota al estudiante en un curso específico.
        
        Parámetros:
            nombre_curso (str): nombre del curso
            nota (float): calificación del estudiante (0-5)
        """
        if 0 <= nota <= 5:
            self.notas[nombre_curso] = nota
            print(f"Nota {nota} asignada a {self.nombre} en {nombre_curso}")
        else:
            print("Error: La nota debe estar entre 0 y 5")
    
    def obtener_promedio(self):
        """
        Calcula el promedio de todas las notas del estudiante.
        
        Returns:
            float: promedio de notas, o 0 si no tiene notas
        """
        if not self.notas:
            return 0
        return sum(self.notas.values()) / len(self.notas)
    
    def __str__(self):
        """Representación en string del estudiante."""
        return f"Estudiante: {self.nombre} (Código: {self.codigo})"
    
    def obtener_info(self):
        """Retorna información detallada del estudiante."""
        info = f"\n--- Estudiante: {self.nombre} ---\n"
        info += f"Código: {self.codigo}\n"
        info += f"Correo: {self.correo}\n"
        info += f"Cursos inscritos: {len(self.cursos_inscritos)}\n"
        if self.notas:
            info += "Notas:\n"
            for curso, nota in self.notas.items():
                info += f"  - {curso}: {nota}\n"
            info += f"Promedio: {self.obtener_promedio():.2f}\n"
        return info


class Modulo:
    """
    Clase que representa un módulo dentro de un curso.
    
    Esta clase está en una relación de COMPOSICIÓN con Curso,
    ya que un módulo no tiene sentido sin un curso que lo contenga.
    """
    
    def __init__(self, numero, nombre, duracion_horas, contenido):
        """
        Constructor de la clase Modulo.
        
        Parámetros:
            numero (int): número del módulo en el curso
            nombre (str): nombre del módulo
            duracion_horas (int): duración en horas del módulo
            contenido (list): lista de temas que cubre el módulo
        """
        self.numero = numero
        self.nombre = nombre
        self.duracion_horas = duracion_horas
        self.contenido = contenido  # Lista de temas
    
    def __str__(self):
        """Representación en string del módulo."""
        return f"Módulo {self.numero}: {self.nombre} ({self.duracion_horas}h)"
    
    def obtener_detalle(self):
        """Retorna información detallada del módulo."""
        detalle = f"\n{str(self)}\n"
        detalle += "Contenido:\n"
        for i, tema in enumerate(self.contenido, 1):
            detalle += f"  {i}. {tema}\n"
        return detalle


class Curso:
    """
    Clase que representa un curso académico.
    
    Demuestra dos tipos de relaciones:
    1. AGREGACIÓN con Estudiante: tiene estudiantes pero no los "posee"
    2. COMPOSICIÓN con Modulo: contiene módulos que dependen de él
    """
    
    def __init__(self, nombre, codigo, profesor, duracion_semanas):
        """
        Constructor de la clase Curso.
        
        Parámetros:
            nombre (str): nombre del curso
            codigo (str): código único del curso
            profesor (str): nombre del profesor que dicta el curso
            duracion_semanas (int): duración del curso en semanas
        """
        self.nombre = nombre
        self.codigo = codigo
        self.profesor = profesor
        self.duracion_semanas = duracion_semanas
        
        # AGREGACIÓN: lista de estudiantes (objetos externos que existen independientemente)
        self.estudiantes = []
        
        # COMPOSICIÓN: lista de módulos (objetos internos que solo existen dentro del curso)
        # Los módulos se crean dentro del curso y no tienen vida propia fuera de él
        self.modulos = []
        
        # Estado del curso
        self.estado = "Planificación"  # Planificación, En curso, Finalizado
    
    def agregar_modulo(self, numero, nombre, duracion_horas, contenido):
        """
        Crea y agrega un módulo al curso (COMPOSICIÓN).
        
        El módulo se crea dentro del curso y es parte integral de él.
        Si el curso se elimina, sus módulos también desaparecen.
        
        Parámetros:
            numero (int): número del módulo
            nombre (str): nombre del módulo
            duracion_horas (int): duración en horas
            contenido (list): lista de temas
        """
        modulo = Modulo(numero, nombre, duracion_horas, contenido)
        self.modulos.append(modulo)
        print(f"Módulo '{nombre}' agregado al curso {self.nombre}")
    
    def inscribir_estudiante(self, estudiante):
        """
        Inscribe un estudiante en el curso (AGREGACIÓN).
        
        El estudiante es un objeto que existe independientemente del curso.
        Simplemente se establece una relación entre ambos.
        
        Parámetros:
            estudiante (Estudiante): objeto estudiante a inscribir
        """
        if estudiante not in self.estudiantes:
            self.estudiantes.append(estudiante)
            estudiante.inscribir_curso(self.nombre)
            print(f"Estudiante {estudiante.nombre} inscrito en {self.nombre}")
        else:
            print(f"El estudiante {estudiante.nombre} ya está inscrito")
    
    def dar_de_baja_estudiante(self, estudiante):
        """
        Da de baja a un estudiante del curso.
        
        Nota: El estudiante sigue existiendo después de ser dado de baja,
        demostrando la naturaleza de la AGREGACIÓN.
        
        Parámetros:
            estudiante (Estudiante): estudiante a dar de baja
        """
        if estudiante in self.estudiantes:
            self.estudiantes.remove(estudiante)
            print(f"Estudiante {estudiante.nombre} dado de baja de {self.nombre}")
        else:
            print(f"El estudiante {estudiante.nombre} no está inscrito")
    
    def obtener_total_horas(self):
        """
        Calcula el total de horas del curso sumando todos los módulos.
        
        Returns:
            int: total de horas del curso
        """
        return sum(modulo.duracion_horas for modulo in self.modulos)
    
    def listar_estudiantes(self):
        """Muestra la lista de estudiantes inscritos."""
        print(f"\n--- Estudiantes inscritos en {self.nombre} ---")
        if not self.estudiantes:
            print("No hay estudiantes inscritos")
        else:
            for i, estudiante in enumerate(self.estudiantes, 1):
                print(f"{i}. {estudiante}")
    
    def listar_modulos(self):
        """Muestra la lista de módulos del curso."""
        print(f"\n--- Módulos de {self.nombre} ---")
        if not self.modulos:
            print("No hay módulos definidos")
        else:
            for modulo in self.modulos:
                print(modulo.obtener_detalle())
    
    def iniciar_curso(self):
        """Cambia el estado del curso a 'En curso'."""
        if self.estado == "Planificación":
            self.estado = "En curso"
            print(f"¡El curso {self.nombre} ha iniciado!")
        else:
            print(f"El curso ya está en estado: {self.estado}")
    
    def finalizar_curso(self):
        """Cambia el estado del curso a 'Finalizado'."""
        if self.estado == "En curso":
            self.estado = "Finalizado"
            print(f"El curso {self.nombre} ha finalizado")
        else:
            print("El curso debe estar 'En curso' para finalizarlo")
    
    def obtener_resumen(self):
        """Retorna un resumen completo del curso."""
        resumen = f"\n{'='*60}\n"
        resumen += f"CURSO: {self.nombre}\n"
        resumen += f"{'='*60}\n"
        resumen += f"Código: {self.codigo}\n"
        resumen += f"Profesor: {self.profesor}\n"
        resumen += f"Duración: {self.duracion_semanas} semanas\n"
        resumen += f"Total de horas: {self.obtener_total_horas()} horas\n"
        resumen += f"Estado: {self.estado}\n"
        resumen += f"Módulos: {len(self.modulos)}\n"
        resumen += f"Estudiantes inscritos: {len(self.estudiantes)}\n"
        return resumen
    
    def __str__(self):
        """Representación en string del curso."""
        return f"Curso: {self.nombre} (Código: {self.codigo})"


# ============================================================================
# DEMOSTRACIÓN DE USO
# ============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("DEMOSTRACIÓN: AGREGACIÓN Y COMPOSICIÓN")
    print("=" * 70)
    
    # ========== CREAR ESTUDIANTES (objetos independientes) ==========
    print("\n1. CREANDO ESTUDIANTES (objetos independientes):")
    print("-" * 70)
    estudiante1 = Estudiante("Carlos Rodríguez", "EST001", "carlos@email.com")
    estudiante2 = Estudiante("Ana Martínez", "EST002", "ana@email.com")
    estudiante3 = Estudiante("Luis Torres", "EST003", "luis@email.com")
    print(f"Creados: {estudiante1}")
    print(f"Creados: {estudiante2}")
    print(f"Creados: {estudiante3}")
    
    # ========== CREAR CURSO ==========
    print("\n2. CREANDO CURSO:")
    print("-" * 70)
    curso_python = Curso(
        nombre="Python Orientado a Objetos",
        codigo="PROG301",
        profesor="Dr. Roberto Gómez",
        duracion_semanas=12
    )
    print(curso_python)
    
    # ========== COMPOSICIÓN: Agregar módulos al curso ==========
    print("\n3. COMPOSICIÓN - Agregando módulos al curso:")
    print("-" * 70)
    print("Los módulos son parte integral del curso (composición)")
    
    curso_python.agregar_modulo(
        numero=1,
        nombre="Introducción a POO",
        duracion_horas=20,
        contenido=[
            "¿Qué es la POO?",
            "Clases y objetos",
            "Atributos y métodos",
            "Encapsulamiento"
        ]
    )
    
    curso_python.agregar_modulo(
        numero=2,
        nombre="Herencia y Polimorfismo",
        duracion_horas=25,
        contenido=[
            "Concepto de herencia",
            "Herencia simple y múltiple",
            "Polimorfismo",
            "Métodos abstractos"
        ]
    )
    
    curso_python.agregar_modulo(
        numero=3,
        nombre="Patrones de diseño",
        duracion_horas=30,
        contenido=[
            "Singleton",
            "Factory",
            "Observer",
            "Strategy"
        ]
    )
    
    # ========== AGREGACIÓN: Inscribir estudiantes ==========
    print("\n4. AGREGACIÓN - Inscribiendo estudiantes al curso:")
    print("-" * 70)
    print("Los estudiantes existen independientemente del curso (agregación)")
    
    curso_python.inscribir_estudiante(estudiante1)
    curso_python.inscribir_estudiante(estudiante2)
    curso_python.inscribir_estudiante(estudiante3)
    
    # ========== MOSTRAR INFORMACIÓN DEL CURSO ==========
    print("\n5. RESUMEN DEL CURSO:")
    print(curso_python.obtener_resumen())
    
    curso_python.listar_modulos()
    curso_python.listar_estudiantes()
    
    # ========== INICIAR CURSO Y ASIGNAR NOTAS ==========
    print("\n6. INICIANDO CURSO Y ASIGNANDO NOTAS:")
    print("-" * 70)
    curso_python.iniciar_curso()
    
    estudiante1.asignar_nota("Python Orientado a Objetos", 4.5)
    estudiante2.asignar_nota("Python Orientado a Objetos", 4.8)
    estudiante3.asignar_nota("Python Orientado a Objetos", 4.2)
    
    # ========== DAR DE BAJA A UN ESTUDIANTE ==========
    print("\n7. DEMOSTRANDO AGREGACIÓN - Dar de baja a un estudiante:")
    print("-" * 70)
    print("El estudiante existe antes y después de estar en el curso")
    print(f"\nInformación de {estudiante3.nombre} ANTES de la baja:")
    print(estudiante3.obtener_info())
    
    curso_python.dar_de_baja_estudiante(estudiante3)
    
    print(f"\nInformación de {estudiante3.nombre} DESPUÉS de la baja:")
    print(estudiante3.obtener_info())
    print("→ El estudiante sigue existiendo con toda su información")
    
    # ========== FINALIZAR CURSO ==========
    print("\n8. FINALIZANDO CURSO:")
    print("-" * 70)
    curso_python.finalizar_curso()
    print(curso_python.obtener_resumen())
    
    # ========== DEMOSTRAR DIFERENCIA ENTRE AGREGACIÓN Y COMPOSICIÓN ==========
    print("\n9. RESUMEN - DIFERENCIA ENTRE AGREGACIÓN Y COMPOSICIÓN:")
    print("=" * 70)
    print("""
    COMPOSICIÓN (Módulos):
    ✓ Los módulos son PARTE del curso
    ✓ Si el curso se elimina, los módulos también se eliminan
    ✓ Los módulos no tienen sentido fuera del curso
    ✓ Relación fuerte: "El curso está COMPUESTO de módulos"
    
    AGREGACIÓN (Estudiantes):
    ✓ Los estudiantes son INDEPENDIENTES del curso
    ✓ Si el curso se elimina, los estudiantes siguen existiendo
    ✓ Los estudiantes pueden estar en múltiples cursos
    ✓ Relación débil: "El curso TIENE estudiantes"
    """)

