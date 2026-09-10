from subprocess import run
from platform import platform

run("cls" if platform().startswith("Windows") else "clear", shell=True)

number = int(input("numero para obtener factorial: "))

factorial = 1

for i in range(1, number + 1):
    factorial = factorial * i 
    
print(f"El factorial de {number} es: {factorial}\n")  