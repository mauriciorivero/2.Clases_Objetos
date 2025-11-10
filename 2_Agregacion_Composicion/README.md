# Módulo 2: Agregación y Composición

## 📖 Descripción

Este módulo explica las relaciones entre objetos: agregación y composición.

## 🎯 Objetivos de Aprendizaje

Al completar este módulo, serás capaz de:
- ✅ Diferenciar entre agregación y composición
- ✅ Implementar relaciones "tiene-un"
- ✅ Decidir cuándo usar agregación vs composición
- ✅ Crear objetos complejos que contienen otros objetos

## 📁 Archivos

- `curso_estudiante.py` - Sistema de cursos con estudiantes y módulos

## 🚀 Cómo Ejecutar

```bash
python curso_estudiante.py
```

## 📚 Conceptos Cubiertos

### 1. Agregación 🔗

**Relación débil "tiene-un"**

- El objeto contenido puede existir independientemente
- Ejemplo: `Curso` tiene `Estudiantes`
- Si el curso se elimina, los estudiantes siguen existiendo

```python
# Los estudiantes existen independientemente
estudiante = Estudiante("Ana", "EST001", "ana@email.com")

# El curso solo los "reúne"
curso.inscribir_estudiante(estudiante)

# Si el curso desaparece, el estudiante sigue vivo
del curso
print(estudiante)  # ✅ Funciona
```

### 2. Composición 🔐

**Relación fuerte "es-parte-de"**

- El objeto contenido NO puede existir sin el contenedor
- Ejemplo: `Curso` tiene `Módulos`
- Si el curso se elimina, sus módulos también

```python
# Los módulos se crean DENTRO del curso
curso.agregar_modulo(
    numero=1,
    nombre="Introducción",
    duracion_horas=20,
    contenido=["tema1", "tema2"]
)

# Los módulos no existen fuera del curso
# Si el curso desaparece, sus módulos también
```

## 🔑 Diferencias Clave

| Aspecto | Agregación | Composición |
|---------|------------|-------------|
| **Relación** | Débil | Fuerte |
| **Dependencia** | Independiente | Dependiente |
| **Ciclo de vida** | Diferente | Mismo |
| **Ejemplo** | Curso ← Estudiante | Curso ← Módulo |
| **Metáfora** | Universidad tiene estudiantes | Cuerpo tiene órganos |

## 💡 Ejemplo Visual

```
AGREGACIÓN:
Curso ◇━━━━ Estudiante
       (el estudiante puede existir sin el curso)

COMPOSICIÓN:
Curso ◆━━━━ Módulo
       (el módulo no existe sin el curso)
```

## 🎓 Ejercicios Sugeridos

1. Crea una clase `Biblioteca` con `Libros` (agregación)
2. Crea una clase `Casa` con `Habitaciones` (composición)
3. Implementa un sistema `Empresa` ← `Empleados` ← `Proyectos`
4. Decide qué tipo de relación usar en cada caso

## 🔍 Puntos Clave

- **Agregación**: El objeto contenido tiene vida propia
- **Composición**: El objeto contenido depende del contenedor
- Usa **listas** para almacenar múltiples objetos relacionados
- La decisión entre agregación y composición depende del dominio del problema

