"""
TEMA 1: CREACIÓN DE CLASES EN PYTHON
=====================================

Una clase es una plantilla o molde que define las características (atributos)
y comportamientos (métodos) que tendrán los objetos creados a partir de ella.

En este ejemplo, crearemos una clase Persona que representa a una persona
con sus características básicas y acciones que puede realizar.
"""


class Persona:
    """
    Clase que representa a una persona con sus atributos básicos.
    
    Esta clase demuestra los conceptos fundamentales:
    - Atributos de instancia: variables que pertenecen a cada objeto individual
    - Métodos de instancia: funciones que operan sobre los datos del objeto
    - El constructor __init__: método especial que se ejecuta al crear un objeto
    - El parámetro self: referencia al objeto actual
    """
    
    # Atributo de clase (compartido por todas las instancias)
    # Este contador llevará el registro de cuántas personas se han creado
    contador_personas = 0
    
    def __init__(self, nombre, edad, identificacion):
        """
        Constructor de la clase Persona.
        
        El método __init__ es un método especial (constructor) que se ejecuta
        automáticamente cuando se crea una nueva instancia de la clase.
        
        Parámetros:
            self: referencia automática al objeto que se está creando
            nombre (str): nombre completo de la persona
            edad (int): edad de la persona en años
            identificacion (str): documento de identificación
        """
        # Atributos de instancia (cada objeto tiene sus propios valores)
        # Se accede a ellos mediante self.nombre_atributo
        self.nombre = nombre
        self.edad = edad
        self.identificacion = identificacion
        
        # Atributo privado (por convención, empieza con _)
        # Indica que no debería accederse directamente desde fuera de la clase
        self._estado = "activo"
        
        # Incrementar el contador de personas cada vez que se crea una instancia
        Persona.contador_personas += 1
    
    def saludar(self):
        """
        Método que hace que la persona salude.
        
        Los métodos son funciones definidas dentro de una clase que describen
        los comportamientos o acciones que puede realizar un objeto.
        
        Returns:
            str: mensaje de saludo personalizado
        """
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."
    
    def cumplir_años(self):
        """
        Método que incrementa la edad de la persona en 1 año.
        
        Este método modifica el estado interno del objeto (su atributo edad).
        """
        self.edad += 1
        print(f"{self.nombre} ahora tiene {self.edad} años. ¡Feliz cumpleaños!")
    
    def es_mayor_de_edad(self):
        """
        Método que determina si la persona es mayor de edad.
        
        Returns:
            bool: True si tiene 18 años o más, False en caso contrario
        """
        return self.edad >= 18
    
    def obtener_informacion(self):
        """
        Método que retorna toda la información de la persona en formato legible.
        
        Returns:
            str: información completa de la persona
        """
        estado_edad = "mayor de edad" if self.es_mayor_de_edad() else "menor de edad"
        return f"""
        --- Información de la Persona ---
        Nombre: {self.nombre}
        Edad: {self.edad} años ({estado_edad})
        Identificación: {self.identificacion}
        Estado: {self._estado}
        """
    
    def actualizar_nombre(self, nuevo_nombre):
        """
        Método setter para actualizar el nombre de la persona.
        
        Parámetros:
            nuevo_nombre (str): el nuevo nombre a asignar
        """
        self.nombre = nuevo_nombre
        print(f"Nombre actualizado correctamente a: {self.nombre}")
    
    @classmethod
    def obtener_total_personas(cls):
        """
        Método de clase que retorna el total de personas creadas.
        
        Los métodos de clase se decoran con @classmethod y reciben 'cls' 
        (la clase) como primer parámetro en lugar de 'self' (la instancia).
        
        Returns:
            int: número total de personas creadas
        """
        return cls.contador_personas
    
    @staticmethod
    def validar_edad(edad):
        """
        Método estático que valida si una edad es válida.
        
        Los métodos estáticos se decoran con @staticmethod y no reciben
        ni 'self' ni 'cls' como primer parámetro. Son como funciones
        regulares pero están organizadas dentro de la clase por conveniencia.
        
        Parámetros:
            edad (int): edad a validar
            
        Returns:
            bool: True si la edad es válida (entre 0 y 120), False en caso contrario
        """
        return 0 <= edad <= 120
    
    def __str__(self):
        """
        Método especial que define la representación en string del objeto.
        
        Se llama automáticamente cuando usamos print() o str() sobre el objeto.
        
        Returns:
            str: representación en texto del objeto
        """
        return f"Persona(nombre='{self.nombre}', edad={self.edad})"
    
    def __repr__(self):
        """
        Método especial que define la representación oficial del objeto.
        
        Se usa principalmente para debugging y debe ser lo más precisa posible.
        
        Returns:
            str: representación técnica del objeto
        """
        return f"Persona(nombre='{self.nombre}', edad={self.edad}, identificacion='{self.identificacion}')"


# ============================================================================
# DEMOSTRACIÓN DE USO
# ============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("DEMOSTRACIÓN: CREACIÓN Y USO DE LA CLASE PERSONA")
    print("=" * 60)
    
    # Crear instancias de la clase Persona
    persona1 = Persona("Juan Pérez", 25, "123456789")
    persona2 = Persona("María García", 17, "987654321")
    
    # Usar métodos de las instancias
    print("\n1. Saludos:")
    print(persona1.saludar())
    print(persona2.saludar())
    
    # Mostrar información completa
    print("\n2. Información completa:")
    print(persona1.obtener_informacion())
    print(persona2.obtener_informacion())
    
    # Cumplir años
    print("\n3. Celebrar cumpleaños:")
    persona1.cumplir_años()
    
    # Actualizar nombre
    print("\n4. Actualizar nombre:")
    persona2.actualizar_nombre("María Fernanda García")
    
    # Usar métodos especiales __str__ y __repr__
    print("\n5. Representaciones del objeto:")
    print(f"str(): {str(persona1)}")
    print(f"repr(): {repr(persona1)}")
    
    # Usar método de clase
    print("\n6. Total de personas creadas:")
    print(f"Se han creado {Persona.obtener_total_personas()} personas")
    
    # Usar método estático
    print("\n7. Validar edades:")
    print(f"¿Es válida la edad 25? {Persona.validar_edad(25)}")
    print(f"¿Es válida la edad 150? {Persona.validar_edad(150)}")
    print(f"¿Es válida la edad -5? {Persona.validar_edad(-5)}")

