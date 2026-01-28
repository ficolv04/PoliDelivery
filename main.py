# PROYECTO FINAL: POLIDELIVERY
# Asignatura: Algoritmos y Estructuras de Datos
# Fecha: 28-01-2026

import os

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

def cargar_centros():
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

# Algoritmo de Burbuja 
def ordenar_burbuja(lista, llave):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j][llave] > lista[j + 1][llave]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Algoritmo Quick Sort 
def quick_sort(lista, llave):
    if len(lista) <= 1:
        return lista
    pivote = lista[len(lista) // 2][llave]
    izquierda = [x for x in lista if x[llave] < pivote]
    centro = [x for x in lista if x[llave] == pivote]
    derecha = [x for x in lista if x[llave] > pivote]
    return quick_sort(izquierda, llave) + centro + quick_sort(derecha, llave)

def listar_centros_admin():
    centros = cargar_centros()
    if not centros:
        print("\n[!] No hay centros registrados en centros.txt.")
        return

    print("\n--- Listar Centros ---")
    print("1. Ordenar por Nombre (Burbuja)")
    print("2. Ordenar por Costo/Distancia (Quick Sort)")
    metodo = input("Seleccione método: ")

    if metodo == "1":
        centros_ordenados = ordenar_burbuja(centros, "nombre")
    elif metodo == "2":
        centros_ordenados = quick_sort(centros, "costo")
    else:
        print("Opción no válida.")
        return

    print("\nID | NOMBRE       | REGION     | COSTO/DIST")
    print("-" * 45)
    for i, c in enumerate(centros_ordenados):
        print(f"{i+1:<2} | {c['nombre']:<12} | {c['region']:<10} | {c['costo']}")
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
        rol = iniciar_sesion()
        if rol == "administrador":
            while True:
                menu_administrador()
                sub_opcion = input("Seleccione una acción: ")
                
                if sub_opcion == "1":
                    print("Lógica para agregar centros...")
                elif sub_opcion == "2":
                    listar_centros_admin() # <--- Aquí llamas al Literal 2
                elif sub_opcion == "7":
                    break
        elif rol == "cliente":
            while True:
                menu_cliente()
                sub_opcion = input("Seleccione una acción: ")
                if sub_opcion == "7": break
                # Aquí irán las llamadas a funciones de cliente

    elif opcion == "2":
        registrar_cliente()
