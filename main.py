# PROYECTO FINAL: POLIDELIVERY
# Asignatura: Algoritmos y Estructuras de Datos
# Fecha: 28-01-2026

def mostrar_menu_principal():
    print("\n" + "="*30)
    print("   SISTEMA POLIDELIVERY")
    print("="*30)
    print("1. Iniciar Sesión (Cliente / Admin)")
    print("2. Registrarse (Solo Clientes)")
    print("3. Salir")
    print("-" * 30)

def menu_administrador():
    print("\n--- PANEL DE ADMINISTRADOR ---")
    print("1. Agregar centros o rutas")
    print("2. Listar centros y rutas (Ordenamiento)")
    print("3. Consultar centro específico (Búsqueda)")
    print("4. Actualizar información")
    print("5. Eliminar centros o rutas")
    print("6. Guardar cambios en centros.txt")
    print("7. Cerrar Sesión")

def menu_cliente():
    print("\n--- MENÚ DE CLIENTE ---")
    print("1. Ver mapa de centros")
    print("2. Consultar ruta óptima (Dijkstra)")
    print("3. Explorar centros por regiones (Árboles)")
    print("4. Seleccionar centros para envío")
    print("5. Ver mi selección y costo total")
    print("6. Guardar ruta en archivo")
    print("7. Cerrar Sesión")

# Bucle principal de ejecución
while True:
    mostrar_menu_principal()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("\n--- Inicio de Sesión ---")
        usuario = input("Usuario: ")
        # Aquí irá la lógica de validación con usuarios.txt 
        
        # Simulación de entrada a roles
        if "admin" in usuario:
            while True:
                menu_administrador() 
                sub_opcion = input("Seleccione una acción: ")
                if sub_opcion == "7": break
        else:
            while True:
                menu_cliente() 
                sub_opcion = input("Seleccione una acción: ")
                if sub_opcion == "7": break

    elif opcion == "2":
        print("\n--- Registro de Nuevo Cliente ---")
        # Datos requeridos por el sistema 
        nombre = input("Nombres y Apellidos: ")
        cedula = input("Identificación: ")
        edad = input("Edad: ")
        correo = input("Usuario (ejemplo@gmail.com): ")
        password = input("Contraseña segura: ")
        print("\n[Sistema] Registro completado. Datos guardados en usuarios.txt.")

    elif opcion == "3":
        print("Saliendo del sistema... ¡Gracias por usar PoliDelivery!")
        break
    else:
        print("Opción no válida. Intente de nuevo.")