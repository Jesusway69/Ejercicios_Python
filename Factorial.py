import os
os.system('clear')

numero = int(input("numero para obtener factorial: "))

factorial = 1
for i in range(1,numero +1):
    factorial = factorial * i 
print(factorial)  