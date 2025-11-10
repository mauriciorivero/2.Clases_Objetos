"""
TEMA 4: HERENCIA EN PROGRAMACIÓN ORIENTADA A OBJETOS
=====================================================

La HERENCIA es un mecanismo que permite crear nuevas clases basadas en clases existentes.
La nueva clase (subclase o clase hija) hereda atributos y métodos de la clase base 
(superclase o clase padre), pudiendo además agregar nuevos atributos/métodos o 
modificar los heredados.

BENEFICIOS DE LA HERENCIA:
- Reutilización de código
- Organización jerárquica del código
- Facilita el mantenimiento
- Permite el polimorfismo

TERMINOLOGÍA:
- Superclase/Clase padre/Clase base: la clase de la que se hereda
- Subclase/Clase hija/Clase derivada: la clase que hereda
- Override/Sobrescritura: redefinir un método heredado en la subclase

Este ejemplo usa una jerarquía de animales para demostrar la herencia.
"""


class Animal:
    """
    SUPERCLASE BASE: Animal
    
    Esta es la clase padre de la que heredarán otras clases.
    Contiene atributos y métodos comunes a todos los animales.
    """
    
    # Atributo de clase compartido por todos los animales
    reino = "Animalia"
    
    def __init__(self, nombre, edad, peso):
        """
        Constructor de la superclase Animal.
        
        Parámetros:
            nombre (str): nombre del animal
            edad (int): edad en años
            peso (float): peso en kilogramos
        """
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.estado = "vivo"
        print(f"🐾 Animal '{nombre}' creado")
    
    def comer(self, alimento):
        """
        Método común a todos los animales.
        
        Este método puede ser usado por todas las subclases o sobrescrito.
        """
        return f"{self.nombre} está comiendo {alimento}"
    
    def dormir(self):
        """Método común a todos los animales."""
        return f"{self.nombre} está durmiendo 💤"
    
    def hacer_sonido(self):
        """
        Método base que será sobrescrito por las subclases.
        
        Este es un ejemplo de un método que las clases hijas DEBEN implementar
        de forma específica.
        """
        return f"{self.nombre} hace un sonido"
    
    def moverse(self):
        """Método base que será sobrescrito según el tipo de animal."""
        return f"{self.nombre} se está moviendo"
    
    def obtener_info(self):
        """Retorna información básica del animal."""
        return f"""
        --- Información del Animal ---
        Tipo: {self.__class__.__name__}
        Nombre: {self.nombre}
        Edad: {self.edad} años
        Peso: {self.peso} kg
        Reino: {self.reino}
        Estado: {self.estado}
        """
    
    def __str__(self):
        """Representación en string del animal."""
        return f"{self.__class__.__name__}: {self.nombre}"


class Mamifero(Animal):
    """
    SUBCLASE: Mamífero
    
    Esta clase HEREDA de Animal y agrega características específicas de los mamíferos.
    
    HEREDA:
    - Todos los atributos de Animal (nombre, edad, peso, estado)
    - Todos los métodos de Animal (comer, dormir, etc.)
    
    AGREGA:
    - Nuevos atributos específicos de mamíferos
    - Nuevos métodos específicos de mamíferos
    - Sobrescribe métodos cuando es necesario
    """
    
    def __init__(self, nombre, edad, peso, tipo_pelaje, numero_patas=4):
        """
        Constructor de Mamífero.
        
        Usa super() para llamar al constructor de la clase padre (Animal)
        y luego agrega atributos específicos de mamíferos.
        
        Parámetros:
            nombre (str): nombre del mamífero
            edad (int): edad en años
            peso (float): peso en kilogramos
            tipo_pelaje (str): tipo de pelaje (corto, largo, rizado, etc.)
            numero_patas (int): número de patas (default: 4)
        """
        # Llamar al constructor de la clase padre (Animal)
        super().__init__(nombre, edad, peso)
        
        # Agregar atributos específicos de Mamífero
        self.tipo_pelaje = tipo_pelaje
        self.numero_patas = numero_patas
        self.temperatura_corporal = 37.0  # Temperatura promedio en °C
        print(f"  → Es un mamífero con pelaje {tipo_pelaje}")
    
    def amamantar(self):
        """
        Método NUEVO específico de mamíferos.
        
        Este método no existe en la clase padre Animal.
        """
        return f"{self.nombre} está amamantando a sus crías 🍼"
    
    def regular_temperatura(self):
        """Método específico de mamíferos (son endotérmicos)."""
        return f"{self.nombre} mantiene su temperatura corporal en {self.temperatura_corporal}°C"
    
    def moverse(self):
        """
        SOBRESCRITURA (Override) del método moverse() de Animal.
        
        Este método redefine el comportamiento del método padre
        para hacerlo específico a mamíferos.
        """
        if self.numero_patas == 4:
            return f"{self.nombre} camina sobre sus {self.numero_patas} patas"
        elif self.numero_patas == 2:
            return f"{self.nombre} camina erguido sobre {self.numero_patas} patas"
        else:
            return f"{self.nombre} se mueve de forma especial"
    
    def obtener_info(self):
        """
        SOBRESCRITURA que EXTIENDE el método de la clase padre.
        
        Llama al método padre con super() y agrega información adicional.
        """
        info_base = super().obtener_info()
        info_adicional = f"""        Tipo de pelaje: {self.tipo_pelaje}
        Número de patas: {self.numero_patas}
        Temperatura corporal: {self.temperatura_corporal}°C
        """
        return info_base + info_adicional


class Oviparo(Animal):
    """
    SUBCLASE: Ovíparo
    
    Esta clase HEREDA de Animal y agrega características específicas
    de animales que se reproducen por huevos.
    """
    
    def __init__(self, nombre, edad, peso, tipo_huevo, puede_volar=False):
        """
        Constructor de Ovíparo.
        
        Parámetros:
            nombre (str): nombre del animal ovíparo
            edad (int): edad en años
            peso (float): peso en kilogramos
            tipo_huevo (str): descripción del tipo de huevo
            puede_volar (bool): indica si puede volar
        """
        # Llamar al constructor de la clase padre
        super().__init__(nombre, edad, peso)
        
        # Atributos específicos de ovíparos
        self.tipo_huevo = tipo_huevo
        self.puede_volar = puede_volar
        print(f"  → Es un ovíparo que pone huevos de tipo: {tipo_huevo}")
    
    def poner_huevos(self, cantidad):
        """
        Método NUEVO específico de ovíparos.
        """
        return f"{self.nombre} ha puesto {cantidad} huevo(s) 🥚"
    
    def incubar(self, dias):
        """Método específico de ovíparos."""
        return f"{self.nombre} está incubando sus huevos por {dias} días"
    
    def moverse(self):
        """
        SOBRESCRITURA del método moverse().
        """
        if self.puede_volar:
            return f"{self.nombre} vuela por el cielo 🦅"
        else:
            return f"{self.nombre} se mueve por tierra"
    
    def obtener_info(self):
        """SOBRESCRITURA que extiende el método padre."""
        info_base = super().obtener_info()
        info_adicional = f"""        Tipo de huevo: {self.tipo_huevo}
        Puede volar: {'Sí' if self.puede_volar else 'No'}
        """
        return info_base + info_adicional


# ============================================================================
# SUBCLASES DE SEGUNDO NIVEL (Herencia multinivel)
# ============================================================================

class Perro(Mamifero):
    """
    SUBCLASE DE SEGUNDO NIVEL: Perro hereda de Mamífero
    
    Perro → Mamífero → Animal (Herencia multinivel)
    
    Hereda TODO de Mamífero, que a su vez heredó todo de Animal.
    """
    
    def __init__(self, nombre, edad, peso, raza):
        """
        Constructor de Perro.
        
        Parámetros:
            nombre (str): nombre del perro
            edad (int): edad en años
            peso (float): peso en kilogramos
            raza (str): raza del perro
        """
        # Llamar al constructor de Mamífero con valores específicos
        super().__init__(nombre, edad, peso, tipo_pelaje="corto", numero_patas=4)
        self.raza = raza
        self.trucos = []
        print(f"  → Es un perro de raza {raza}")
    
    def hacer_sonido(self):
        """SOBRESCRITURA específica para perros."""
        return f"{self.nombre} dice: ¡Guau guau! 🐕"
    
    def mover_cola(self):
        """Método NUEVO específico de perros."""
        return f"{self.nombre} mueve la cola felizmente 🐾"
    
    def aprender_truco(self, truco):
        """Método específico de perros."""
        self.trucos.append(truco)
        return f"{self.nombre} aprendió el truco: {truco}"
    
    def hacer_truco(self):
        """Ejecuta un truco aleatorio."""
        if self.trucos:
            import random
            truco = random.choice(self.trucos)
            return f"{self.nombre} hace el truco: {truco} ⭐"
        return f"{self.nombre} aún no sabe trucos"


class Gato(Mamifero):
    """
    SUBCLASE DE SEGUNDO NIVEL: Gato hereda de Mamífero
    
    Gato → Mamífero → Animal
    """
    
    def __init__(self, nombre, edad, peso, color):
        """Constructor de Gato."""
        super().__init__(nombre, edad, peso, tipo_pelaje="suave", numero_patas=4)
        self.color = color
        self.vidas = 7  # Atributo especial de gatos 😺
        print(f"  → Es un gato de color {color}")
    
    def hacer_sonido(self):
        """SOBRESCRITURA específica para gatos."""
        return f"{self.nombre} dice: ¡Miau miau! 🐱"
    
    def ronronear(self):
        """Método NUEVO específico de gatos."""
        return f"{self.nombre} ronronea contento 😺"
    
    def arañar(self, objeto):
        """Método específico de gatos."""
        return f"{self.nombre} está arañando {objeto} 🐾"
    
    def cazar(self):
        """Método específico de gatos."""
        return f"{self.nombre} está cazando 🐭"


class Aguila(Oviparo):
    """
    SUBCLASE DE SEGUNDO NIVEL: Águila hereda de Ovíparo
    
    Aguila → Ovíparo → Animal
    """
    
    def __init__(self, nombre, edad, peso, envergadura):
        """
        Constructor de Águila.
        
        Parámetros:
            envergadura (float): envergadura de las alas en metros
        """
        super().__init__(nombre, edad, peso, tipo_huevo="cascara dura", puede_volar=True)
        self.envergadura = envergadura
        self.altura_vuelo_max = 3000  # metros
        print(f"  → Es un águila con envergadura de {envergadura}m")
    
    def hacer_sonido(self):
        """SOBRESCRITURA específica para águilas."""
        return f"{self.nombre} grita: ¡Screeee! 🦅"
    
    def cazar_desde_aire(self):
        """Método NUEVO específico de águilas."""
        return f"{self.nombre} caza desde el aire con precisión 🎯"
    
    def volar_alto(self):
        """Método específico de águilas."""
        return f"{self.nombre} vuela hasta {self.altura_vuelo_max}m de altura"


class Pinguino(Oviparo):
    """
    SUBCLASE DE SEGUNDO NIVEL: Pingüino hereda de Ovíparo
    
    Pinguino → Ovíparo → Animal
    
    Ejemplo interesante: Es un ave pero NO puede volar.
    """
    
    def __init__(self, nombre, edad, peso, especie):
        """Constructor de Pingüino."""
        super().__init__(nombre, edad, peso, tipo_huevo="cascara dura", puede_volar=False)
        self.especie = especie
        self.velocidad_nado = 25  # km/h
        print(f"  → Es un pingüino de la especie {especie}")
    
    def hacer_sonido(self):
        """SOBRESCRITURA específica para pingüinos."""
        return f"{self.nombre} grazna: ¡Honk honk! 🐧"
    
    def nadar(self):
        """Método NUEVO específico de pingüinos."""
        return f"{self.nombre} nada a {self.velocidad_nado} km/h 🏊"
    
    def deslizarse(self):
        """Método específico de pingüinos."""
        return f"{self.nombre} se desliza sobre su panza en el hielo ⛸️"


# ============================================================================
# DEMOSTRACIÓN DE USO
# ============================================================================

def demostrar_herencia_basica():
    """Demuestra los conceptos básicos de herencia."""
    print("=" * 70)
    print("1. HERENCIA BÁSICA - Creando objetos de diferentes niveles")
    print("=" * 70)
    
    print("\n--- Animal (Clase Base) ---")
    animal_generico = Animal("Criatura", 5, 10.0)
    print(animal_generico.comer("comida"))
    print(animal_generico.hacer_sonido())
    print(animal_generico.moverse())
    
    print("\n--- Mamífero (Hereda de Animal) ---")
    mamifero = Mamifero("Bestia", 3, 50.0, "largo")
    print(mamifero.comer("carne"))  # Método heredado
    print(mamifero.amamantar())      # Método propio
    print(mamifero.moverse())        # Método sobrescrito
    
    print("\n--- Ovíparo (Hereda de Animal) ---")
    oviparo = Oviparo("Volador", 2, 5.0, "cascara blanda", puede_volar=True)
    print(oviparo.comer("insectos"))  # Método heredado
    print(oviparo.poner_huevos(3))    # Método propio
    print(oviparo.moverse())          # Método sobrescrito


def demostrar_herencia_multinivel():
    """Demuestra la herencia de múltiples niveles."""
    print("\n" + "=" * 70)
    print("2. HERENCIA MULTINIVEL - Perro → Mamífero → Animal")
    print("=" * 70)
    
    print("\n--- Creando un Perro ---")
    perro = Perro("Max", 5, 25.0, "Labrador")
    
    print("\n--- Métodos heredados de Animal ---")
    print(perro.comer("croquetas"))
    print(perro.dormir())
    
    print("\n--- Métodos heredados de Mamífero ---")
    print(perro.amamantar())
    print(perro.regular_temperatura())
    
    print("\n--- Métodos propios de Perro ---")
    print(perro.hacer_sonido())
    print(perro.mover_cola())
    print(perro.aprender_truco("sentarse"))
    print(perro.aprender_truco("dar la pata"))
    print(perro.hacer_truco())
    
    print("\n--- Información completa ---")
    print(perro.obtener_info())


def demostrar_polimorfismo_con_herencia():
    """
    Demuestra el polimorfismo gracias a la herencia.
    
    Objetos de diferentes clases pueden ser tratados de forma uniforme
    si comparten la misma clase padre.
    """
    print("\n" + "=" * 70)
    print("3. POLIMORFISMO A TRAVÉS DE HERENCIA")
    print("=" * 70)
    
    # Crear una colección de diferentes animales
    print("\n--- Creando zoológico virtual ---")
    animales = [
        Perro("Luna", 3, 20.0, "Pastor Alemán"),
        Gato("Michi", 2, 4.5, "naranja"),
        Aguila("Águila Real", 4, 6.0, 2.3),
        Pinguino("Pingu", 1, 15.0, "Emperador")
    ]
    
    print("\n--- Todos los animales pueden usar métodos de Animal ---")
    for animal in animales:
        print(f"\n{animal}")
        print(f"  - {animal.hacer_sonido()}")
        print(f"  - {animal.moverse()}")
        print(f"  - {animal.comer('su alimento favorito')}")


def demostrar_isinstance_y_herencia():
    """Demuestra cómo verificar tipos con herencia."""
    print("\n" + "=" * 70)
    print("4. VERIFICACIÓN DE TIPOS CON HERENCIA")
    print("=" * 70)
    
    perro = Perro("Rocky", 4, 30.0, "Rottweiler")
    gato = Gato("Pelusa", 3, 5.0, "blanco")
    aguila = Aguila("Halcón", 2, 4.0, 1.8)
    
    print("\n--- Verificando isinstance() ---")
    print(f"perro es Perro: {isinstance(perro, Perro)}")
    print(f"perro es Mamifero: {isinstance(perro, Mamifero)}")
    print(f"perro es Animal: {isinstance(perro, Animal)}")
    print(f"perro es Oviparo: {isinstance(perro, Oviparo)}")
    
    print(f"\naguila es Aguila: {isinstance(aguila, Aguila)}")
    print(f"aguila es Oviparo: {isinstance(aguila, Oviparo)}")
    print(f"aguila es Animal: {isinstance(aguila, Animal)}")
    print(f"aguila es Mamifero: {isinstance(aguila, Mamifero)}")
    
    print("\n--- Filtrando por tipo ---")
    animales = [perro, gato, aguila]
    
    print("\nMamíferos en la lista:")
    mamiferos = [a for a in animales if isinstance(a, Mamifero)]
    for m in mamiferos:
        print(f"  - {m}")
    
    print("\nOvíparos en la lista:")
    oviparos = [a for a in animales if isinstance(a, Oviparo)]
    for o in oviparos:
        print(f"  - {o}")


def demostrar_uso_super():
    """Demuestra el uso de super() en herencia."""
    print("\n" + "=" * 70)
    print("5. USO DE super() PARA ACCEDER A LA CLASE PADRE")
    print("=" * 70)
    
    class AnimalConLog(Animal):
        """Clase que extiende métodos usando super()."""
        
        def comer(self, alimento):
            """Extiende el método comer() agregando un log."""
            # Llamar al método de la clase padre
            resultado = super().comer(alimento)
            # Agregar funcionalidad adicional
            log = f"[LOG] {self.nombre} comió {alimento}"
            return f"{resultado}\n{log}"
    
    print("\n--- Animal con logging ---")
    animal_log = AnimalConLog("Logger", 2, 15.0)
    print(animal_log.comer("frutas"))


# ============================================================================
# PROGRAMA PRINCIPAL
# ============================================================================

if __name__ == "__main__":
    print("\n")
    print("╔" + "═" * 68 + "╗")
    print("║" + "DEMOSTRACIÓN COMPLETA: HERENCIA EN POO".center(68) + "║")
    print("╚" + "═" * 68 + "╝")
    
    # Ejecutar todas las demostraciones
    demostrar_herencia_basica()
    demostrar_herencia_multinivel()
    demostrar_polimorfismo_con_herencia()
    demostrar_isinstance_y_herencia()
    demostrar_uso_super()
    
    # Resumen final
    print("\n" + "=" * 70)
    print("RESUMEN: CONCEPTOS CLAVE DE HERENCIA")
    print("=" * 70)
    print("""
    ✓ HERENCIA: Mecanismo para crear clases basadas en otras clases
    
    ✓ SINTAXIS:
      class ClaseHija(ClasePadre):
          # código de la clase hija
    
    ✓ super(): Función para llamar métodos de la clase padre
      - super().__init__(): llama al constructor del padre
      - super().metodo(): llama a cualquier método del padre
    
    ✓ SOBRESCRITURA (Override):
      - Redefinir un método heredado en la subclase
      - Permite personalizar el comportamiento
    
    ✓ HERENCIA MULTINIVEL:
      - ClaseC → ClaseB → ClaseA
      - ClaseC hereda de B, que hereda de A
    
    ✓ isinstance(objeto, Clase):
      - Verifica si un objeto es instancia de una clase
      - Incluye clases padre en la jerarquía
    
    ✓ BENEFICIOS:
      - Reutilización de código
      - Organización jerárquica
      - Polimorfismo
      - Facilita mantenimiento
    """)
    
    print("\n" + "=" * 70)
    print("¡Demostración completada!")
    print("=" * 70)

