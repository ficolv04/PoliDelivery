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
            
    return tiene_minuscula and tiene_mayuscula and tiene_numero