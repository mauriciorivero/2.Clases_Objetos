# Módulo 4: Herencia

## 📖 Descripción

Este módulo enseña el concepto de herencia: crear nuevas clases basadas en clases existentes.

## 🎯 Objetivos de Aprendizaje

Al completar este módulo, serás capaz de:
- ✅ Entender qué es la herencia
- ✅ Crear subclases que heredan de superclases
- ✅ Usar `super()` para acceder a la clase padre
- ✅ Sobrescribir métodos (override)
- ✅ Implementar herencia multinivel
- ✅ Verificar tipos con `isinstance()`

## 📁 Archivos

- `animales_herencia.py` - Jerarquía de animales con herencia

## 🚀 Cómo Ejecutar

```bash
python animales_herencia.py
```

## 📚 Conceptos Cubiertos

### 1. Sintaxis de Herencia

```python
# Clase padre (superclase)
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hacer_sonido(self):
        return "Sonido genérico"

# Clase hija (subclase)
class Perro(Animal):  # Hereda de Animal
    def hacer_sonido(self):  # Sobrescribe el método
        return "¡Guau!"
```

### 2. Uso de `super()`

Accede a métodos de la clase padre:

```python
class Mamifero(Animal):
    def __init__(self, nombre, tipo_pelaje):
        super().__init__(nombre)  # Llama al __init__ de Animal
        self.tipo_pelaje = tipo_pelaje
```

### 3. Herencia Multinivel

```python
Animal
  ↓
Mamifero
  ↓
Perro
```

`Perro` hereda de `Mamifero`, que hereda de `Animal`:

```python
perro = Perro("Max", "Labrador")

# Tiene acceso a métodos de todas las clases padre
perro.comer()       # De Animal
perro.amamantar()   # De Mamifero
perro.mover_cola()  # De Perro
```

### 4. Sobrescritura (Override)

Redefinir un método heredado:

```python
class Animal:
    def moverse(self):
        return "Se está moviendo"

class Ave(Animal):
    def moverse(self):  # Override
        return "Vuela por el cielo"

class Pez(Animal):
    def moverse(self):  # Override
        return "Nada en el agua"
```

### 5. Verificación con `isinstance()`

```python
perro = Perro("Max", "Labrador")

print(isinstance(perro, Perro))     # True
print(isinstance(perro, Mamifero))  # True
print(isinstance(perro, Animal))    # True
print(isinstance(perro, Ave))       # False
```

## 🌳 Jerarquía del Ejemplo

```
Animal (clase base)
├── Mamifero
│   ├── Perro
│   └── Gato
└── Oviparo
    ├── Aguila
    └── Pinguino
```

## 💡 Beneficios de la Herencia

1. **Reutilización de código**: No repetir código común
2. **Organización**: Jerarquías lógicas de clases
3. **Mantenimiento**: Cambios en un lugar afectan a todas las subclases
4. **Extensibilidad**: Fácil agregar nuevos tipos

## 🎓 Ejercicios Sugeridos

1. Crea una jerarquía `Vehiculo → [Coche, Moto, Bicicleta]`
2. Implementa `Figura → [Circulo, Rectangulo, Triangulo]`
3. Crea `Empleado → [EmpleadoTiempoCompleto, Freelancer]`
4. Agrega métodos específicos a cada subclase

## 🔍 Puntos Clave

- **Herencia**: Mecanismo para reutilizar código
- **Sintaxis**: `class Hija(Padre):`
- **super()**: Accede a la clase padre
- **Override**: Redefinir métodos heredados
- **isinstance()**: Verifica toda la jerarquía
- **DRY**: Don't Repeat Yourself - la herencia evita repetición

## ⚠️ Cuándo NO usar Herencia

- Si no hay relación "es-un" (usa composición)
- Si crea jerarquías muy profundas (complejas de mantener)
- Si necesitas heredar de múltiples clases no relacionadas

