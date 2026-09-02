from subprocess import run
from platform import platform

run("cls" if platform().startswith("Windows") else "clear", shell=True)
    



primer_numero = 4
segundo_numero = 0
cero = 0

#Comentar y descomentar la siguiente asignación de segundo_numero para ver cambios
#segundo_numero = "5"

# ==========================================
# 1. TRY-EXCEPT (Captura segura)
# ==========================================
try:
    print(primer_numero + segundo_numero)
    print("operación correcta\n")
except Exception:  # Cambiado except vacío por Exception
    print("operación incorrecta\n")

# ==========================================
# 2. TRY-EXCEPT-ELSE
# ==========================================
try:
    print(primer_numero + segundo_numero)
    print("operación correcta\n")
except Exception:
    print("operación incorrecta\n")
else:  # Solo entra si el bloque try NO lanzó ninguna excepción
    print("la ejecución continúa (bloque else)\n")

# ==========================================
# 3. TRY-EXCEPT-ELSE-FINALLY
# ==========================================
try:
    print(primer_numero + segundo_numero)
    print("operación correcta\n")
except Exception:
    print("operación incorrecta\n")
else:
    print("la ejecución continúa\n")
finally:
    # Se ejecuta SIEMPRE (haya o no un error). Ideal para liberar recursos o cerrar archivos.
    print("Liberando recursos en el bloque finally...\n")

# ==========================================
# 4. EXCEPCIONES ESPECÍFICAS
# ==========================================
try:
    print(primer_numero + segundo_numero)
    print("operación correcta\n")
except TypeError:  # Captura estricta de tipos de datos
    print("tipos de dato incompatibles para esta operación\n")

try:
    print(primer_numero / cero)
    print("operación correcta\n")
except ZeroDivisionError:  # Captura estricta de división por cero
    print("no se puede dividir entre 0\n")

# ==========================================
# 5. CAPTURA MÚLTIPLE Y ALIAS
# ==========================================
try:
    print(primer_numero + segundo_numero)
    print("operación correcta")
except ValueError:
    print("valores incompatibles con esta operación")
except TypeError:
    print("tipos de dato incompatibles para esta operación")
print("")

try:
    print(primer_numero / segundo_numero)
    print("operación correcta")
except Exception as fallo:  # Captura el objeto del error para leer su mensaje original
    print(f"Fallo detectado por el sistema: {fallo}\n")