# 2. Gestor de Tareas Diarias
# Descripción:
# Simula una app de tareas pendientes (To-Do List).

# Debe permitir:

# Agregar tareas.
# Marcar tareas como completadas.
# Eliminar tareas.
# Mostrar todas las tareas (pendientes y completadas).
# Salir del sistema.

lista_tareas = []

def agregar(lista_tareas):
    tareas = input("ingresa la tarea: ").lower()
    estado = "sin terminar"
    tarea_dic = {"tarea" : tareas, "sin terminada" : estado}
    lista_tareas.append(tarea_dic)

def completadas(lista_tareas):
    for terminadas in lista_tareas:
        if terminadas["sin terminada"] == "sin terminar":
            print(f"las tareas {terminadas['tarea']} estan en estado {terminadas['sin terminada']}")
            marcar=int(input("digita 1 para poner terminada y 2 para salir: "))
            if marcar == 1:
                terminadas["sin terminada"]="terminada"
                print(f"las tareas {terminadas['tarea']} estan en estado {terminadas['sin terminada']}")
            elif marcar == 2:
                print("saliste al menu principal")
                break
        else:
            print(f"las tareas {terminadas['tarea']} estan en estado {terminadas['sin terminada']}")

             
def eliminar(lista_tareas):
    for eliminar in lista_tareas:
        nombreE = input("indica el nombre de la tarea que queires eliminar: ").lower()
        if eliminar["tarea"] == nombreE:
            lista_tareas.remove(eliminar)
            print(f"la tarea {nombreE} a sido eliminada")
            return
    print("no existe la tarea")


def mostrar(lista_tareas):
    for mostrar in lista_tareas:
        print(f"las tareas {mostrar['tarea']} estan en estado {mostrar['sin terminada']}")        




while True:
    print("Menu principal")
    print("1. Agregar tareas: ")
    print("2. Mostrar competadas: ")
    print("3. eliminar tareas: ")
    print("4. mostrar")
    print("5. salir")
    
    

    opcion = int(input("digita una opcion de 1 a 5: "))
    if opcion < 1 or opcion > 5:
        opcion = int(input("digita una opcion  valida de 1 a 5: "))
        continue
    if opcion == 1:
         agregar(lista_tareas)
    elif opcion == 2:
         completadas(lista_tareas)
    elif opcion == 3:
        eliminar(lista_tareas)
    elif opcion == 4:
        mostrar(lista_tareas)
    else:
        print("saliste del menu")
        break