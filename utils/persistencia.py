import os

def preparar_archivo_usuarios():
    
    if not os.path.exists("usuarios.txt"):
        archivo = open("usuarios.txt", "w")
        archivo.write("Admin Inicial,000,99,admin@gmail.com,Admin123,administrador\n")
        archivo.close()

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
