import pygame

class Personaje:
    def __init__(self, nombre, vidas, posicion_x, posicion_y):
        self.nombre = nombre
        self._posicion_x = posicion_x
        self._posicion_y = posicion_y
        self.vidas = vidas

        self.ancho = 40
        self.alto = 50
        self.velocidad = 5
        self.salto = False
        self.vel_y = 0
        self.gravedad = 0.6
        self.proyectiles = []
        self.invulnerable_timer = 0  

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
            self._posicion_x -= self.velocidad
        elif direccion == "derecha":
            self._posicion_x += self.velocidad

    def iniciar_salto(self):
        if not self.salto:
            self.salto = True
            self.vel_y = -11

    def aplicar_gravedad(self, mantener_salto=False):
        if self.salto:
            factor = 0.35 if mantener_salto else 1.0
            self.vel_y += self.gravedad * factor
            self._posicion_y += self.vel_y
            if self._posicion_y >= 300:
                self._posicion_y = 300
                self.salto = False
                self.vel_y = 0

    def get_rect(self):
        return pygame.Rect(int(self._posicion_x), int(self._posicion_y), self.ancho, self.alto)

    def perder_vida(self):
        if pygame.time.get_ticks() > self.invulnerable_timer:
            self.vidas -= 1
            self.invulnerable_timer = pygame.time.get_ticks() + 1000
            self._posicion_x = 100
            self._posicion_y = 300

    def dibujar(self, surf, color):
        rect = self.get_rect()
        pygame.draw.rect(surf, color, rect)
