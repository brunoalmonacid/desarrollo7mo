import pygame

ROJO = (200, 50, 50)

class Enemigo:
    def __init__(self, x, y, limite_izq=400, limite_der=700):
        self.x = x
        self.y = y
        self.ancho = 40
        self.alto = 40
        self.vx = 2
        self.limite_izq = limite_izq
        self.limite_der = limite_der
        self.vivo = True

    def actualizar(self):
        if not self.vivo:
            return
        self.x += self.vx
        if self.x < self.limite_izq or self.x + self.ancho > self.limite_der:
            self.vx *= -1

    def get_rect(self):
        return pygame.Rect(int(self.x), int(self.y), self.ancho, self.alto)

    def dibujar(self, surf):
        if self.vivo:
            pygame.draw.rect(surf, ROJO, self.get_rect())
