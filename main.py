# PROYECTO FINAL: POLIDELIVERY
# Asignatura: Algoritmos y Estructuras de Datos
# Fecha: 2026-01-31

import os

# ==========================================
# SECCIÓN: PERSISTENCIA (Manejo de Archivos)
# ==========================================

def preparar_archivo_usuarios():
    """Crea el archivo de usuarios con un administrador inicial si no existe."""
    if not os.path.exists("usuarios.txt"):
        with open("usuarios.txt", "w") as archivo:
            archivo.write("Admin Inicial,000,99,admin@gmail.com,Admin123,administrador\n")
    # Nota: Si el archivo existe pero está vacío, el administrador no estará. 
    # Asegúrate de borrar el .txt si quieres que se cree de nuevo.

def cargar_centros():
    """Lee los centros desde centros.txt y los retorna como una lista de diccionarios."""
    centros = []
    if os.path.exists("centros.txt"):
        with open("centros.txt", "r") as f:
            for linea in f:
                datos = linea.strip().split(",")
                if len(datos) == 3:
                    centros.append({
                        "nombre": datos[0],
                        "region": datos[1],
                        "costo": int(datos[2])
                    })
    return centros

# ==========================================
# SECCIÓN: SEGURIDAD
# ==========================================

def validar_contrasena(password):
    """Valida que la clave tenga minúsculas, mayúsculas y números."""
    tiene_minuscula = False
    tiene_mayuscula = False
    tiene_numero = False
    
    for letra in password:
        if 'a' <= letra <= 'z':
            tiene_minuscula = True
        elif 'A' <= letra <= 'Z':
            tiene_mayuscula = True
        elif '0' <= letra <= '9':
            tiene_numero = True
            
    return tiene_minuscula and tiene_mayuscula and tiene_numero

# ==========================================
# SECCIÓN: ALGORITMOS DE ORDENAMIENTO
# ==========================================

def ordenar_burbuja(lista, llave):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j][llave] > lista[j + 1][llave]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def quick_sort(lista, llave):
    if len(lista) <= 1:
        return lista
    pivote = lista[len(lista) // 2][llave]
    izquierda = [x for x in lista if x[llave] < pivote]
    centro = [x for x in lista if x[llave] == pivote]
    derecha = [x for x in lista if x[llave] > pivote]
    return quick_sort(izquierda, llave) + centro + quick_sort(derecha, llave)

# ==========================================
# SECCIÓN: FUNCIONES DE SESIÓN Y REGISTRO
# ==========================================

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
        if not os.path.exists("usuarios.txt"):
            print("Error: El archivo de usuarios no existe.")
            return "ninguno"
            
        with open("usuarios.txt", "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                # Comparación exacta de correo (índice 3) y clave (índice 4)
                if len(datos) >= 6:
                    if datos[3] == u_ingresado and datos[4] == p_ingresado:
                        print(f"\n¡Acceso concedido! Bienvenido {datos[0]}")
                        return datos[5] # Retorna el rol: 'administrador' o 'cliente'
    except Exception as e:
        print(f"Error al leer la base de datos: {e}")
    
    print("Usuario o clave incorrectos.")
    return "ninguno"

# ==========================================
# SECCIÓN: MENÚS Y VISTAS
# ==========================================

def listar_centros_admin():
    centros = cargar_centros()
    if not centros:
        print("\n[!] No hay centros registrados en centros.txt.")
        return

    print("\n1. Ordenar por Nombre (Burbuja)")
    print("2. Ordenar por Costo (Quick Sort)")
    metodo = input("Seleccione método: ")

    if metodo == "1":
        centros = ordenar_burbuja(centros, "nombre")
    elif metodo == "2":
        centros = quick_sort(centros, "costo")
    else:
        print("Opción inválida.")
        return

    print("\nID | NOMBRE       | REGION     | COSTO")
    print("-" * 40)
    for i, c in enumerate(centros):
        print(f"{i+1:<2} | {c['nombre']:<12} | {c['region']:<10} | {c['costo']}")

def mostrar_menu_principal():
    print("\n" + "="*30)
    print("   SISTEMA POLIDELIVERY")
    print("="*30)
    print("1. Iniciar Sesión\n2. Registrarse\n3. Salir")
    print("-" * 30)

def menu_administrador():
    print("\n--- PANEL DE ADMINISTRADOR ---")
    print("1. Agregar centros\n2. Listar centros\n7. Cerrar Sesión")

def menu_cliente():
    print("\n--- MENÚ DE CLIENTE ---")
    print("1. Ver mapa\n7. Cerrar Sesión")

# ==========================================
# SECCIÓN: EJECUCIÓN PRINCIPAL
# ==========================================

preparar_archivo_usuarios()

while True:
    mostrar_menu_principal()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        rol = iniciar_sesion()
        
        if rol == "administrador":
            while True:
                menu_administrador()
                sub_opcion = input("Seleccione una acción: ")
                if sub_opcion == "7": 
                    break
                elif sub_opcion == "1":
                    print("Lógica para agregar centros... (Pendiente)")
                elif sub_opcion == "2":
                    listar_centros_admin()

        elif rol == "cliente":
            while True:
                menu_cliente()
                sub_opcion = input("Seleccione una acción: ")
                if sub_opcion == "7": 
                    break
                elif sub_opcion == "1":
                    print("Mostrando mapa... (Pendiente)")

    elif opcion == "2":
        registrar_cliente()
    elif opcion == "3":
        print("Saliendo... ¡Hasta pronto!")
        break