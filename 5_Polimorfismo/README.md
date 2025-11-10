# Módulo 5: Polimorfismo

## 📖 Descripción

Este módulo enseña el polimorfismo: la capacidad de objetos de diferentes clases de responder al mismo mensaje de diferentes maneras.

## 🎯 Objetivos de Aprendizaje

Al completar este módulo, serás capaz de:
- ✅ Entender qué es el polimorfismo
- ✅ Implementar polimorfismo de subtipos
- ✅ Usar duck typing en Python
- ✅ Crear sistemas flexibles y extensibles
- ✅ Aplicar el principio "una interfaz, múltiples implementaciones"

## 📁 Archivos

- `empleados_polimorfismo.py` - Sistema de nómina polimórfico

## 🚀 Cómo Ejecutar

```bash
python empleados_polimorfismo.py
```

## 📚 Conceptos Cubiertos

### 1. ¿Qué es el Polimorfismo?

**"Una interfaz, múltiples implementaciones"**

Diferentes objetos responden al mismo mensaje de formas diferentes:

```python
# Todos tienen calcular_salario(), pero cada uno lo hace diferente
empleado_tc.calcular_salario()    # Salario fijo
empleado_ph.calcular_salario()    # Horas * tarifa
empleado_com.calcular_salario()   # Base + comisión
```

### 2. Polimorfismo de Subtipos

Usando herencia:

```python
class Empleado:
    def calcular_salario(self):
        raise NotImplementedError

class EmpleadoTiempoCompleto(Empleado):
    def calcular_salario(self):
        return self.salario_mensual  # Implementación específica

class EmpleadoPorHoras(Empleado):
    def calcular_salario(self):
        return self.horas * self.tarifa  # Implementación diferente
```

### 3. Ventaja: Código Genérico

Un mismo código funciona con diferentes tipos:

```python
def procesar_nomina(empleados):
    total = 0
    for empleado in empleados:
        # No importa QUÉ tipo de empleado sea
        # Solo importa que tenga calcular_salario()
        salario = empleado.calcular_salario()
        total += salario
    return total

# Funciona con CUALQUIER tipo de empleado
empleados = [
    EmpleadoTiempoCompleto(...),
    EmpleadoPorHoras(...),
    EmpleadoPorComision(...),
    EmpleadoFreelance(...)
]

total = procesar_nomina(empleados)  # ✅ Polimorfismo en acción
```

### 4. Duck Typing

**"Si camina como pato y grazna como pato, es un pato"**

Python no verifica el tipo, solo que tenga los métodos necesarios:

```python
class Perro:
    def hacer_sonido(self):
        return "¡Guau!"

class Gato:
    def hacer_sonido(self):
        return "¡Miau!"

class Radio:  # ¡No es un animal!
    def hacer_sonido(self):
        return "♪ Música ♪"

# Función polimórfica
def hacer_sonar(cosa):
    return cosa.hacer_sonido()

# Funciona con TODOS, no importa el tipo
print(hacer_sonar(Perro()))   # ¡Guau!
print(hacer_sonar(Gato()))    # ¡Miau!
print(hacer_sonar(Radio()))   # ♪ Música ♪
```

## 🎯 Ejemplo Práctico: Sistema de Nómina

El ejemplo implementa un sistema completo con:

1. **Empleados de Tiempo Completo**: Salario fijo mensual
2. **Empleados por Horas**: Cobran por hora trabajada
3. **Empleados por Comisión**: Base + % de ventas
4. **Freelancers**: Cobran por proyecto

Todos responden a `calcular_salario()` de forma diferente.

## 💡 Beneficios del Polimorfismo

1. **Código más flexible**: Fácil agregar nuevos tipos
2. **Extensibilidad**: Nuevas clases sin cambiar código existente
3. **Mantenimiento**: Cambios localizados en cada clase
4. **Abstracción**: Trabajar con interfaces, no implementaciones

## 🔄 Tipos de Polimorfismo

| Tipo | Descripción | Ejemplo |
|------|-------------|---------|
| **Subtipos** | Via herencia | `Animal → Perro, Gato` |
| **Duck Typing** | Sin herencia | "tiene método X" |
| **Sobrecarga** | Operadores | `__add__`, `__mul__` |

## 🎓 Ejercicios Sugeridos

1. Crea un sistema de formas con `calcular_area()` polimórfico
2. Implementa diferentes estrategias de descuento en un sistema de ventas
3. Crea un reproductor multimedia que maneje audio, video e imágenes
4. Implementa diferentes métodos de pago (tarjeta, efectivo, PayPal)

## 🔍 Puntos Clave

- **Polimorfismo**: Mismo método, diferentes comportamientos
- **Interfaz común**: Define QUÉ hacer, no CÓMO
- **Duck Typing**: Python no verifica tipos, solo métodos
- **Extensible**: Fácil agregar nuevos tipos sin romper código existente
- **Principio**: "Programa hacia interfaces, no implementaciones"

## ⭐ Principio de Diseño

```
"El código debe depender de abstracciones, no de implementaciones concretas"
```

Esto significa:
- Escribe funciones que acepten la clase base
- No te preocupes por los tipos específicos
- Deja que el polimorfismo haga su magia

## 📊 Ejemplo Visual

```
Sistema de Nómina
       ↓
[calcular_salario() para todos]
       ↓
┌──────────┬──────────┬──────────┬──────────┐
│   T.C.   │   Horas  │ Comisión │Freelance │
│  Fijo    │ * Tarifa │  Base+%  │ Proyecto │
└──────────┴──────────┴──────────┴──────────┘
   ↓            ↓          ↓          ↓
  3500        4200       5600       8000

Total: 21,300
```

¡El sistema calcula todo sin saber el tipo específico de cada empleado!

