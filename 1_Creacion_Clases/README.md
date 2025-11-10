# Módulo 1: Creación de Clases

## 📖 Descripción

Este módulo enseña los conceptos fundamentales de la creación de clases en Python.

## 🎯 Objetivos de Aprendizaje

Al completar este módulo, serás capaz de:
- ✅ Definir qué es una clase
- ✅ Crear clases con atributos y métodos
- ✅ Entender el constructor `__init__`
- ✅ Usar `self` correctamente
- ✅ Diferenciar entre atributos de instancia y de clase
- ✅ Implementar métodos de instancia, de clase y estáticos
- ✅ Usar métodos especiales (`__str__`, `__repr__`)

## 📁 Archivos

- `persona.py` - Ejemplo completo de la clase Persona

## 🚀 Cómo Ejecutar

```bash
python persona.py
```

## 📚 Conceptos Cubiertos

### 1. Definición de Clase

```python
class Persona:
    """Una clase representa una plantilla para crear objetos"""
    pass
```

### 2. Constructor `__init__`

El método que se ejecuta al crear un objeto:

```python
def __init__(self, nombre, edad):
    self.nombre = nombre  # Atributo de instancia
    self.edad = edad
```

### 3. Atributos

- **Atributos de instancia:** Únicos para cada objeto
- **Atributos de clase:** Compartidos por todas las instancias

### 4. Métodos

- **Métodos de instancia:** Operan sobre datos del objeto (usan `self`)
- **Métodos de clase:** Operan sobre la clase (usan `@classmethod` y `cls`)
- **Métodos estáticos:** No acceden a instancia ni clase (usan `@staticmethod`)

### 5. Métodos Especiales

- `__str__()`: Representación legible para usuarios
- `__repr__()`: Representación técnica para desarrolladores

## 💡 Ejemplo Rápido

```python
# Crear una persona
persona = Persona("Juan", 25, "12345")

# Usar métodos
print(persona.saludar())  # Método de instancia
persona.cumplir_años()    # Modifica el estado

# Método de clase
total = Persona.obtener_total_personas()

# Método estático
es_valida = Persona.validar_edad(30)
```

## 🎓 Ejercicios Sugeridos

1. Modifica la clase `Persona` para agregar un atributo `profesion`
2. Crea un método `trabajar()` que use la profesión
3. Agrega validación en el constructor para la edad
4. Crea una clase similar `Estudiante` con atributos propios

## 🔍 Puntos Clave

- **`self`** es la referencia al objeto actual
- **`__init__`** es el constructor, se llama automáticamente
- Los **atributos de clase** se definen fuera de `__init__`
- Los **métodos** definen el comportamiento de los objetos

