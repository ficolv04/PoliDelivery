import os
from logic.ordenamiento import ordenar_burbuja, quick_sort
from utils.seguridad import validar_contrasena
from utils.persistencia import preparar_archivo_usuarios, cargar_centros

# --- FUNCIONES DE SESIÓN Y REGISTRO ---

def registrar_cliente():
    print("\n--- Registro de Nuevo Cliente ---")
    nombre = input("Nombres y Apellidos: ")
    cedula = input("Identificacion: ")
    edad = input("Edad: ")
    correo = input("Usuario (ejemplo@gmail.com): ")
    
    es_segura = False
    while not es_segura:
        password = input("Contraseña segura: ")
        if validar_contrasena(password):
            es_segura = True
        else:
            print("Error: La clave debe tener minusculas, mayusculas y numeros.")

    with open("usuarios.txt", "a") as archivo:
        archivo.write(f"{nombre},{cedula},{edad},{correo},{password},cliente\n")
    print("\n[Sistema] Registro completado. Datos guardados en usuarios.txt.")

def iniciar_sesion():
    print("\n--- Inicio de Sesión ---")
    u_ingresado = input("Usuario (Correo): ")
    p_ingresado = input("Contraseña: ")
    
    try:
        with open("usuarios.txt", "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                if datos[3] == u_ingresado and datos[4] == p_ingresado:
                    print(f"\n¡Acceso concedido! Bienvenido {datos[0]}")
                    return datos[5] 
    except FileNotFoundError:
        print("Error: No se encontró la base de datos de usuarios.")
    
    print("Usuario o clave incorrectos.")
    return "ninguno"

def listar_centros_admin():
    centros = cargar_centros()
    if not centros:
        print("\n[!] No hay centros registrados.")
        return

    print("\n1. Ordenar por Nombre (Burbuja)\n2. Ordenar por Costo (Quick Sort)")
    metodo = input("Seleccione método: ")

    if metodo == "1":
        centros = ordenar_burbuja(centros, "nombre")
    elif metodo == "2":
        centros = quick_sort(centros, "costo")

    print("\nID | NOMBRE       | REGION     | COSTO")
    for i, c in enumerate(centros):
        print(f"{i+1:<2} | {c['nombre']:<12} | {c['region']:<10} | {c['costo']}")

# --- MENÚS ---

def mostrar_menu_principal():
    print("\n" + "="*30 + "\n   SISTEMA POLIDELIVERY\n" + "="*30)
    print("1. Iniciar Sesión\n2. Registrarse\n3. Salir\n" + "-"*30)

def menu_administrador():
    print("\n--- PANEL DE ADMINISTRADOR ---")
    print("1. Agregar centros\n2. Listar centros\n7. Cerrar Sesión")

def menu_cliente():
    print("\n--- MENÚ DE CLIENTE ---")
    print("1. Ver mapa\n7. Cerrar Sesión")

# --- EJECUCIÓN PRINCIPAL ---
preparar_archivo_usuarios()

while True:
    mostrar_menu_principal()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        rol = iniciar_sesion()
        if rol == "administrador":
            while True:
                menu_administrador()
                if input("Seleccione: ") == "7": break
                elif opcion == "2": listar_centros_admin()
        elif rol == "cliente":
            while True:
                menu_cliente()
                if input("Seleccione: ") == "7": break
    elif opcion == "2":
        registrar_cliente()
    elif opcion == "3":
        break