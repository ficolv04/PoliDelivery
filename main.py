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

#=======================================
# SECCION: ALGORITMOS GRAFOS
#=======================================

def construir_grafo():
    
    centros = cargar_centros()
    grafo = {}
    
    for c in centros:
        grafo[c["nombre"]] = []

    # REGLA DE NEGOCIO: Para el proyecto, conectaremos centros de la misma región
    # con un costo menor, y de diferentes regiones con un costo mayor.
    for i in range(len(centros)):
        for j in range(i + 1, len(centros)):
            c1 = centros[i]
            c2 = centros[j]
            
            
            distancia = (c1["costo"] + c2["costo"]) // 2
            
            # Si son de diferente región, el envío es más caro (penalidad)
            if c1["region"] != c2["region"]:
                distancia += 50 
            
            # Añadimos la conexión bidireccional
            grafo[c1["nombre"]].append((c2["nombre"], distancia))
            grafo[c2["nombre"]].append((c1["nombre"], distancia))
            
    return grafo
import heapq # Requisito del documento: Usar Heap para optimizar Dijkstra 

def calcular_ruta_optima(inicio, destino):
    """Literal 11 y 12: Encuentra la ruta más económica usando Dijkstra."""
    grafo = construir_grafo()
    
    if inicio not in grafo or destino not in grafo:
        return None, float('inf')

    # Cola de prioridad: (costo_acumulado, nodo_actual, camino_recorrido)
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

def validar_correo(correo):
    """Verifica que el correo tenga un formato básico: algo@algo.algo"""
    if "@" in correo and "." in correo:
        # Verificamos que el punto esté después del arroba
        posicion_arroba = correo.find("@")
        posicion_punto = correo.rfind(".") # Busca el último punto
        if posicion_punto > posicion_arroba:
            return True
    return False


def registrar_cliente():
    
    # VALIDACIÓN DE CORREO
    correo_valido = False
    while not correo_valido:
        correo = input("Usuario (ejemplo@gmail.com): ")
        if validar_correo(correo):
            correo_valido = True
        else:
            print("Error: El formato del correo es inválido. Debe incluir '@' y un '.'")

    # ... (continúa con la contraseña)
def registrar_cliente():
    print("\n--- Registro de Nuevo Cliente ---")
    nombre = input("Nombres y Apellidos: ")
    cedula = input("Identificacion: ")
    
    # --- BLOQUE DE VALIDACIÓN DE EDAD ---
    edad_valida = False
    while not edad_valida:
        edad_input = input("Edad: ")
        if edad_input.isdigit(): 
            edad = int(edad_input)
            if 0 < edad < 120: 
                edad_valida = True
            else:
                print("Error: Ingrese una edad real (1-119).")
        else:
            print("Error: La edad debe ser un número. No ingrese letras.")
    

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
# ==========================================
# SECCIÓN: GESTIÓN DE CENTROS (ADMIN)
# ==========================================


def agregar_centro():
    """Permite al administrador ingresar un nuevo centro al archivo .txt"""
    print("\n--- Agregar Nuevo Centro de Distribución ---")
    nombre = input("Nombre del centro: ")
    region = input("Región (Costa/Sierra/Oriente): ")
    try:
        costo = int(input("Costo de envío base: "))
        # Guardamos en el archivo usando "a" (append) para no borrar lo anterior
        with open("centros.txt", "a") as f:
            f.write(f"{nombre},{region},{costo}\n")
        print(f"\n[Sistema] Centro '{nombre}' guardado exitosamente.")
    except ValueError:
        print("\n[!] Error: El costo debe ser un número entero.")

def consultar_centro_especifico():
    """Busca un centro por nombre usando el algoritmo de Búsqueda Binaria."""
    centros = cargar_centros()
    if not centros:
        print("\n[!] No hay centros registrados para buscar.")
        return

    # REQUISITO: La búsqueda binaria necesita la lista ordenada por nombre
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
        print("\n[!] Centro no encontrado en el sistema.")

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

def actualizar_centro():
    """Literal 16: Actualizar información de centros existentes."""
    centros = cargar_centros()
    if not centros:
        print("\n[!] No hay centros registrados para actualizar.")
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
        print("\n[!] No se encontró el centro solicitado.")

def eliminar_centro():
    """Literal 17: Eliminar centros o rutas del archivo centros.txt."""
    centros = cargar_centros()
    if not centros:
        print("\n[!] No hay centros registrados para eliminar.")
        return

    nombre_eliminar = input("\nIngrese el nombre del centro que desea eliminar: ").strip().lower()
    
    # Creamos una nueva lista EXCLUYENDO el centro que queremos borrar
    centros_restantes = [c for c in centros if c["nombre"].lower() != nombre_eliminar]

    if len(centros_restantes) < len(centros):
        # Si la lista es más pequeña, significa que sí encontramos y quitamos el centro
        with open("centros.txt", "w") as f:
            for c in centros_restantes:
                f.write(f"{c['nombre']},{c['region']},{c['costo']}\n")
        print(f"\n[Sistema] El centro '{nombre_eliminar}' ha sido eliminado exitosamente.")
    else:
        print("\n[!] No se encontró ningún centro con ese nombre.")

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
    print("7. Cerrar Sesión")


# ==========================================
# SECCIÓN: gestion del cliente 
# ==========================================
def menu_cliente():
    print("\n--- MENÚ DE CLIENTE ---")
    print("1. Ver mapa de centros")
    print("2. Consultar ruta óptima (Dijkstra)") # Agregamos esto para que sea visible
    print("7. Cerrar Sesión")

def mostrar_mapa_centros():
    
    grafo = construir_grafo()
    print("\n--- MAPA DE CENTROS Y CONEXIONES ---")
    if not grafo:
        print("[!] No hay centros registrados.")
        return
        
    for centro, conexiones in grafo.items():
        print(f"[{centro}] se conecta con:")
        for vecino, costo in conexiones:
            print(f"   -> {vecino} (Costo estimado: ${costo})")    
def consultar_ruta_cliente():
    """Literal 12: Interfaz para que el cliente consulte su envío."""
    print("\n--- Consultar Ruta de Envío Óptima ---")
    origen = input("Ciudad de origen: ")
    destino = input("Ciudad de destino: ")
    
    ruta, costo_total = calcular_ruta_optima(origen, destino)
    
    if ruta:
        print(f"\n[Éxito] Ruta encontrada: {' -> '.join(ruta)}")
        print(f"[Costo Total] ${costo_total}")
    else:
        print("\n[!] No se pudo calcular una ruta entre esas ciudades.")


# ==========================================
# SECCIÓN: EJECUCIÓN PRINCIPAL
# ==========================================

preparar_archivo_usuarios()

while True:
    mostrar_menu_principal()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        rol = iniciar_sesion()
        
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


        # MENÚ PARA CLIENTE

        elif rol == "cliente":
            while True:
                menu_cliente()
                sub_opcion = input("Seleccione una acción: ")
                if sub_opcion == "7": 
                    break
                elif sub_opcion == "1":
                    mostrar_mapa_centros() 
                elif sub_opcion == "2":
                    consultar_ruta_cliente() 

    elif opcion == "2":
        registrar_cliente()
        
    elif opcion == "3":
        print("Saliendo... ¡Hasta pronto!")
        break