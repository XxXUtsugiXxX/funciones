# 1. Sistema de Biblioteca Virtual
# Descripción:
# Crea un programa que permita gestionar una pequeña biblioteca.

# Debe permitir:

# Ver los libros disponibles.
# Agregar nuevos libros.
# Prestar libros (cambiar su estado a “prestado”).
# Devolver libros.
# Ver el historial de préstamos.


librosL = []

def agregar_libros(librosL):
    nombre = input("ingresa el libro que quieres agregar: ").lower()
    estado = "disponible"
    libroD = {"nombre" : nombre, "prestar" : estado}
    librosL.append(libroD)
    
def ver_libros(librosL):
        if not librosL: 
            print("inventario de libros vacio")
        else:
            for libroD in librosL:
                print(f"el nombre del libro {libroD["nombre"]} y esta en estado {libroD["prestar"]}")
        
def prestar_libros(librosL):
    libro = input("digita el libro que quieres buscar: ").lower() 
    for buscar in librosL:
        if buscar["nombre"].lower() == libro:
            if buscar["prestar"] == "disponible":
                buscar["prestar"]="prestado"
                print(f"libro {libro} prestado")
            else:
                print("libro no disponible")
                break
        else:   
            print("no existe")
        
def devolverL(librosL):
    libro = input("digita el libro que quieres buscar: ").lower() 
    for buscar in librosL:
        if buscar["nombre"].lower() == libro:
            if buscar["prestar"] == "prestado":
                buscar["prestar"]="disponible"
                print(f"libro {libro} devuelto")
            else:
                print("libro no prestado")
                break
        else:   
            print("no existe")
            
def historial(librosL):
    for librosD in librosL:
        if librosD["prestar"] == "prestado":
            print(f"estos son los libros prestados {librosD}")
            break

            
while True:
    print("Menu principal")
    print("1. Agregar libros: ")
    print("2. Mostrar ver libros: ")
    print("3. prestar libros: ")
    print("4. devolver libros")
    print("5. historial de libros prestados")
    print("6. salir")
    

    opcion = int(input("digita una opcion de 1 a 6: "))
    if opcion < 1 or opcion > 6:
        opcion = int(input("digita una opcion  valida de 1 a 6: "))
        continue
    if opcion == 1:
        agregar_libros(librosL)
    elif opcion == 2:
        ver_libros(librosL)
    elif opcion == 3:
        prestar_libros(librosL)
    elif opcion == 4:
        devolverL(librosL)
    elif opcion == 5:
        historial(librosL)
    else:
        print("saliste del menu")
        break
    