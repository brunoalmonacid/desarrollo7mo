from personaje import Personaje

class Mario(Personaje):
    def __init__(self, nombre, daño, tirarFuego, vidas = 3, posicion_x = 0, posicion_y = 0):
        super().__init__(nombre, daño, vidas, posicion_x, posicion_y)
        self._tirarFuego = tirarFuego

    def tirarFuego(self):
        if self._tirarFuego:
            return "lanzaste una bola de fuego"
    
        



