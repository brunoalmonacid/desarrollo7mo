from personaje import Personaje

class Peach(Personaje):
    def __init__(self, nombre, vidas, posicion_x, posicion_y, planear=True):
        super().__init__(nombre, vidas, posicion_x, posicion_y)
        self.planear = bool(planear)

    def planear_activado(self):
        if self.planear:
            print("Peach está planeando!")
