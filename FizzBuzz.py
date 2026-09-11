from subprocess import run
from platform import platform

run("cls" if platform().startswith("Windows") else "clear", shell=True)

"""Escribe un programa que muestre por consola (con un print) los
  números de 1 a 100 (ambos incluidos en horizontal
  y con un salto de línea cada 10 impresiones)
  , sustituyendo los siguientes:
  - Múltiplos de 3 por la palabra "fizz".
  - Múltiplos de 5 por la palabra "buzz".
  - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz" """

for i in range(1, 101):
    if i % 15 == 0:
        print(f"{'FizzBuzz':^10}", end="")
    elif i % 5 == 0:
        print(f"{'Buzz':^10}", end="")
    elif i % 3 == 0:
        print(f"{'Fizz':^10}", end="")
    else:
        print(f"{i:^10}", end="")
    if i % 10 == 0:
        print()
