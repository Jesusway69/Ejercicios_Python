import os
os.system('clear')

myStr = "Hello WorLd "
#print (dir(myStr))
print (myStr.upper() )# CAMBIA TODO EL STRING A MAYÚSCULAS
print (myStr.lower()) # CAMBIA TODO EL STRING A MINÚSCULAS
print (myStr.swapcase()) # CAMBIA LAS MAYÚSCULAS A MINÚSCULAS Y VICEVERSA
print (myStr.casefold())# CAMBIA TODO EL STRING A MINÚSCULAS INCLUYENDO CARACTERES ESPECIALES
print (myStr.capitalize()) # DEJA SOLO EL PRIMER CARACTER DEL STRING EN MAYÚSCULAS Y EL RESTO A MUNÚSCULAS
print (myStr.replace("Hello" , "Hola")) #REEMPLAZA LA PARTE DEL STRING INDICADA ENTRE LAS PRIMERAS COMILLAS POR LA INDICADA EN LAS SEGUNDAS COMILLAS
print (myStr.count ("o")) #INDICA CUANTOS CARCTERES COMO EL INDICADO HAY DENTRO DEL STRING
print (myStr.startswith("He")) #INDICA SI EL PRIMER O PRIMEROS CARACTERES SON VERDADEROS O FALSOS DENTRO DEL STRING (DEVUELVE BOOLEANO)
print (myStr.endswith ("rld "))#INDICA SI EL ÚLTIMO O ÚLTIMOS CARACTERES SON VERDADEROS O FALSOS DENTRO DEL STRING (DEVUELVE BOOLEANO)
print (len(myStr)) # CUENTA EL NÚMERO DE CARACTERES QUE HAY DENTRO DEL STRING (INCLUYENDO ESPACIOS) (FUNCIÓN DE SISTEMA)
print (myStr  * 5) # SE PUEDEN MULTIPLICAR LOS DATOS DE TIPO STRING
print (myStr[::-1]) #INVIERTE EL ORDEN DE LOS CARACTERES DEL STRING


cadena = "Hola mundo"
#método1
a, b, c, d, e, f , g ,h ,i ,j = cadena
print(j,i,h,g,f,e,d,c,b,a)
#método2
print (cadena[::-1])
#método3
cadena_reves=''.join(reversed(cadena))
print(cadena_reves)
print(type(cadena_reves))

'''def invertir_cadena(cadena):
     cadena="Hola mundo"
     for l in cadena:
         cadena_reves = l + cadena_reves
         return cadena_reves

     print (cadena_reves)

invertir_cadena(cadena)'''


nom, ape, ed = "Jesús", "Matilla", 45
print("Mi nombre es {} {} y mi edad es {}".format(nom, ape, ed))
print("Mi nombre es %s %s y mi edad es %d" %(nom, ape, ed))
print("Mi nombre es " + nom + " " + ape + " y mi edad es " + str(ed))
print(f"Mi nombre es {nom} {ape} y mi edad es {ed}")


x= '23'
print (x.upper())