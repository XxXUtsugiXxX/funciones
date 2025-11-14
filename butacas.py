def reserva(butacos, nombre, posicion):
    if posicion <= 10:
        reserva1.extend([butacos, nombre, posicion])
    else:
        print("esto es invalido")
    for dato in reserva1:
        print(f"numero de butacos {butacos}, a nombre de {nombre}, en la posición {posicion}")
        confirmar=input("dijita si o no, si es correcto el pedido: ")
        break
    if confirmar == "si":
        confirmado.extend([ nombre])
    else:
        Noconfirmado.extend([nombre])
        
    print(f"estas personas estan confirmadas {confirmado}")
    print(f"estas personas dijeron que no {Noconfirmado}")
        
confirmado = []
Noconfirmado = []
reserva1 = []
reserva(5, "brayhan", 9)
reserva(10, "andres", 8)