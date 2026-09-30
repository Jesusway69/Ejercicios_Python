from subprocess import run
from platform import platform

run("cls" if platform().startswith("Windows") else "clear", shell=True)

"""
PARA COMENTAR EN VARIAS LÍNEAS
SE PUEDE USAR
LA TRIPLE COMILLA DOBLE O SIMPLE
"""
print("Hello World")
print("H€llø ñ wör´ld" + " ™H@√€ å |\| | © €  D∂¥")
print("Good morning world" + ", HAVE A NICE DAY!!")
print("123 % world")
e = "Erasé"
u = "una"
v = "vez..."
print(e, u, v)  # CONCATENACIÓN DE VARIABLES


for i in range(1, 257 + 1, 2):
    print(i)
