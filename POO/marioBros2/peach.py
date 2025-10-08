from personaje import Personaje

class Peach(Personaje):
    def __init__(self, nombre, daño, planear, vidas = 3, posicion_x = 0, posicion_y = 0):
        super().__init__(nombre, daño, vidas, posicion_x, posicion_y)
        self._planear = planear

def planear_activado(self):
    if self._planear == True:
        return "estas está planeando"
    
