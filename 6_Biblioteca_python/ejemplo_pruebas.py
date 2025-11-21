"""
Script de ejemplo para probar las APIs (Flask y FastAPI)
Este script hace solicitudes HTTP a los endpoints para demostrar su uso.

Requiere: pip install requests
"""

import requests
import json

# Configuración
FLASK_URL = "http://localhost:5000"
FASTAPI_URL = "http://localhost:8000"

# Cambiar según qué servidor quieras probar
BASE_URL = FASTAPI_URL  # o FLASK_URL


def imprimir_respuesta(titulo, response):
    """Función auxiliar para imprimir respuestas de forma legible"""
    print("\n" + "="*60)
    print(f"📋 {titulo}")
    print("="*60)
    print(f"Status Code: {response.status_code}")
    print(f"Respuesta JSON:")
    print(json.dumps(response.json(), indent=2, ensure_ascii=False))


def prueba_1_obtener_todos_los_libros():
    """GET /libros - Obtener todos los libros"""
    print("\n🔍 PRUEBA 1: Obtener todos los libros")
    response = requests.get(f"{BASE_URL}/libros")
    imprimir_respuesta("Todos los libros", response)


def prueba_2_crear_libro():
    """POST /libros - Crear un nuevo libro"""
    print("\n🔍 PRUEBA 2: Crear un nuevo libro")
    
    nuevo_libro = {
        "titulo": "Harry Potter y la Piedra Filosofal",
        "isbn": "978-0-439-70818-8",
        "autor": "J.K. Rowling",
        "anio": 1997,
        "paginas": 309,
        "disponible": True
    }
    
    response = requests.post(
        f"{BASE_URL}/libros",
        json=nuevo_libro,
        headers={"Content-Type": "application/json"}
    )
    
    imprimir_respuesta("Libro creado", response)


def prueba_3_obtener_libro_especifico():
    """GET /libros/{isbn} - Obtener un libro específico"""
    print("\n🔍 PRUEBA 3: Obtener un libro específico")
    
    isbn = "978-0-307-47472-3"  # Cien Años de Soledad
    response = requests.get(f"{BASE_URL}/libros/{isbn}")
    
    imprimir_respuesta(f"Libro con ISBN {isbn}", response)


def prueba_4_actualizar_libro():
    """PUT /libros/{isbn} - Actualizar un libro"""
    print("\n🔍 PRUEBA 4: Actualizar un libro completo")
    
    isbn = "978-0-439-70818-8"  # El libro que creamos
    
    libro_actualizado = {
        "titulo": "Harry Potter y la Piedra Filosofal (Edición Especial)",
        "isbn": isbn,
        "autor": "J.K. Rowling",
        "anio": 1997,
        "paginas": 320,
        "disponible": True
    }
    
    response = requests.put(
        f"{BASE_URL}/libros/{isbn}",
        json=libro_actualizado,
        headers={"Content-Type": "application/json"}
    )
    
    imprimir_respuesta("Libro actualizado", response)


def prueba_5_prestar_libro():
    """POST /libros/{isbn}/prestar - Prestar un libro"""
    print("\n🔍 PRUEBA 5: Prestar un libro")
    
    isbn = "978-0-439-70818-8"
    response = requests.post(f"{BASE_URL}/libros/{isbn}/prestar")
    
    imprimir_respuesta("Libro prestado", response)


def prueba_6_devolver_libro():
    """POST /libros/{isbn}/devolver - Devolver un libro"""
    print("\n🔍 PRUEBA 6: Devolver un libro")
    
    isbn = "978-0-439-70818-8"
    response = requests.post(f"{BASE_URL}/libros/{isbn}/devolver")
    
    imprimir_respuesta("Libro devuelto", response)


def prueba_7_eliminar_libro():
    """DELETE /libros/{isbn} - Eliminar un libro"""
    print("\n🔍 PRUEBA 7: Eliminar un libro")
    
    isbn = "978-0-439-70818-8"
    response = requests.delete(f"{BASE_URL}/libros/{isbn}")
    
    imprimir_respuesta("Libro eliminado", response)


def prueba_8_libro_no_encontrado():
    """Probar error 404"""
    print("\n🔍 PRUEBA 8: Intentar obtener un libro que no existe")
    
    isbn = "999-9-999-99999-9"
    response = requests.get(f"{BASE_URL}/libros/{isbn}")
    
    imprimir_respuesta("Error esperado (404)", response)


def prueba_9_crear_libro_invalido():
    """Probar validación de datos"""
    print("\n🔍 PRUEBA 9: Intentar crear un libro con datos inválidos")
    
    # Falta el campo 'titulo'
    libro_invalido = {
        "isbn": "978-1-111-11111-1",
        "autor": "Autor Desconocido",
        "anio": 2023
        # Faltan: titulo, paginas, disponible
    }
    
    response = requests.post(
        f"{BASE_URL}/libros",
        json=libro_invalido,
        headers={"Content-Type": "application/json"}
    )
    
    imprimir_respuesta("Error esperado (validación)", response)


def menu_principal():
    """Menú interactivo para ejecutar pruebas"""
    print("\n" + "="*60)
    print("🧪 SCRIPT DE PRUEBAS - API DE BIBLIOTECA")
    print("="*60)
    print(f"🌐 Servidor: {BASE_URL}")
    print("="*60)
    print("\nOpciones:")
    print("1. Obtener todos los libros")
    print("2. Crear un nuevo libro")
    print("3. Obtener un libro específico")
    print("4. Actualizar un libro")
    print("5. Prestar un libro")
    print("6. Devolver un libro")
    print("7. Eliminar un libro")
    print("8. Probar error 404 (libro no encontrado)")
    print("9. Probar validación (datos inválidos)")
    print("0. Ejecutar todas las pruebas")
    print("q. Salir")
    print("="*60)


def ejecutar_todas_las_pruebas():
    """Ejecuta todas las pruebas en secuencia"""
    print("\n🚀 Ejecutando todas las pruebas...")
    
    try:
        prueba_1_obtener_todos_los_libros()
        input("\n▶️  Presiona Enter para continuar...")
        
        prueba_2_crear_libro()
        input("\n▶️  Presiona Enter para continuar...")
        
        prueba_3_obtener_libro_especifico()
        input("\n▶️  Presiona Enter para continuar...")
        
        prueba_4_actualizar_libro()
        input("\n▶️  Presiona Enter para continuar...")
        
        prueba_5_prestar_libro()
        input("\n▶️  Presiona Enter para continuar...")
        
        prueba_6_devolver_libro()
        input("\n▶️  Presiona Enter para continuar...")
        
        prueba_7_eliminar_libro()
        input("\n▶️  Presiona Enter para continuar...")
        
        prueba_8_libro_no_encontrado()
        input("\n▶️  Presiona Enter para continuar...")
        
        prueba_9_crear_libro_invalido()
        
        print("\n✅ Todas las pruebas completadas!")
        
    except requests.exceptions.ConnectionError:
        print("\n❌ Error: No se pudo conectar al servidor")
        print(f"   Verifica que el servidor esté corriendo en {BASE_URL}")
        print("\n   Para Flask: python app_flask.py")
        print("   Para FastAPI: uvicorn app_fastapi:app --reload")


def main():
    """Función principal"""
    pruebas = {
        "1": prueba_1_obtener_todos_los_libros,
        "2": prueba_2_crear_libro,
        "3": prueba_3_obtener_libro_especifico,
        "4": prueba_4_actualizar_libro,
        "5": prueba_5_prestar_libro,
        "6": prueba_6_devolver_libro,
        "7": prueba_7_eliminar_libro,
        "8": prueba_8_libro_no_encontrado,
        "9": prueba_9_crear_libro_invalido,
        "0": ejecutar_todas_las_pruebas
    }
    
    while True:
        menu_principal()
        opcion = input("\n👉 Elige una opción: ").strip().lower()
        
        if opcion == 'q':
            print("\n👋 ¡Hasta luego!\n")
            break
        
        if opcion in pruebas:
            try:
                pruebas[opcion]()
                
                if opcion != "0":
                    input("\n▶️  Presiona Enter para volver al menú...")
            
            except requests.exceptions.ConnectionError:
                print("\n❌ Error: No se pudo conectar al servidor")
                print(f"   Verifica que el servidor esté corriendo en {BASE_URL}")
                print("\n   Para Flask: python app_flask.py")
                print("   Para FastAPI: uvicorn app_fastapi:app --reload")
                input("\n▶️  Presiona Enter para volver al menú...")
            
            except Exception as e:
                print(f"\n❌ Error inesperado: {str(e)}")
                input("\n▶️  Presiona Enter para volver al menú...")
        else:
            print("\n❌ Opción inválida")
            input("\n▶️  Presiona Enter para continuar...")


if __name__ == "__main__":
    # Verificar que requests esté instalado
    try:
        import requests
    except ImportError:
        print("\n❌ Error: El módulo 'requests' no está instalado")
        print("   Instálalo con: pip install requests\n")
        exit(1)
    
    # Ejecutar el programa
    main()

