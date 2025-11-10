# Módulo 3: Instanciación de Clases

## 📖 Descripción

Este módulo explora las diferentes formas de crear objetos (instancias) en Python.

## 🎯 Objetivos de Aprendizaje

Al completar este módulo, serás capaz de:
- ✅ Crear instancias de clases de múltiples formas
- ✅ Usar argumentos posicionales y nombrados
- ✅ Crear objetos dinámicamente
- ✅ Implementar factory methods
- ✅ Verificar tipos e instancias
- ✅ Entender la independencia entre objetos

## 📁 Archivos

- `instanciacion_ejemplos.py` - Ejemplos completos de instanciación

## 🚀 Cómo Ejecutar

```bash
python instanciacion_ejemplos.py
```

## 📚 Conceptos Cubiertos

### 1. Instanciación Básica

```python
# Forma 1: Argumentos posicionales
persona1 = Persona("Juan", 25, "123")

# Forma 2: Argumentos nombrados
persona2 = Persona(
    nombre="María",
    edad=30,
    identificacion="456"
)

# Forma 3: Mezcla
persona3 = Persona("Carlos", edad=28, identificacion="789")
```

### 2. Instanciación Dinámica

Crear objetos desde datos externos:

```python
# Desde diccionario
datos = {"nombre": "Ana", "edad": 22, "identificacion": "321"}
persona = Persona(**datos)  # Desempaquetado

# Desde lista
personas = []
for datos in lista_datos:
    persona = Persona(**datos)
    personas.append(persona)
```

### 3. Factory Methods

Métodos alternativos para crear instancias:

```python
class Fecha:
    @classmethod
    def desde_string(cls, fecha_str):
        dia, mes, año = fecha_str.split('-')
        return cls(int(dia), int(mes), int(año))
    
    @classmethod
    def hoy(cls):
        # Retorna fecha actual
        return cls(dia_actual, mes_actual, año_actual)

# Uso
fecha1 = Fecha(10, 11, 2025)  # Constructor normal
fecha2 = Fecha.desde_string("10-11-2025")  # Factory method
fecha3 = Fecha.hoy()  # Factory method
```

### 4. Verificación de Instancias

```python
# Verificar tipo
print(isinstance(persona, Persona))  # True

# Obtener tipo
print(type(persona))  # <class 'Persona'>

# ID único
print(id(persona))  # Dirección de memoria
```

## 💡 Independencia de Instancias

Cada instancia es única y tiene:
- Su propia dirección en memoria
- Sus propios valores de atributos
- Estado independiente de otras instancias

```python
p1 = Persona("Juan", 25, "123")
p2 = Persona("María", 30, "456")

p1.edad = 26  # Solo afecta a p1
print(p2.edad)  # Sigue siendo 30

print(p1 is p2)  # False - son objetos diferentes
```

## 🎓 Ejercicios Sugeridos

1. Crea 10 estudiantes usando un bucle
2. Implementa un factory method `desde_csv()` que lea desde archivo
3. Crea instancias dinámicamente desde entrada del usuario
4. Implementa un sistema que valide datos antes de instanciar

## 🔍 Puntos Clave

- **Instanciación**: Proceso de crear objetos concretos desde una clase
- **Cada objeto es único**: Tiene su propia memoria y estado
- **Factory methods**: Formas alternativas de crear objetos (usan `@classmethod`)
- **Desempaquetado (`**`)**: Útil para crear objetos desde diccionarios
- **isinstance()**: Verifica si un objeto es instancia de una clase

