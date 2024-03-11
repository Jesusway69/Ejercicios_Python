import os
os.system('clear')

condicion = True
if condicion:
 print("se ejecuta la condición si es true")

#Si aquí hay un else entra por él si condición es false y no entra al siguiente if

 condicion = 5*2
if condicion == 10:
     print ('se ejecuta la condicion del segundo if')

     print ("la ejecución continúa")

condicion=0
while condicion<100:
    print(condicion)
    condicion += 11
    if condicion==55:
     print ('hemos cortado la ejecución en', condicion)
     break
     """con break el programa finaliza al cumplirse la condición del if,
       sino continúa hasta cumplirse la condición del while-else"""
     
else:
    print("ya ha llegado a" , condicion)


