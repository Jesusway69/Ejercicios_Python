from nis import cat
import os
from warnings import catch_warnings
os.system('clear')


primer_numero = 4
segundo_numero = 0
#Comentar y descomentar la siguiente asignación de segundo_numero para ver cambios
#segundo_numero = "5"


### try-except
try:
  print(primer_numero + segundo_numero)
  print("operación correcta")
except:
    print("operación incorrecta")

### try-except-else
try:
   print(primer_numero + segundo_numero)
   print("operación correcta")
except: #obligatorio para completar try
    print("operación incorrecta")
else: # opcional para continuar sin excepciones
    print ("la ejecución continúa")

### try-except-else-finally
try: 
   print(primer_numero + segundo_numero)
   print("operación correcta")
except: #obligatorio para completar try
    print("operación incorrecta")
else: # opcional para continuar sin excepciones
    print ("la ejecución contitúa")
finally: #opcional para continuar con y sin excepciones
    print("la ejecución continúa pero puede haber errores")

###prevención de excepciones por tipo
try: 
   print(primer_numero + segundo_numero)
   print("operación correcta")
except TypeError: #TypeError limita la excepción al tipo de dato
    print("tipos de dato incompatibles para esta opración")

###prevención de excepciones por tipo y/o por valor
try: 
   print(primer_numero + segundo_numero)
   print("operación correcta")
except ValueError: #ValueError limita la excepción al valor del dato
    print("valores incompatibles con esta operación")
except TypeError: #TypeError limita la excepción al tipo de dato
    print("tipos de dato incompatibles para esta operación")


###prevención y captura de fallos (concretos o genéricos)
try: 
   print(primer_numero / segundo_numero)
   print("operación correcta")
except Exception as fallo: #Exception nos permite capturar cualquier excepción en una variable
    print(fallo)

 
