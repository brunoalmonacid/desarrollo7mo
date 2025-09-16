import pygame

ROJO = (200, 50, 50)

class Enemigo:
    def __init__(self, x, y, limite_izq=400, limite_der=700):
        self._x = x
        self._y = y
        self._ancho = 40
        self._alto = 40
        self._vx = 2
        self._limite_izq = limite_izq
        self._limite_der = limite_der
        self._vivo = True

    def actualizar(self):
        if not self._vivo:
            return
        self._x += self._vx
        if self._x < self._limite_izq or self._x + self._ancho > self._limite_der:
            self._vx *= -1

    def get_rect(self):
        return pygame.Rect(int(self._x), int(self._y), self._ancho, self._alto)

    def dibujar(self, surf):
        if self._vivo:
            pygame.draw.rect(surf, ROJO, self.get_rect())

    @property
    def vivo(self):
        return self._vivo

    @vivo.setter
    def vivo(self, v):
        self._vivo = bool(v)
