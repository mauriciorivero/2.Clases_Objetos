# 🎯 Ejercicios Prácticos de POO en Python

Este documento contiene ejercicios prácticos para reforzar los conceptos aprendidos en cada módulo.

---

## 📝 Ejercicio 1: Creación de Clases - Sistema de Biblioteca

### Objetivo
Crear un sistema básico de biblioteca con la clase `Libro`.

### Requisitos
Crea una clase `Libro` con:

**Atributos:**
- `titulo` (str)
- `autor` (str)
- `isbn` (str)
- `año_publicacion` (int)
- `disponible` (bool) - por defecto True
- Atributo de clase: `total_libros` para contar libros creados

**Métodos:**
- `prestar()` - marca el libro como no disponible
- `devolver()` - marca el libro como disponible
- `obtener_info()` - retorna información del libro
- `es_antiguo()` - retorna True si tiene más de 50 años

**Métodos especiales:**
- `__str__()` - representación legible
- `__repr__()` - representación técnica

### Código Base

```python
class Libro:
    # Implementa aquí
    pass

# Pruebas
libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "978-0307474728", 1967)
print(libro1.obtener_info())
libro1.prestar()
print(f"¿Disponible? {libro1.disponible}")
libro1.devolver()
print(f"¿Es antiguo? {libro1.es_antiguo()}")
```

---

## 📝 Ejercicio 2: Agregación y Composición - Sistema Bancario

### Objetivo
Implementar un sistema bancario con cuentas y transacciones.

### Requisitos

**Clase `Cliente`** (existe independientemente):
- Atributos: `nombre`, `cedula`, `telefono`
- Métodos: `obtener_info()`

**Clase `Transaccion`** (composición - depende de Cuenta):
- Atributos: `tipo` (depósito/retiro), `monto`, `fecha`
- Métodos: `__str__()`

**Clase `CuentaBancaria`** (contiene Cliente y Transacciones):
- Atributos: `numero_cuenta`, `cliente`, `saldo`, `transacciones`
- Métodos:
  - `depositar(monto)` - agrega transacción
  - `retirar(monto)` - agrega transacción
  - `agregar_transaccion()` - COMPOSICIÓN
  - `obtener_historial()` - muestra transacciones

### Preguntas
1. ¿Por qué `Cliente` es agregación?
2. ¿Por qué `Transaccion` es composición?

### Código Base

```python
from datetime import datetime

class Cliente:
    # Implementa aquí
    pass

class Transaccion:
    # Implementa aquí
    pass

class CuentaBancaria:
    # Implementa aquí
    pass

# Pruebas
cliente1 = Cliente("María Rodríguez", "12345678", "555-1234")
cuenta = CuentaBancaria("001-12345", cliente1)
cuenta.depositar(1000)
cuenta.retirar(200)
cuenta.obtener_historial()
```

---

## 📝 Ejercicio 3: Instanciación - Gestión de Productos

### Objetivo
Practicar diferentes formas de instanciar objetos.

### Requisitos

**Clase `Producto`:**
- Atributos: `codigo`, `nombre`, `precio`, `stock`, `categoria`
- Constructor normal
- Factory method: `desde_csv(linea_csv)` - crea producto desde string CSV
- Factory method: `desde_dict(diccionario)` - crea producto desde dict
- Factory method: `crear_por_defecto()` - crea producto genérico

### Tareas

1. Crear 5 productos usando el constructor normal
2. Crear 3 productos desde diccionarios (simulando datos de API)
3. Crear 2 productos desde strings CSV
4. Listar todos los productos creados

### Código Base

```python
class Producto:
    contador = 0
    
    def __init__(self, codigo, nombre, precio, stock, categoria="General"):
        # Implementa aquí
        pass
    
    @classmethod
    def desde_csv(cls, linea_csv):
        """
        Crea producto desde CSV: "P001,Laptop,1200.50,10,Electrónica"
        """
        # Implementa aquí
        pass
    
    @classmethod
    def desde_dict(cls, datos):
        """
        Crea producto desde diccionario
        """
        # Implementa aquí
        pass

# Pruebas
# Normal
p1 = Producto("P001", "Mouse", 25.99, 50, "Periféricos")

# Desde CSV
p2 = Producto.desde_csv("P002,Teclado,75.50,30,Periféricos")

# Desde diccionario
datos = {"codigo": "P003", "nombre": "Monitor", "precio": 299.99, "stock": 15}
p3 = Producto.desde_dict(datos)
```

---

## 📝 Ejercicio 4: Herencia - Sistema de Vehículos

### Objetivo
Crear una jerarquía de vehículos usando herencia.

### Requisitos

**Clase base `Vehiculo`:**
- Atributos: `marca`, `modelo`, `año`, `color`
- Métodos: `arrancar()`, `detener()`, `obtener_info()`

**Subclase `Automovil`** (hereda de Vehiculo):
- Atributos adicionales: `numero_puertas`, `tipo_combustible`
- Métodos: sobrescribir `arrancar()` para ser específico

**Subclase `Motocicleta`** (hereda de Vehiculo):
- Atributos adicionales: `cilindrada`, `tipo_motor`
- Métodos: `hacer_caballito()`, sobrescribir `arrancar()`

**Subclase `Camion`** (hereda de Vehiculo):
- Atributos adicionales: `capacidad_carga`, `numero_ejes`
- Métodos: `cargar()`, `descargar()`

### Tareas

1. Implementar todas las clases con herencia correcta
2. Usar `super()` en todos los constructores
3. Crear 2 objetos de cada tipo
4. Demostrar que todos son instancias de `Vehiculo`
5. Crear una lista mixta y llamar a `arrancar()` en cada uno (polimorfismo)

### Código Base

```python
class Vehiculo:
    def __init__(self, marca, modelo, año, color):
        # Implementa aquí
        pass
    
    def arrancar(self):
        return f"{self.marca} {self.modelo} está arrancando"

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, año, color, numero_puertas, tipo_combustible):
        # Usa super() aquí
        pass

# Implementa Motocicleta y Camion

# Pruebas
auto = Automovil("Toyota", "Corolla", 2023, "Rojo", 4, "Gasolina")
moto = Motocicleta("Yamaha", "YZF-R3", 2023, "Azul", 321, "2 tiempos")
camion = Camion("Volvo", "FH16", 2022, "Blanco", 20000, 3)

# Lista polimórfica
vehiculos = [auto, moto, camion]
for v in vehiculos:
    print(v.arrancar())
    print(isinstance(v, Vehiculo))  # Debe ser True para todos
```

---

## 📝 Ejercicio 5: Polimorfismo - Sistema de Formas Geométricas

### Objetivo
Implementar polimorfismo para calcular áreas y perímetros de diferentes formas.

### Requisitos

**Clase base `Forma`:**
- Atributos: `color`
- Métodos abstractos: `calcular_area()`, `calcular_perimetro()`

**Subclases:**

1. **`Circulo`**
   - Atributo: `radio`
   - Implementar área: π × r²
   - Implementar perímetro: 2 × π × r

2. **`Rectangulo`**
   - Atributos: `ancho`, `alto`
   - Implementar área: ancho × alto
   - Implementar perímetro: 2 × (ancho + alto)

3. **`Triangulo`**
   - Atributos: `base`, `altura`, `lado1`, `lado2`, `lado3`
   - Implementar área: (base × altura) / 2
   - Implementar perímetro: lado1 + lado2 + lado3

**Clase `CalculadoraFormas`:**
- Método: `calcular_area_total(lista_formas)` - suma todas las áreas
- Método: `generar_reporte(lista_formas)` - muestra info de todas

### Tareas

1. Implementar todas las clases
2. Crear al menos 2 objetos de cada forma
3. Usar `CalculadoraFormas` para procesar todas las formas
4. Demostrar que el código funciona sin importar el tipo de forma (polimorfismo)

### Código Base

```python
import math

class Forma:
    def __init__(self, color):
        self.color = color
    
    def calcular_area(self):
        raise NotImplementedError("Subclases deben implementar este método")
    
    def calcular_perimetro(self):
        raise NotImplementedError("Subclases deben implementar este método")

class Circulo(Forma):
    # Implementa aquí
    pass

class Rectangulo(Forma):
    # Implementa aquí
    pass

class Triangulo(Forma):
    # Implementa aquí
    pass

class CalculadoraFormas:
    @staticmethod
    def calcular_area_total(formas):
        """
        POLIMORFISMO: funciona con cualquier forma que tenga calcular_area()
        """
        # Implementa aquí
        pass
    
    @staticmethod
    def generar_reporte(formas):
        # Implementa aquí
        pass

# Pruebas
formas = [
    Circulo("Rojo", 5),
    Rectangulo("Azul", 10, 5),
    Triangulo("Verde", 6, 4, 5, 5, 5),
    Circulo("Amarillo", 3),
    Rectangulo("Morado", 8, 8)
]

# Polimorfismo en acción
area_total = CalculadoraFormas.calcular_area_total(formas)
print(f"Área total: {area_total:.2f}")

CalculadoraFormas.generar_reporte(formas)
```

---

## 📝 Ejercicio 6 (DESAFÍO): Sistema de E-commerce Completo

### Objetivo
Integrar TODOS los conceptos aprendidos en un sistema completo.

### Requisitos

Implementa un sistema de e-commerce con:

**Clases necesarias:**

1. **`Usuario`** - clientes del sistema
2. **`Producto`** - productos a la venta
3. **`CarritoCompra`** - contiene productos (agregación)
4. **`Pedido`** - contiene productos y detalles (composición)
5. **`MetodoPago`** (clase base abstracta)
   - `PagoTarjeta` (subclase)
   - `PagoPayPal` (subclase)
   - `PagoEfectivo` (subclase)
6. **`SistemaVentas`** - gestiona todo

### Funcionalidades

1. Usuarios pueden agregar productos al carrito
2. Carrito puede calcular total
3. Crear pedido desde carrito
4. Procesar pago usando diferentes métodos (POLIMORFISMO)
5. Generar factura del pedido

### Conceptos a Demostrar

- ✅ Creación de clases
- ✅ Agregación (Usuario ← CarritoCompra ← Productos)
- ✅ Composición (Pedido ← DetallesPedido)
- ✅ Instanciación (múltiples formas de crear objetos)
- ✅ Herencia (MetodoPago y sus subclases)
- ✅ Polimorfismo (procesar_pago funciona con cualquier método)

---

## 🎓 Criterios de Evaluación

Para cada ejercicio, asegúrate de:

- [ ] Código funciona sin errores
- [ ] Comentarios explican las decisiones importantes
- [ ] Nombres de variables y métodos son descriptivos
- [ ] Se usan correctamente los conceptos de POO
- [ ] El código está bien organizado
- [ ] Se incluyen pruebas que demuestran funcionalidad

---

## 📚 Recursos Adicionales

### Documentación Oficial
- [Python Classes](https://docs.python.org/3/tutorial/classes.html)
- [Python Data Model](https://docs.python.org/3/reference/datamodel.html)

### Tips
1. **Empieza simple**: No intentes implementar todo a la vez
2. **Prueba frecuentemente**: Verifica cada clase antes de continuar
3. **Usa print()**: Para entender qué está pasando en tu código
4. **Dibuja diagramas**: Ayuda visualizar las relaciones entre clases
5. **Consulta los ejemplos**: Los módulos tienen código de referencia

---

## 💡 Soluciones

Las soluciones están disponibles en cada módulo del curso como referencia.
Intenta resolver los ejercicios primero antes de consultar las soluciones.

---

**¡Éxito en tu aprendizaje! 🚀**

