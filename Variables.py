

#CASE SENSITIVE
from decimal import MIN_EMIN


nombre = "jesus"
primerapellido = "Matilla"
print (nombre , primerapellido)
nombre, primerapellido , edad = "Jesus" , "Matilla", 46 #declarar variables en una línea, no recomendado por facilidad de error
#se pueden combinar tipos de datos diferentes
print(primerapellido,edad,nombre) #podemos imprimir las variables en el orden que queramos

#ENTRADA DE DATOS SIMPLE POR TERMINAL (INPUT)
nombre = input("como te llamas? ") #Se pausa la ejecución para pedir entrada de datos, acepta cualquier tipo
print ("OK, te llamas",nombre) #Imprime la varibla que le acabamos de dar aunque ya se hubiera declarado y mostrado antes

#CONVENCIONES
book_name = "el señor de las moscas" #Snake case para valores variables (convención más admitida en python)
bookName = "el guardian entre el centeno" #Camel case para valores variables (no bien visto en python)
BookName = "don quijote" # Pascal case
BOOK_NAME = "los trapos sucios" # Screaming snake case para valores fijos o constantes de más de una palabra
PI = 3.1416 #Valores fijos o constantes todo en mayusculas
#book-name = "los pilares de la tierra" #kebap case (no reconocida)
l33t = "password" #Leet case para contraseñas

# OPERADORES DE COMPARACION (siempre devuelve booleano)
print (5==5) #IGUAL
print (5!=5) #DIFERENTE
print (456>358) #MAYOR 
print (152<125) #MENOR 
print(184<=184) #MENOR O IGUAL 
print(225>=521) #MAYOR O IGUAL 



mi_lista = ["Miguel", "Luis", "Jose" , "Ana" , "Carmen"]
mi_lista.append("Sara" )
print(mi_lista)