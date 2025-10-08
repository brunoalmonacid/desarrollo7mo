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



