import os
import hashlib
from collections import defaultdict
from send2trash import send2trash

# Función para calcular el hash de un archivo
def calculate_hash(file_path):
    """Cálculo del hash SHA-1 de un archivo."""
    hash_sha = hashlib.sha1()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha.update(chunk)
    return hash_sha.hexdigest()

# Función para listar archivos por tamaño
def list_files_by_size(directory):
    """Lista todos los archivos en el directorio agrupados por tamaño."""
    files_dict = defaultdict(list)
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            size = os.path.getsize(file_path)
            files_dict[size].append((file_path, calculate_hash(file_path)))
    return {size: files for size, files in files_dict.items() if len(files) > 1}

# Función para mostrar grupos de duplicados
def display_duplicate_groups(duplicate_groups):
    """Muestra los grupos de archivos duplicados."""
    print("Grupos de archivos duplicados:")
    for i, (size, group) in enumerate(duplicate_groups.items(), start=1):
        print(f"\nGrupo {i}:")
        for file_path, hash_value in group:
            print(file_path)
        print(f"Tamaño: {size} bytes")
        print("-" * 20)

# Función para seleccionar una acción
def select_action(duplicate_group):
    """Selecciona la acción a realizar con los duplicados."""
    while True:
        choice = input("Elige una opción (1-3): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= 3:
            return int(choice)
        print("Opción inválida. Introduce un número entre 1 y 3.")

# Función principal
def main():
    directory = '/home/jesus/Descargas'
    duplicate_groups = list_files_by_size(directory)

    if not duplicate_groups:
        print("No se encontraron archivos duplicados.")
        return

    display_duplicate_groups(duplicate_groups)

    for i, (size, group) in enumerate(duplicate_groups.items(), start=1):
        choice = select_action(group)
        if choice == 3:  # Borrar ambos
            for file_path, _ in group:
                send2trash(file_path)
                print(f"Borrando {file_path}")
        elif choice < len(group):  # Conservar el seleccionado y borrar el resto
            keep_file_path = group[choice - 1][0]
            for file_path, _ in group:
                if file_path != keep_file_path:
                    send2trash(file_path)
                    print(f"Borrando {file_path}")

if __name__ == '__main__':
    main()

#Script generado por Qwen 2.5 coder 7B instruct Q4 en local en minisforum un1290 con zorinOS 18.1 