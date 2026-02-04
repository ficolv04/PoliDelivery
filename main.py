# PROYECTO FINAL: POLIDELIVERY
# Asignatura: Algoritmos y Estructuras de Datos
# Fecha: 2026- 02- 04

import os
import heapq # Requisito: Heap para Dijkstra 
from collections import deque # Para BFS

def preparar_archivo_usuarios():
    if (not os.path.exists("usuarios.txt")) or (os.path.getsize("usuarios.txt") == 0):
        with open("usuarios.txt", "w") as archivo:
            archivo.write("Admin Inicial,000,99,admin@gmail.com,Admin123,administrador\n")

# ==========================================
# SECCIÓN: ESTRUCTURAS DE DATOS (Árboles y Grafos)
# ==========================================

class NodoArbol:
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.hijos = []

# ==========================================
# SECCIÓN: ALGORITMOS DE BÚSQUEDA (BFS/DFS)
# ==========================================

def bfs_centros_cercanos(grafo, inicio):
    if inicio not in grafo:
        print("Error: Centro inicial no existe.")
        return

    visitados = set([inicio])
    cola = deque([inicio])
    print(f"\nCentros cercanos a {inicio}:")
    while cola:
        actual = cola.popleft()
        for vecino, costo in grafo.get(actual, []):
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append(vecino)
                print(f" -> {vecino}")


def dfs_exploracion_completa(grafo, inicio, visitados=None):
    
    if inicio not in grafo:
        print("Error: Centro inicial no existe.")
        return

    if visitados is None: visitados = set()
    visitados.add(inicio)
    print(f"Visitando: {inicio}")
    for vecino, costo in grafo.get(inicio, []):
        if vecino not in visitados:
            dfs_exploracion_completa(grafo, vecino, visitados)


#=======================================
# SECCION: ALGORITMOS GRAFOS
#=======================================

def construir_grafo():
    
    centros = cargar_centros()
    grafo = {}
    
    for c in centros:
        grafo[c["nombre"]] = []

    for i in range(len(centros)):
        for j in range(i + 1, len(centros)):
            c1 = centros[i]
            c2 = centros[j]
            
            
            distancia = (c1["costo"] + c2["costo"]) // 2
            
            if c1["region"] != c2["region"]:
                distancia += 50 
            
            grafo[c1["nombre"]].append((c2["nombre"], distancia))
            grafo[c2["nombre"]].append((c1["nombre"], distancia))
            
    return grafo

def calcular_ruta_optima(inicio, destino):
    grafo = construir_grafo()
    
    if inicio not in grafo or destino not in grafo:
        return None, float('inf')

    cola_prioridad = [(0, inicio, [])]
    visitados = set()

    while cola_prioridad:
        (costo, actual, camino) = heapq.heappop(cola_prioridad)

        if actual in visitados:
            continue

        camino = camino + [actual]
        visitados.add(actual)

        if actual == destino:
            return camino, costo

        for (vecino, peso) in grafo.get(actual, []):
            if vecino not in visitados:
                heapq.heappush(cola_prioridad, (costo + peso, vecino, camino))

    return None, float('inf')


# ==========================================
# SECCIÓN: ALGORITMOS DE ORDENAMIENTO
# ==========================================

def ordenar_burbuja(lista, llave):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if str(lista[j][llave]).lower() > str(lista[j + 1][llave]).lower():
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

def validar_correo(correo):

    if "@" in correo and "." in correo:
        posicion_arroba = correo.find("@")
        posicion_punto = correo.rfind(".")
        if posicion_punto > posicion_arroba:
            return True
    return False

def correo_ya_existe(correo):

    if not os.path.exists("usuarios.txt"):
        return False
    
    with open("usuarios.txt", "r") as archivo:
        for linea in archivo:
            datos = linea.strip().split(",")
            if len(datos) >= 4:
                if datos[3].lower() == correo.lower():
                    return True
    return False

def registrar_cliente():
    print("\n--- Registro de Nuevo Cliente ---")
    
    nombre_valido = False
    while not nombre_valido:
        nombre = input("Nombres y Apellidos: ").strip()
        
        if not nombre:
            print("Error: El nombre no puede estar vacío.")
            continue 

        tiene_numero = False
        for caracter in nombre:
            if caracter.isdigit(): # Revisa si el caracter es un número
                tiene_numero = True
                break 
        
        if tiene_numero:
            print("Error: El nombre no puede contener números.")
        else:
            nombre_valido = True 
    
    # Validación de Identificación (Cédula)
    cedula_valida = False
    while not cedula_valida:
        cedula = input("Identificacion (solo números): ")
        if cedula.isdigit() and len(cedula) == 10:
            cedula_valida = True
        else:
            print("Error: La identificación debe tener 10 dígitos numéricos.")

    # Validación de Edad
    edad_valida = False
    while not edad_valida:
        edad_input = input("Edad: ")
        if edad_input.isdigit(): 
            edad = int(edad_input)
            if 0 < edad < 120: 
                edad_valida = True
            else:
                print("Error: Ingrese una edad real .")
        else:
            print("Error: La edad debe ser un número.")

    # VALIDACIÓN DE CORREO
    correo_valido = False
    while not correo_valido:
        correo = input("Usuario (ejemplo@gmail.com): ").strip()
        
        if not validar_correo(correo):
            print("Error: El formato del correo es inválido. Debe incluir '@' y un '.'")
        elif correo_ya_existe(correo):
            print(f"Error: El correo '{correo}' ya está registrado. Intente con otro.")
        else:
            correo_valido = True

    # Validación de Contraseña
    def validar_contrasena(password):
    
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
        
    es_segura = False
    while not es_segura:
        password = input("Contraseña segura: ")
        if validar_contrasena(password):
            es_segura = True
        else:
            print("Error: La clave debe tener minúsculas, mayúsculas y números.")

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
                if len(datos) >= 6:
                    if datos[3] == u_ingresado and datos[4] == p_ingresado:
                        print(f"\n¡Acceso concedido! Bienvenido {datos[0]}")
                        return datos[5] ,datos[0]
    except Exception as e:
        print(f"Error al leer la base de datos: {e}")
    
    print("Usuario o clave incorrectos.")
    return "ninguno" , None

# ==========================================
# SECCIÓN: GESTIÓN DE CENTROS (ADMIN)
# ==========================================

def mostrar_menu_principal():
    print("\n" + "="*30)
    print("   SISTEMA POLIDELIVERY")
    print("="*30)
    print("1. Iniciar Sesión\n2. Registrarse\n3. Salir")
    print("-" * 30)

def menu_administrador():
    print("\n--- PANEL DE ADMINISTRADOR ---")
    print("1. Agregar centros")
    print("2. Listar centros (Ordenamiento)")
    print("3. Consultar centro específico (Búsqueda Binaria)") # Requisito Literal 16
    print("4. Actualizar información") # Requisito Literal 16
    print("5. Eliminar centros") # Requisito Literal 17
    print("6. Mostrar la matriz de costos ")
    print("7. Cerrar Sesión")

def agregar_centro():
    
    print("\n--- Agregar Nuevo Centro de Distribución ---")
    nombre = input("Nombre del centro: ").lower()
    region = input("Región (Costa/Sierra/Oriente): ").strip().capitalize()


    centros = cargar_centros()
    for c in centros:
        if c["nombre"].lower() == nombre.lower():
            print(" Error: El centro ya existe.")
            return
        
    try:
        costo = int(input("Costo de envío base: "))
        # Guardamos en el archivo usando "a" (append) para no borrar lo anterior
        with open("centros.txt", "a") as f:
            f.write(f"{nombre},{region},{costo}\n")
        print(f"\n[Sistema] Centro '{nombre}' guardado exitosamente.")
    except ValueError:
        print("\nError: El costo debe ser un número entero.")
def listar_centros_admin():
    centros = cargar_centros()
    if not centros:
        print("\n No hay centros registrados en centros.txt.")
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

def consultar_centro_especifico():
    centros = cargar_centros()
    if not centros:
        print("\n No hay centros registrados para buscar.")
        return
    centros_ordenados = ordenar_burbuja(centros, "nombre")
    nombre_buscado = input("\nIngrese el nombre del centro a buscar: ").strip().lower()

    izq = 0
    der = len(centros_ordenados) - 1
    encontrado = None

    while izq <= der:
        medio = (izq + der) // 2
        nombre_actual = centros_ordenados[medio]["nombre"].lower()
        
        if nombre_actual == nombre_buscado:
            encontrado = centros_ordenados[medio]
            break
        elif nombre_actual < nombre_buscado:
            izq = medio + 1
        else:
            der = medio - 1

    if encontrado:
        print(f"\n[Resultado] Centro: {encontrado['nombre']} | Región: {encontrado['region']} | Costo: ${encontrado['costo']}")
    else:
        print("\n Centro no encontrado en el sistema.")


def actualizar_centro():
    centros = cargar_centros()
    if not centros:
        print("\n No hay centros registrados para actualizar.")
        return

    nombre_buscado = input("\nIngrese el nombre del centro que desea actualizar: ").strip().lower()
    encontrado = False

    for centro in centros:
        if centro["nombre"].lower() == nombre_buscado:
            print(f"\nDatos actuales - Región: {centro['region']}, Costo: {centro['costo']}")
            
            # Pedimos los nuevos datos
            nuevo_nombre = input("Nuevo nombre (deje vacío para no cambiar): ")
            nueva_region = input("Nueva región (deje vacío para no cambiar): ")
            nuevo_costo = input("Nuevo costo (deje vacío para no cambiar): ")

            # Actualizamos solo si el usuario ingresó algo
            if nuevo_nombre: centro["nombre"] = nuevo_nombre
            if nueva_region: centro["region"] = nueva_region
            if nuevo_costo: centro["costo"] = int(nuevo_costo)
            
            encontrado = True
            break    

    if encontrado:
        # Guardamos toda la lista actualizada en el archivo (modo 'w' para sobrescribir)
        with open("centros.txt", "w") as f:
            for c in centros:
                f.write(f"{c['nombre']},{c['region']},{c['costo']}\n")
        print("\n[Sistema] Información actualizada correctamente en centros.txt.")
    else:
        print("\n No se encontró el centro solicitado.")

def eliminar_centro():
    centros = cargar_centros()
    if not centros:
        print("\n No hay centros registrados para eliminar.")
        return

    nombre_eliminar = input("\nIngrese el nombre del centro que desea eliminar: ").strip().lower()
    
    centros_restantes = []

    for c in centros:
        nombre_centro = c["nombre"].strip().lower()
        nombre_a_eliminar = nombre_eliminar.strip().lower()

        if nombre_centro != nombre_a_eliminar:
            centros_restantes.append(c)

    if len(centros_restantes) < len(centros):
        with open("centros.txt", "w") as f:
            for c in centros_restantes:
                f.write(f"{c['nombre']},{c['region']},{c['costo']}\n")
        print(f"\n[Sistema] El centro '{nombre_eliminar}' ha sido eliminado exitosamente.")
    else:
        print("\n No se encontró ningún centro con ese nombre.")

def mostrar_matriz_costos():

    grafo = construir_grafo()
    centros = list(grafo.keys())

    print("\n--- MATRIZ DE COSTOS ---")
    print(" " * 15, end="")
    for c in centros:
        print(f"{c[:10]:>12}", end="")
    print()

    for c1 in centros:
        print(f"{c1[:12]:<12}", end=" ")
        for c2 in centros:
            if c1 == c2:
                print(f"{0:>12}", end="")
            else:
                costo = next((c for v, c in grafo[c1] if v == c2), "-")
                print(f"{costo:>12}", end="")
        print()


# ==========================================
# SECCIÓN: gestion del cliente 
# ==========================================

def mostrar_mapa_centros():
    
    grafo = construir_grafo()
    print("\n--- MAPA DE CENTROS Y CONEXIONES ---")
    if not grafo:
        print(" No hay centros registrados.")
        return
        
    for centro, conexiones in grafo.items():
        print(f"[{centro}] se conecta con:")
        for vecino, costo in conexiones:
            print(f"   -> {vecino} (Costo estimado: ${costo})")    

def consultar_ruta_cliente():
    print("\n--- Consultar Ruta de Envío Óptima ---")
    
    origen = input("Ciudad de origen: ").strip()
    destino = input("Ciudad de destino: ").strip()

    
    ruta, costo_total = calcular_ruta_optima(origen, destino)
    
    if ruta:
        print(f"\n[Éxito] Ruta encontrada: {' -> '.join(ruta)}")
        print(f"[Costo Total] ${costo_total}")
    else:
        print("\n No se pudo calcular una ruta entre esas ciudades.")

    
def construir_arbol_regiones(centros):
    
    raiz = NodoArbol("PoliDelivery - Ecuador")
    regiones = {}
    for c in centros:
        reg = c["region"]
        if reg not in regiones:
            regiones[reg] = NodoArbol(reg)
            raiz.hijos.append(regiones[reg])
        regiones[reg].hijos.append(NodoArbol(c["nombre"]))
    return raiz
def cargar_centros():
    centros = []
    if os.path.exists("centros.txt"):
        with open("centros.txt", "r") as f:
            for linea in f:
                datos = linea.strip().split(",")
                if len(datos) == 3:
                    try:
                        costo = int(datos[2])
                    except ValueError:
                        continue

                    centros.append({
                        "nombre": datos[0],
                        "region": datos[1].strip().capitalize(),
                        "costo": costo
                    })

    return centros
def explorar_arbol_recursivo(nodo, nivel=0):
    
    print("  " * nivel + "|-- " + nodo.nombre)
    for hijo in nodo.hijos:
        explorar_arbol_recursivo(hijo, nivel + 1)

envio_actual = [] 

def gestionar_envio_cliente(nombre_cliente):
    global envio_actual
    while True:
        print("\n--- GESTIÓN DE MI ENVÍO -  --")
        print("1. Seleccionar centros (min 2)\n2. Listar y Ordenar selección\n3. Eliminar centros seleccionados\n4. Guardar y Salir")
        op = input("Seleccione: ")
        
        if op == "1":
            centros = cargar_centros()

            if not centros:
                print("No hay centros registrados.")
                continue

            for i, c in enumerate(centros):
                print(f"{i}. {c['nombre']}")

            idx_txt = input("Ingrese el ID del centro a añadir: ").strip()
            if not idx_txt.isdigit():
                print("Error: Debe ingresar un numero.")
                continue

            idx = int(idx_txt)
            if idx < 0 or idx >= len(centros):
                print("Error: ID fuera de rango.")
                continue

            envio_actual.append(centros[idx])
        elif op == "2":
            if not envio_actual: print("Vacío."); continue
            print("\n1. Ordenar por Nombre\n2. Ordenar por Costo")
            met = input("Método: ").strip()
            if met == "1":
                envio_actual = quick_sort(envio_actual, "nombre")
            elif met == "2":
                envio_actual = quick_sort(envio_actual, "costo")
            else:
                print("Opción inválida.")
                continue

        
        elif op == "3":
            envio_actual = []
            print("Selección eliminada.")
            
        elif op == "4":
            if len(envio_actual) < 2:
                print("Error: Debe seleccionar mínimo dos centros.")
            else:
                filename = f"rutas-{nombre_cliente.replace(' ', '-')}.txt"
                total = sum(c["costo"] for c in envio_actual)

                with open(filename, "w") as f:
                    f.write(f"Envío de: {nombre_cliente}\n")
                    for c in envio_actual:
                        f.write(f"{c['nombre']},{c['region']},{c['costo']}\n")
                    f.write(f"COSTO TOTAL: ${total}\n")
                    
                print(f"Guardado en {filename}")
                break

def menu_cliente_completo(nombre_cliente):
    while True:
        print(f"\n--- MENÚ DE CLIENTE: {nombre_cliente} ---")
        print("1. Ver mapa de centros")             
        print("2. Consultar ruta óptima (Dijkstra)")
        print("3. Explorar Jerarquía (Árboles)")    
        print("4. Gestionar Carrito de Envío")      
        print("5. Ver centros cercanos (BFS)")      
        print("6. Explorar rutas completas (DFS)")  
        print("7. Cerrar Sesión")

        sub = input("Seleccione una opción: ")
        if sub == "7":
            break
        # Lógica de procesamiento de opciones...
        sub = input("Seleccione: ")

        if sub == "7":
            break
        elif sub == "1":
            mostrar_mapa_centros()
        elif sub == "2":
            consultar_ruta_cliente()
        elif sub == "3":
            arbol = construir_arbol_regiones(cargar_centros())
            explorar_arbol_recursivo(arbol)
        elif sub == "4":
            gestionar_envio_cliente(nombre_cliente)
        
        elif sub == "5":
            inicio = input("Centro inicial: ")
            bfs_centros_cercanos(construir_grafo(), inicio)

        elif sub == "6":
            inicio = input("Centro inicial: ")
            dfs_exploracion_completa(construir_grafo(), inicio)

        else:
            print("Opción inválida.")

# ==========================================
# SECCIÓN: EJECUCIÓN PRINCIPAL
# ==========================================

preparar_archivo_usuarios()

while True:
    mostrar_menu_principal()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        rol,nombre_u = iniciar_sesion()
        
        # MENÚ PARA ADMINISTRADOR
        if rol == "administrador":
            while True:
                menu_administrador()
                sub_opcion = input("Seleccione una acción: ")
                if sub_opcion == "7": 
                    break
                elif sub_opcion == "1":
                    agregar_centro() 
                elif sub_opcion == "2":
                    listar_centros_admin() 
                elif sub_opcion == "3":
                    consultar_centro_especifico() 
                elif sub_opcion == "4":
                    actualizar_centro() 
                elif sub_opcion == "5":
                    eliminar_centro()
                elif sub_opcion == "6":
                    mostrar_matriz_costos()



        # MENÚ PARA CLIENTE

        elif rol == "cliente":
            menu_cliente_completo(nombre_u)

    elif opcion == "2":
        registrar_cliente()
        
    elif opcion == "3":
        print("Saliendo... ¡Hasta pronto!")
        break