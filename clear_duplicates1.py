import os
from collections import defaultdict
from send2trash import send2trash # type: ignore
def get_file_size_and_content(file_path):
    """Devuelve un hash del tamaño y contenido del archivo."""
    with open(file_path, 'rb') as file:
        content = file.read()
    return (os.path.getsize(file_path), hash(content))

def find_duplicates(directory):
    """Encuentra archivos duplicados en el directorio dado."""
    duplicates = defaultdict(list)
    
    for root, _, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            size_and_content_hash = get_file_size_and_content(path)
            duplicates[size_and_content_hash].append(path)
    
    return {key: paths for key, paths in duplicates.items() if len(paths) > 1}

def interact_with_user(duplicates_dict):
    """Interactúa con el usuario para decidir qué hacer con los archivos duplicados."""
    for index, (key, paths) in enumerate(duplicates_dict.items(), 1):
        print(f"\nGrupo {index}:")
        for path in paths:
            print(path)
        
        while True:
            decision = input("\nElige una opción: Conservar 1, Conservar 2, Conservar ambos, Elegir manualmente (c/s/b/m): ").strip().lower()
            if decision in ['c', 's', 'b', 'm']:
                break
            
        if decision == 'c':
            keep_files = input("Ingresa el número del archivo que deseas conservar (usa comas para múltiples archivos): ").strip().split(',')
            keep_files = [int(f.strip()) - 1 for f in keep_files]
        elif decision == 's':
            send2trash.send2trash(paths[0])  # Suponemos que el primero es a conservar
            send2trash.send2trash(paths[1])
        elif decision == 'b':
            print("Se conservarán ambos archivos.")
            continue
        else:
            for i, path in enumerate(paths):
                while True:
                    choice = input(f"¿Deseas enviar a la papelera {path}? (s/n): ").strip().lower()
                    if choice in ['n', 's']:
                        break
                if choice == 's':
                    send2trash.send2trash(path)
      
def main():
    directory = '/Users/jesus/Downloads'
    
    if not os.path.isdir(directory):
        print(f"El directorio {directory} no existe.")
        return
    
    duplicates = find_duplicates(directory)
    
    if not duplicates:
        print("No se encontraron archivos duplicados.")
        return
    
    interact_with_user(duplicates)

if __name__ == "__main__":
    main()

#Script generado por Qwen 2.5 14B Q8 en local en mac mini m4 con macOS Tahoe