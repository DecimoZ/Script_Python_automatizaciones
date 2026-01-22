print("-" * 10)
print("bievenido al programa de creacion de archivos")
print("-" * 10)

def crear_archivo_txt():
    pedir_nombre = input("ingrese el nombre del archivo que desea crear:")
    nombre = pedir_nombre
    open(f"{nombre}.txt", "x")


def crear_archivo_py():
    pedir_nombre = input("ingrese el nombre del archivo que desea crear:")
    nombre = pedir_nombre
    open(f"{nombre}.docx", "x")


def crear_archivo_power():
    pedir_nombre = input("ingrese el nombre del archivo que desea crear:")
    nombre = pedir_nombre
    open(f"{nombre}.pptx", "x")


opcion_usuario = int(input("ingrese la opcion que desea hacer 1 para crear txt | 2 para crear un word  | 3 para crear powerpoint : "))

def app():
    if opcion_usuario == 1:
        crear_archivo_txt()
    elif opcion_usuario == 2:
        crear_archivo_py()
    elif opcion_usuario == 3:
        crear_archivo_power()
    else:
        print("no se crea el archivo")



app()
print("-" * 10)




