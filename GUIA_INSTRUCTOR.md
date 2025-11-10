# 👨‍🏫 Guía para el Instructor

## 📋 Contenido del Material

Este material de entrenamiento contiene ejemplos completos y detallados de Programación Orientada a Objetos en Python, organizados en 5 módulos progresivos.

---

## 📁 Estructura del Proyecto

```
2.Clases_Objetos/
│
├── README.md                          # Descripción general del curso
├── GUIA_INSTRUCTOR.md                 # Este archivo
├── EJERCICIOS_PRACTICOS.md            # 6 ejercicios para estudiantes
│
├── 1_Creacion_Clases/
│   ├── README.md                      # Guía del módulo
│   └── persona.py                     # Ejemplo: Clase Persona
│
├── 2_Agregacion_Composicion/
│   ├── README.md                      # Guía del módulo
│   └── curso_estudiante.py            # Ejemplo: Curso, Estudiante, Módulo
│
├── 3_Instanciacion/
│   ├── README.md                      # Guía del módulo
│   └── instanciacion_ejemplos.py      # Múltiples formas de instanciar
│
├── 4_Herencia/
│   ├── README.md                      # Guía del módulo
│   └── animales_herencia.py           # Jerarquía de animales
│
└── 5_Polimorfismo/
    ├── README.md                      # Guía del módulo
    └── empleados_polimorfismo.py      # Sistema de nómina polimórfico
```

---

## 🎯 Objetivos Generales del Curso

Al finalizar este curso, los estudiantes serán capaces de:

1. ✅ Crear clases con atributos y métodos
2. ✅ Entender y aplicar encapsulamiento
3. ✅ Distinguir entre agregación y composición
4. ✅ Instanciar objetos de múltiples formas
5. ✅ Implementar herencia para reutilizar código
6. ✅ Aplicar polimorfismo para crear sistemas flexibles
7. ✅ Diseñar sistemas orientados a objetos completos

---

## 📅 Plan de Clases Sugerido

### Semana 1: Fundamentos

**Sesión 1 (2-3 horas): Creación de Clases**
- Teoría: ¿Qué es POO? ¿Por qué usarla?
- Práctica: Ejecutar y analizar `persona.py`
- Ejercicio: Modificar la clase Persona
- Tarea: Crear clase Estudiante similar

**Sesión 2 (2-3 horas): Instanciación**
- Teoría: Objetos vs Clases
- Práctica: Ejecutar `instanciacion_ejemplos.py`
- Ejercicio: Crear objetos de diferentes formas
- Tarea: Implementar factory methods propios

---

### Semana 2: Relaciones

**Sesión 3 (3 horas): Agregación y Composición**
- Teoría: Diferencias entre agregación y composición
- Práctica: Analizar `curso_estudiante.py`
- Ejercicio: Sistema de biblioteca (Ejercicio 2)
- Tarea: Completar ejercicio bancario

**Sesión 4 (2 horas): Repaso y Práctica**
- Resolver dudas de las sesiones anteriores
- Trabajo en ejercicios prácticos
- Mini proyecto: Sistema básico

---

### Semana 3: Herencia y Polimorfismo

**Sesión 5 (3 horas): Herencia**
- Teoría: Jerarquías de clases, super()
- Práctica: Ejecutar `animales_herencia.py`
- Ejercicio: Sistema de vehículos (Ejercicio 4)
- Tarea: Crear jerarquía propia

**Sesión 6 (3 horas): Polimorfismo**
- Teoría: "Una interfaz, múltiples implementaciones"
- Práctica: Analizar `empleados_polimorfismo.py`
- Ejercicio: Sistema de formas (Ejercicio 5)
- Tarea: Comenzar proyecto final

---

### Semana 4: Integración

**Sesión 7 (3 horas): Proyecto Integrador**
- Trabajo en ejercicio 6 (e-commerce)
- Asesoría individual
- Resolver dudas específicas

**Sesión 8 (2 horas): Presentaciones**
- Estudiantes presentan sus proyectos
- Retroalimentación
- Evaluación final

---

## 🔧 Preparación del Ambiente

### Requisitos
- Python 3.6 o superior
- Editor de código (VS Code, PyCharm, etc.)
- Terminal/Consola

### Verificación del Ambiente

```bash
# Verificar versión de Python
python3 --version

# Navegar al directorio
cd /Users/mauriciorivero/Documents/SENA2025/3287281/Python_Django/2.Clases_Objetos

# Ejecutar primer ejemplo
cd 1_Creacion_Clases
python3 persona.py
```

---

## 📖 Cómo Usar los Ejemplos

### Para Demostración en Clase

1. **Proyectar el código** - Mostrar el archivo en el editor
2. **Leer comentarios** - Los comentarios explican cada concepto
3. **Ejecutar el programa** - Mostrar la salida
4. **Modificar en vivo** - Cambiar valores y re-ejecutar
5. **Preguntar** - Verificar comprensión

### Para Práctica Individual

1. Estudiantes leen el código primero
2. Ejecutan el ejemplo completo
3. Modifican partes específicas
4. Experimentan con cambios
5. Comparten resultados

---

## 💡 Tips para Enseñar POO

### Conceptos Clave por Enfatizar

1. **Módulo 1 - Creación de Clases**
   - La clase es el molde, el objeto es la instancia
   - `self` siempre referencia al objeto actual
   - `__init__` se ejecuta automáticamente

2. **Módulo 2 - Agregación vs Composición**
   - Agregación: el objeto puede vivir solo (Estudiante)
   - Composición: el objeto depende del contenedor (Módulo)
   - Pregunta clave: "¿Puede existir independientemente?"

3. **Módulo 3 - Instanciación**
   - Cada objeto es único (diferente ID en memoria)
   - Factory methods dan flexibilidad
   - `isinstance()` verifica tipos

4. **Módulo 4 - Herencia**
   - "Es-un" vs "Tiene-un"
   - `super()` accede al padre
   - Override personaliza comportamiento

5. **Módulo 5 - Polimorfismo**
   - Mismo método, diferentes implementaciones
   - Permite código genérico
   - Duck typing es pythonic

---

## 🎓 Evaluación Sugerida

### Evaluación Continua (60%)

- **Participación en clase**: 10%
- **Ejercicios prácticos (1-5)**: 30% (6% cada uno)
- **Tareas**: 20%

### Proyecto Final (40%)

Ejercicio 6: Sistema de E-commerce

**Criterios de evaluación:**
- Funcionalidad (15%): El sistema funciona correctamente
- POO (15%): Uso correcto de conceptos de POO
- Código limpio (5%): Organización y comentarios
- Creatividad (5%): Características adicionales

---

## 📊 Rúbrica para Proyectos

| Criterio | Excelente (100%) | Bueno (75%) | Suficiente (50%) | Insuficiente (25%) |
|----------|------------------|-------------|------------------|-------------------|
| **Clases** | Todas las clases bien diseñadas | Mayoría bien diseñadas | Algunas problemas | Diseño pobre |
| **Herencia** | Jerarquía lógica y eficiente | Herencia funcional | Herencia básica | No usa herencia |
| **Polimorfismo** | Implementado correctamente | Implementado parcialmente | Intento de polimorfismo | No usa polimorfismo |
| **Código limpio** | Muy legible, bien comentado | Legible, comentarios | Poco legible | Código confuso |
| **Funcionalidad** | 100% funcional | >75% funcional | >50% funcional | <50% funcional |

---

## 🚨 Errores Comunes y Soluciones

### Error 1: Olvidar `self`

```python
# ❌ Incorrecto
class Persona:
    def __init__(nombre, edad):  # Falta self
        self.nombre = nombre

# ✅ Correcto
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
```

### Error 2: No usar `super()` en herencia

```python
# ❌ Incorrecto
class Estudiante(Persona):
    def __init__(self, nombre, edad, matricula):
        self.nombre = nombre  # Duplicando código
        self.edad = edad
        self.matricula = matricula

# ✅ Correcto
class Estudiante(Persona):
    def __init__(self, nombre, edad, matricula):
        super().__init__(nombre, edad)
        self.matricula = matricula
```

### Error 3: Confundir atributos de clase e instancia

```python
# ❌ Problemático
class Estudiante:
    cursos = []  # Compartido por TODAS las instancias
    
    def agregar_curso(self, curso):
        self.cursos.append(curso)  # ¡Todos los estudiantes tendrán todos los cursos!

# ✅ Correcto
class Estudiante:
    def __init__(self):
        self.cursos = []  # Único para cada instancia
```

---

## 🔍 Actividades Complementarias

### Debates en Clase

1. **¿Cuándo usar herencia vs composición?**
2. **¿Python es realmente orientado a objetos?**
3. **¿Ventajas y desventajas de duck typing?**

### Ejercicios Rápidos (5-10 minutos)

1. En una pizarra, dibujar diagrama de clases
2. Identificar errores en código proyectado
3. Predecir salida de código sin ejecutarlo
4. Diseñar clases para un problema dado

### Proyecto Alternativo

Si el ejercicio 6 es muy complejo, alternativas:

1. **Sistema de Reservas de Hotel**
   - Cliente, Habitación, Reserva
   - Tipos de habitaciones (herencia)
   - Cálculo de precio (polimorfismo)

2. **Juego Simple de Rol**
   - Personaje, Enemigo, Items
   - Diferentes clases de personajes
   - Sistema de combate

3. **Sistema Académico**
   - Estudiante, Profesor, Curso
   - Diferentes tipos de evaluación
   - Cálculo de notas

---

## 📚 Recursos Adicionales para el Instructor

### Libros Recomendados
- "Python Object-Oriented Programming" - Dusty Phillips
- "Fluent Python" - Luciano Ramalho
- "Clean Code" - Robert C. Martin

### Sitios Web
- [Real Python - OOP](https://realpython.com/python3-object-oriented-programming/)
- [Python Official Docs - Classes](https://docs.python.org/3/tutorial/classes.html)

### Videos
- Buscar "Python OOP" en YouTube
- Tutoriales de Corey Schafer (altamente recomendado)

---

## 📞 Soporte y Mejoras

### Si encuentra problemas en el material:
1. Verifique la versión de Python (debe ser 3.6+)
2. Revise los comentarios en el código
3. Consulte el README de cada módulo

### Sugerencias para mejorar el material:
- Documente los cambios necesarios
- Agregue ejemplos adicionales según el contexto local
- Adapte los ejercicios al nivel del grupo

---

## ✅ Checklist de Preparación

Antes de cada sesión:

- [ ] Probar todos los ejemplos que usará
- [ ] Preparar modificaciones en vivo
- [ ] Tener ejercicios listos
- [ ] Revisar conceptos clave
- [ ] Preparar respuestas a preguntas comunes
- [ ] Tener proyector/pantalla funcionando
- [ ] Verificar que todos los estudiantes tienen Python instalado

---

## 🎯 Objetivos de Aprendizaje por Módulo

### Módulo 1
- [x] Definir qué es una clase
- [x] Crear clases con atributos y métodos
- [x] Usar `__init__` y `self` correctamente

### Módulo 2
- [x] Diferenciar agregación de composición
- [x] Implementar relaciones entre objetos
- [x] Decidir qué tipo de relación usar

### Módulo 3
- [x] Instanciar objetos de múltiples formas
- [x] Crear factory methods
- [x] Verificar tipos con isinstance

### Módulo 4
- [x] Implementar herencia correctamente
- [x] Usar super() apropiadamente
- [x] Sobrescribir métodos

### Módulo 5
- [x] Implementar polimorfismo
- [x] Crear sistemas flexibles
- [x] Aplicar duck typing

---

## 💬 Frases Clave para Recordar

> **"La clase es el molde, el objeto es la galleta"**

> **"Si puede existir solo, es agregación; si depende del contenedor, es composición"**

> **"super() es como pedirle ayuda a tu padre"**

> **"Polimorfismo: Un método, muchas formas"**

> **"En Python, si camina como pato y grazna como pato, es un pato"**

---

**¡Éxito en su labor docente! 🎓**

*Material preparado para SENA 2025*
*Curso: Python - Desarrollo Orientado a Objetos*

