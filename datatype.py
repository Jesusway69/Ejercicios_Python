from subprocess import run
from platform import platform

run("cls" if platform().startswith("Windows") else "clear", shell=True)


# STRINGS

print("Hello World")

# concatenation
print("para" + "choques")

# repeat
print("Ja " * 5)

# show types
print(type("hello world"))
print("3 + 10")
print(3 + 10)


# NUMBERS

# integer
print(type(30))
print(30)

# float
print(type(30.5))
print(30.5)

# complex
print(type(1+2j))
print(1+2j)

# Boolean
print(type(True))
print(type(False))
print(5 > 2)
print("5" == 5)


# STRUCTURES

# LIST mutable
int_list = [10, 20, 30, 40]
int_srt_list = [10, "hello", "world"]
all_types_list = [20, "hola", True, 10.5]
print(type([10, 20]))
print(type(int_list))
print(type(int_srt_list))
print(type(all_types_list))

# TUPLE inmutable
parenthesis_tuple = (10, 20, 30, 40)
non_parenthesis_tuple = 10, 20, 30, 40
empty_Tuple = ()
print(type((10, 20)))
print(type(parenthesis_tuple))
print(type(non_parenthesis_tuple))
print(type(empty_Tuple))

# Tuple Unpacking (Desempaquetado)
x, y, z, w = non_parenthesis_tuple
print(x)
print(y)

# Truco "pythónico": Intercambio de valores usando tuplas implícitas
a = 1
b = 2
a, b = b, a
print(a, b)  # Imprime: 2 1

# DICTIOARIES key : value
id_dict = {
    "name": "Phil",
    "aka": "Animal",
    "surname": "Taylor"
}
empty_dict = {}
print({
    "latitude": 12121212,
    "longitude": 121212121
})

print(type(id_dict))
print(type(empty_dict))
print(type({"madrid": "campeon"}))
print({"madrid": "campeon"})

# NONE epmty datatype
print(type(None))
print(type(print("dato vacío")))

# Identity object
a = 100
print(id(a))
