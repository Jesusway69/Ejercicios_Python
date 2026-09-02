from subprocess import run
from platform import platform

run("cls" if platform().startswith("Windows") else "clear", shell=True)

val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]

def int_to_roman1(num:int, val:list, syms:list): #propuesta con while y for
    if not isinstance(num, int) or num <= 0:
        raise ValueError("Input must be a positive integer.")
    
    
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syms[i]
            num -= val[i]
        i += 1
    return roman_num


def int_to_roman2(num:int, val:list, syms:list): #propuesta con while y continue
    if not isinstance(num, int) or num <= 0:
        raise ValueError("Input must be a positive integer.")
    # ... (mismos arrays de val y syms) ...

    roman_num = ""
    i = 0

    while num > 0:
        # Tu lógica: Si el número es menor, avanzamos el índice y saltamos la vuelta
        if num < val[i]:
            i += 1
            continue  # Vuelve al 'while num > 0' con el nuevo índice 'i'

        # Si no es menor, significa que podemos añadir la letra romana
        roman_num += syms[i]
        num -= val[i]

    return roman_num


def int_to_roman3(num:int, val:list, syms:list):
    if not isinstance(num, int) or num <= 0:
        raise ValueError("Input must be a positive integer.")
    roman_num = ""
    i = 0

    # Mientras el número no llegue a cero...
    while num > 0:
        # Mientras el número sea mayor o igual que la "moneda" actual...
        while num >= val[i]:
            roman_num += syms[i]  # Añadimos la letra
            num -= val[i]  # Restamos el valor

        # Cuando ya no quepa más esa letra, pasamos a la siguiente más pequeña
        i += 1

    return roman_num

print(int_to_roman1(26, val, syms))  # Example usage
print(int_to_roman2(12, val, syms))  # Example usage
print(int_to_roman3(1974, val, syms))  # Example usage