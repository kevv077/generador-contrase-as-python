from random import sample 
# Importamos la función sample de la librería random, la cual nos permite seleccionar una muestra aleatoria de una secuencia


longitud = input("Ingrese la longitud de la contraseña: ") # Solicitamos la longitud de la contraseña
def password_generator(longitud):  # Definimos la función password_generator
    abc_minusculas = "abcdefghijklmnopqrstuvwxyz" # Definimos el abecedario en minúsculas
    abc_mayusculas = abc_minusculas.upper() # Convertimos las letras a mayúsculas
    numeros = "0123456789" # Definimos los números
    simbolos = "{}[]()*;/,_-" # Definimos los símbolos
    caracteres = abc_minusculas + abc_mayusculas + numeros + simbolos # Unimos todos los caracteres
    password_union = sample(caracteres, longitud) # Seleccionamos una muestra aleatoria de la longitud ingresada
    password_result = "".join(password_union) # Unimos los caracteres seleccionados
    return password_result # Retornamos la contraseña generada

password = password_generator(int(longitud)) # Llamamos a la función y le pasamos la longitud de la contraseña
print("Contraseña: ", password) # Imprimimos la contraseña generada