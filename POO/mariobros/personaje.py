import pygame

class Personaje:
    def __init__(self, nombre, vidas, posicion_x, posicion_y):
        self._nombre = nombre
        self._posicion_x = posicion_x
        self._posicion_y = posicion_y
        self._vidas = vidas

        self._ancho = 40
        self._alto = 50
        self._velocidad = 5
        self._salto = False
        self._vel_y = 0
        self._gravedad = 0.6
        self._proyectiles = []
        self._invulnerable_timer = 0

    @property
    def posicion_x(self):
        return self._posicion_x

    @posicion_x.setter
    def posicion_x(self, v):
        self._posicion_x = v

    @property
    def posicion_y(self):
        return self._posicion_y

    @posicion_y.setter
    def posicion_y(self, v):
        self._posicion_y = v

    def mover(self, direccion):
        if direccion == "izquierda":
            self._posicion_x -= self._velocidad
        elif direccion == "derecha":
            self._posicion_x += self._velocidad

    def iniciar_salto(self):
        if not self._salto:
            self._salto = True
            self._vel_y = -11

    def aplicar_gravedad(self, mantener_salto=False):
        if self.salto:
            factor = 0.35 if mantener_salto else 1.0
            self._vel_y += self._gravedad * factor
            self._posicion_y += self._vel_y
            if self._posicion_y >= 300:
                self._posicion_y = 300
                self._salto = False
                self._vel_y = 0

    def get_rect(self):
        return pygame.Rect(int(self._posicion_x), int(self._posicion_y), self.ancho, self.alto)

    def perder_vida(self):
        if pygame.time.get_ticks() > self._invulnerable_timer:
            self._vidas -= 1
            self._invulnerable_timer = pygame.time.get_ticks() + 1000
            self._posicion_x = 100
            self._posicion_y = 300

    def dibujar(self, surf, color):
        rect = self.get_rect()
        pygame.draw.rect(surf, color, rect)

    # --- Propiedades públicas (API compatible) ---
    @property
    def nombre(self):
        return self._nombre

    @property
    def vidas(self):
        return self._vidas

    @vidas.setter
    def vidas(self, v):
        self._vidas = v

    @property
    def vel_y(self):
        return self._vel_y

    @vel_y.setter
    def vel_y(self, v):
        self._vel_y = v

    @property
    def salto(self):
        return self._salto

    @salto.setter
    def salto(self, v):
        self._salto = bool(v)

    @property
    def proyectiles(self):
        return self._proyectiles

    @proyectiles.setter
    def proyectiles(self, val):
        self._proyectiles = val

    @property
    def ancho(self):
        return self._ancho

    @property
    def alto(self):
        return self._alto

    @property
    def velocidad(self):
        return self._velocidad

    @velocidad.setter
    def velocidad(self, v):
        self._velocidad = v
