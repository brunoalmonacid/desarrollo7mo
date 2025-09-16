import pygame
from personaje import Personaje

NARANJA = (255, 140, 0)
ANCHO = 800

class Mario(Personaje):
    def __init__(self, nombre, vidas, posicion_x, posicion_y, tirarFuego=True):
        super().__init__(nombre, vidas, posicion_x, posicion_y)
        self._tirarFuego = bool(tirarFuego)
        self._last_shot = 0
        self._shot_cooldown = 350

    def tirar_fuego(self):
        if not self._tirarFuego:
            return
        ahora = pygame.time.get_ticks()
        if ahora - self._last_shot >= self._shot_cooldown:
            bx = int(self._posicion_x + self.ancho)
            by = int(self._posicion_y + self.alto // 3)
            bola = pygame.Rect(bx, by, 10, 10)
            self.proyectiles.append({'rect': bola, 'vx': 8})
            self._last_shot = ahora

    def actualizar_proyectiles(self):
        nuevas = []
        for p in self.proyectiles:
            p['rect'].x += p['vx']
            if p['rect'].x < ANCHO:
                nuevas.append(p)
        self.proyectiles = nuevas

    def dibujar(self, surf, color):
        super().dibujar(surf, color)
        for p in self.proyectiles:
            pygame.draw.rect(surf, NARANJA, p['rect'])
