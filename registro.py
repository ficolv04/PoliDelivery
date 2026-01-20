def validar_contrasena(password):
    tiene_minuscula = False
    tiene_mayuscula = False
    tiene_numero = False
    
    for letra in password:
        if letra.islower():   
            tiene_minuscula = True
        if letra.isupper():   
            tiene_mayuscula = True
        if letra.isdigit():   
            tiene_numero = True
            
   
    if tiene_minuscula == True and tiene_mayuscula == True and tiene_numero == True:
        print("¡Contraseña segura aceptada!")
        return True
    else:
        print("Error: La contraseña debe tener minúsculas, una mayúscula y un número.")
        return False

clave = input("Prueba una contraseña: ")
validar_contrasena(clave)