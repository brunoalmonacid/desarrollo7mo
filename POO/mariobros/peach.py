from personaje import Personaje

class Peach(Personaje):
    def __init__(self, nombre, vidas, posicion_x, posicion_y, planear=True):
        super().__init__(nombre, vidas, posicion_x, posicion_y)
        self._planear = bool(planear)

    def planear_activado(self):
        if self._planear:
            print("Peach está planeando!")

    @property
    def planear(self):
        return self._planear

    @planear.setter
    def planear(self, v):
        self._planear = bool(v)
