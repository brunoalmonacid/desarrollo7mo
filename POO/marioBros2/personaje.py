from mario import Mario
from peach import Peach

import time

class Personaje: 
    def __init__(self, nombre, daño, vidas = 3, posicion_x = 0, posicion_y = 0):
        self._nombre = nombre
        self._posicion_x = posicion_x
        self._posicion_y = posicion_y
        self._vidas = vidas
        self._daño = daño
def posicion_x(self):
    return self.posicion_x 

def posicion_y(self):
    return self.posicion_y 

def mover (self, direccion):
    if direccion == "izquierda":
        self._posicion_x -= 1 
    elif direccion == "derecha":
        self._posicion_x += 1

def salto(self):
    if salto == True:
        self._posicion_y += 1 
        time.sleep(0,5)
        self._posicion_y -= 1
        return "saltaste"
def vidas (self, ):
    return self._vidas

def dondeEstoy(self):
    return (self._posicion_x, self._posicion_y)



def obtenerPersonaje():
    return Mario, Peach

def seleccionarPersonaje():
    if seleccionarPersonaje == 1:
        return Mario("Mario", 3, 0, 0)
    if seleccionarPersonaje == 2:
        return Peach("Peach", 3, 0, 0)

#menu
def menu():
    print("Seleccione un personaje:")
    print("1. Mario")
    print("2. Peach")
    seleccionarPersonaje = int(input("Ingrese el número del personaje que desea seleccionar: "))
    personaje = seleccionarPersonaje()
    print(f"Has seleccionado a {personaje._nombre} con {personaje._vidas} vidas.")
    return personaje

def menuMario():
    while True:
        print("\n--- MENÚ PERSONAJE ---")
        print("1. Mover izquierda")
        print("2. Mover derecha")
        print("3. Saltar")
        print("4. Acción especial")
        print("5. Mostrar estado")
        print("0. cerrar")
        
        opc = int(input("Seleccione una opción: "))
        if opc == 0:
            break
        elif opc == 1:
            Personaje.mover("izquierda")    
        elif opc == 2:
            Personaje.mover("derecha")  
        elif opc == 3: 
            Personaje.salto("salto")
        elif opc == 4:
            if Personaje == Mario:
                Personaje.tirarFuego()
            elif Personaje == Peach:
                Personaje.planear_activado()
        elif opc == 5:
            print(f"Posición: {Personaje.dondeEstoy()} | Vidas: {Personaje.vidas()}")