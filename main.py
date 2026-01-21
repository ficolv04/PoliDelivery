# PROYECTO FINAL: POLIDELIVERY
# Asignatura: Algoritmos y Estructuras de Datos
# Fecha: 28-01-2026
import os

# --- FUNCIONES DE SEGURIDAD (Tu Parte) ---

def preparar_archivo_usuarios():
    
    if not os.path.exists("usuarios.txt"):
        archivo = open("usuarios.txt", "w")
        archivo.write("Admin Inicial,000,99,admin@gmail.com,Admin123,administrador\n")
        archivo.close()

def validar_contrasena(password):
    tiene_minuscula = False
    tiene_mayuscula = False
    tiene_numero = False
    
    for i in range(len(password)):
        letra = password[i]
        if letra >= 'a' and letra <= 'z':
            tiene_minuscula = True
        elif letra >= 'A' and letra <= 'Z':
            tiene_mayuscula = True
        elif letra >= '0' and letra <= '9':
            tiene_numero = True
            
    if tiene_minuscula == True:
        if tiene_mayuscula == True:
            if tiene_numero == True:
                return True
    return False

def registrar_cliente():
    print("\n--- Registro de Nuevo Cliente ---")
    nombre = input("Nombres y Apellidos: ")
    cedula = input("Identificacion: ")
    edad = input("Edad: ")
    correo = input("Usuario (ejemplo@gmail.com): ")
    
    es_segura = False
    while es_segura == False:
        password = input("Contraseña segura: ")
        if validar_contrasena(password) == True:
            es_segura = True
        else:
            print("Error: La clave debe tener minusculas, mayusculas y numeros.")

    archivo = open("usuarios.txt", "a")
    archivo.write(nombre + "," + cedula + "," + edad + "," + correo + "," + password + ",cliente\n")
    archivo.close()
    print("\n[Sistema] Registro completado. Datos guardados en usuarios.txt.")

def iniciar_sesion():
    print("\n--- Inicio de Sesión ---")
    u_ingresado = input("Usuario (Correo): ")
    p_ingresado = input("Contraseña: ")
    
    try:
        archivo = open("usuarios.txt", "r")
        lineas = archivo.readlines()
        archivo.close()
        
        for i in range(len(lineas)):
            datos = lineas[i].strip().split(",")
            if datos[3] == u_ingresado and datos[4] == p_ingresado:
                print("\n¡Acceso concedido! Bienvenido " + datos[0])
                return datos[5] 
    except:
        print("Error: No se encontró la base de datos de usuarios.")
    
    print("Usuario o clave incorrectos.")
    return "ninguno"

# --- MENÚS DEL SISTEMA ---

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
    print("2. Listar centros y rutas")
    print("3. Cerrar Sesión")

def menu_cliente():
    print("\n--- MENÚ DE CLIENTE ---")
    print("1. Ver mapa de centros")
    print("2. Consultar ruta óptima")
    print("3. Cerrar Sesión")

# --- EJECUCIÓN PRINCIPAL ---

preparar_archivo_usuarios() 

while True:
    mostrar_menu_principal()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        # Usamos tu función real de login
        rol = iniciar_sesion()
        
        if rol == "administrador":
            while True:
                menu_administrador() 
                sub_opcion = input("Seleccione una acción: ")
                if sub_opcion == "3": break # Salir del menú de admin
        elif rol == "cliente":
            while True:
                menu_cliente() 
                sub_opcion = input("Seleccione una acción: ")
                if sub_opcion == "3": break

    elif opcion == "2":
        
        registrar_cliente()

    elif opcion == "3":
        print("Saliendo del sistema... ¡Gracias por usar PoliDelivery!")
        break
    else:
        print("Opción no válida. Intente de nuevo.")