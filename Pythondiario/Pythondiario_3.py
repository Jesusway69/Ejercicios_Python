import os
from random import randint as rad
os.system('cls')


"""
Ejercicio 1
Diseñar un sistema de puntos para el juego El reino del dragón:
Dejo el enlace por si alguien no lo vio.
La idea es la siguiente: mientras el jugador vaya ganando, ira acumulando puntos.
Ejemplo: Si el jugador entra en la primera cueva y gana el tesoro, se le acreditan 100 puntos,
 entra en la segunda cueva y gana el tesoro, se le acreditan otros 100 puntos. Si el jugador pierde,
 saldrá en pantalla el total de los puntos que realizo y la opción de empezar de nuevo.







Ejercicio 2
Escribe un programa que te permita jugar a una versión simplificada del
juego Master Mind. El juego consistirá en adivinar una cadena de números
distintos. Al principio, el programa debe pedir la longitud de la cadena (de 2
a 9 cifras). Después el programa debe ir pidiendo que intentes adivinar la
cadena de números. En cada intento, el programa informará de cuántos números
han sido acertados (el programa considerará que se ha acertado un número si
coincide el valor y la posición).

Dime la longitud de la cadena: 4
Intenta adivinar la cadena: 1234
Con 1234 has adivinado 1 valores. Intenta adivinar
la cadena: 1243
Con 1243 has adivinado 0 valores. Intenta adivinar
la cadena: 1432
Con 1432 has adivinado 2 valores. Intenta adivinar
la cadena: 2431
Con 2431 has adivinado 4 valores.
Felicidades
"""
def init(longitud):

    list_cadena = [0] * longitud
    if longitud<2 or longitud>9:
        print ("Sólo se admiten números del 2 al 9, intente de nuevo")
        init()
    else:
        for i in range (longitud):
         list_cadena[i] = rad(0,9)
    
    return list_cadena

def adivina(cadena):
    list_cadena2 = []
    contador =0
    
    choose = input(f"Introduzca una cadena numérica de {len(init(len(cadena)))} cifras: ")

    for num in choose:
        list_cadena2.append(int(num))
    for i in list_cadena2:
        for j in cadena:
            if i == j:
                contador+=1
     
    print (f"Con {choose} has adivinado {contador} valores")

    if cadena != list_cadena2:
        adivina(cadena)
    else:
        print ("Felicidades, has adivinado todos los números!!")
        return
    

longitud = int(input("Introduzca un número entre 2 y 9 para determinar la longitud de la cadena: "))
init(longitud)
adivina(init(longitud))











"""
Ejercicio 3
Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden
 las tres últimas letras tiene que decir que riman. Si coinciden sólo las dos
 últimas tiene que decir que riman un poco y si no, que no riman.

Ejercicio 4
Has un programa que pida al usuario una cantidad de dolares, una tasa de interés y un numero de años.
Muestra por pantalla en cuanto se habrá convertido el capital inicial transcurridos esos años
  si cada año se aplica la tasa de interés introducida.
Recordar que un capital C dolares a un interés del x por cien durante n años se convierte en C * (1 + x/100)elevado a n (años).
Probar el programa sabiendo que una cantidad de 10000 dolares al 4.5% de interés anual
 se convierte en 24117.14 dolares al cabo de 20 años.
"""