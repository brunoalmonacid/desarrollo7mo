from personaje import Personaje

class Enemigo(Personaje):
    def __init__(self, nombre, daño, vidas = 1, posicion_x = 2, posicion_y = 2):
        super().__init__(nombre, daño, vidas, posicion_x, posicion_y)

def daño(self):
    if daño == True:
        self._vidas -= 1
