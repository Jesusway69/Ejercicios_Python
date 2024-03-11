import os
os.system('clear')


def funcion():
    print('función de muestra')
funcion()

def suma_dos_valores(primer_valor,segundo_valor):
    print(primer_valor + segundo_valor)
#suma_dos_valores(45,54)
#suma_dos_valores(9.5,2.5)
#suma_dos_valores('234','908')

def suma_dos_valores_con_retorno(primer_valor , segundo_valor):
    return(primer_valor + segundo_valor)
resultado = suma_dos_valores_con_retorno(45,54)
print(resultado)
#resultado = suma_dos_valores (45,54)
#print(resultado)

def imprime_nombre(nombre,apellido):
    print(f'{nombre} {apellido}')
imprime_nombre(apellido="Matilla",nombre="Jesús")

def imprime_nombre_por_defecto(nombre,apellido,alias="sin alias"):
    print(f'{nombre} {apellido} {alias}')
imprime_nombre_por_defecto("Jesús","Matilla")

def imprimir_textos(*texto_s):
    for texto in texto_s:
      print(texto)
imprimir_textos("buenos","días")
imprimir_textos("por","la","mañana")

suma_dos_valores(1,2)
print(suma_dos_valores_con_retorno(2,3))