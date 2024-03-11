import os
os.system('cls')

"""ejercicios sacados de https://pythondiario.com/2013/05/ejercicios-en-python-parte-1.html

1 - Definir una función max() que tome como argumento dos números
y devuelva el mayor de ellos. (Es cierto que python tiene una función max()
incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.
"""
print("\nEJERCICIO 1:")
def max (num1:int, num2:int)->int:
  result = num1-num2
  if result<0:
    return num2
  elif result == 0:
    return "Los 2 números son iguales"
  else:
    return num1

print ("el número mas alto es:",max(0,-1))  

"""
2 - Definir una función max_de_tres(), 
que tome tres números como argumentos y devuelva el mayor de ellos.
"""
print("\nEJERCICIO 2:")
def max_de_tres (num1:int, num2:int, num3:int)->int:
  list_num = []
  list_num.append(num1)
  list_num.append(num2)
  list_num.append(num3)
  list_num.sort()
  return list_num[len(list_num)-1]
print ("el número mas alto es:", max_de_tres(31,89,58))

"""
3 - Definir una función que calcule la longitud de una lista o una cadena dada.
 (Es cierto que python tiene la función len() 
 incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio.
"""
print("\nEJERCICIO 3:")
def len (cadena:str,lista:list):
  counter_char = 0
  counter_element =0
  for char in cadena:
    counter_char +=1
  for element in lista:
    counter_element +=1
  
  return counter_char, counter_element
print("las longitudes de la cadena y la lista son:",len ("hola", [1,2,3,4,5,6]))

"""
4 - Escribir una función que tome un carácter y devuelva True si es una vocal,
 de lo contrario devuelve False.
"""
print("\nEJERCICIO 4:")
def vocal (char:str)->bool:
  if len(char)>1:
    print ("sólo se puede introducir una letra")
    return
  else:
    return char.casefold() in "aeiouAEIOUáéíóúÁÉÍÓÚ"
print(vocal("d"))

"""
5 - Escribir una función sum() y una función multip() que sumen y multipliquen
 respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) 
 debería devolver 10 y multip([1,2,3,4]) debería devolver 24."""
print("\nEJERCICIO 5:")
my_numbers_list = [1,2,3,4]
def sum(list_num:list):
  result = 0
  for i in list_num:
    result += i
  return result 
print(sum(my_numbers_list))


def mult(list_num:list):
  result = 1
  for i in list_num:
    result *= i
  return result 
print(mult(my_numbers_list))

"""
6 - Definir una función inversa() que calcule la inversión de una cadena.
 Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"
"""
print("\nEJERCICIO 6:")
def inversa (cadena:str):
  cadena_list =[]
  for i in cadena:
    cadena_list.append(i)
  cadena_list.reverse()
  cadena=''
  for i in cadena_list:
    cadena += i
  return cadena
print(inversa("estoy probando"))

"""
7 - Definir una función es_palindromo() que reconoce palíndromos 
(es decir, palabras que tienen el mismo aspecto escritas invertidas)
 ejemplo: es_palindromo ("radar") tendría que devolver True.
"""
print("\nEJERCICIO 7:")
def es_palindromo(cadena:str):
   cadena_list =[]
   cadena_reverse =''
   for i in cadena:
     cadena_list.append(i)
   cadena_list.reverse()
   for i in cadena_list:
     cadena_reverse += i 
   if cadena.lower() == cadena_reverse.lower():
     return True
   else:
     return False
print(es_palindromo("Radar"))

"""
8 - Definir una función superposicion() que tome dos listas
 y devuelva True si tienen al menos 1 miembro en común o devuelva 
 False de lo contrario. Escribir la función usando el bucle for anidado.
"""
print("\nEJERCICIO 8:")
list1 =[1,3,5,8,9,7,13]
list2 =[2,4,6,8,10,12]
def superposicion_for(list1,list2):
  for i in list1:
    for j in list2:
     if i == j:
        return True
     else:
        pass
  return False
print(superposicion_for(list1,list2))

def superposicion_set(list1,list2):
  set1 = set(list1)
  set2 = set(list2)
  if set1 & set2:
    return True
  else:
    return False
print(superposicion_set(list1,list2))

"""
9 - Definir una función generar_n_caracteres() 
que tome un entero n y devuelva el caracter multiplicado por n. 
Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".
"""
print("\nEJERCICIO 9:")
def generar_n_caracteres(num:int , char:str)->str:
  
  return num * char

print (generar_n_caracteres(5, 'x'))

"""
10 - Definir un histograma procedimiento() 
que tome una lista de números enteros e imprima un histograma en la pantalla.
 Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
****
*********
*******
"""
print("\nEJERCICIO 10:")
def procedimiento(listograma:list):
  for i in listograma:
    print('\n')
    for j in range(0,i):
     print('*', end='')
  
  


procedimiento([4, 9, 7])












