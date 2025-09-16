import pygame, sys
from mario import Mario
from peach import Peach
from POO.mariobros.enemigos import Enemigo

pygame.init()

ANCHO, ALTO = 800, 400
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego modular")
reloj = pygame.time.Clock()

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (50, 50, 200)
ROSA = (255, 182, 193)

def seleccionar_personaje():
    fuente = pygame.font.SysFont(None, 40)
    while True:
        ventana.fill(BLANCO)
        texto = fuente.render("Elige [M] Mario o [P] Peach", True, NEGRO)
        ventana.blit(texto, (200, 150))
        pygame.display.flip()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_m:
                    return Mario("Mario", 3, 100, 300)
                if e.key == pygame.K_p:
                    return Peach("Peach", 3, 100, 300)

def main():
    jugador = seleccionar_personaje()
    enemigo = Enemigo(520, 300)

    fuente = pygame.font.SysFont(None, 32)
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    jugador.iniciar_salto()
                if e.key == pygame.K_f and isinstance(jugador, Mario):
                    jugador.tirar_fuego()

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            jugador.mover("izquierda")
        if teclas[pygame.K_RIGHT]:
            jugador.mover("derecha")

        mantener = isinstance(jugador, Peach) and teclas[pygame.K_SPACE]
        jugador.aplicar_gravedad(mantener)

        if isinstance(jugador, Mario):
            jugador.actualizar_proyectiles()

        enemigo.actualizar()

        # Colisiones
        if enemigo.vivo and jugador.get_rect().colliderect(enemigo.get_rect()):
            if jugador.vel_y > 0:
                enemigo.vivo = False
                jugador.vel_y = -8
                jugador.salto = True
            else:
                jugador.perder_vida()

        if isinstance(jugador, Mario) and enemigo.vivo:
            for p in jugador.proyectiles:
                if p['rect'].colliderect(enemigo.get_rect()):
                    enemigo.vivo = False

        # Dibujo
        ventana.fill(BLANCO)
        color = AZUL if isinstance(jugador, Mario) else ROSA
        jugador.dibujar(ventana, color)
        enemigo.dibujar(ventana)
        vidas = fuente.render(f"Vidas: {jugador.vidas}", True, NEGRO)
        ventana.blit(vidas, (10, 10))
        pygame.display.flip()
        reloj.tick(60)

if __name__ == "__main__":
    main()
