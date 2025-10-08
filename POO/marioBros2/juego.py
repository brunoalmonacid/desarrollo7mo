from enemigo import Enemigo
from mario import Mario
from peach import Peach
import time

def obtener_personajes_disponibles():
    """Devuelve lista (nombre, factory) — sin prints."""
    return [
        ("Mario", lambda: Mario("Mario", 2, True)),
        ("Peach", lambda: Peach("Peach", 1, True)),
    ]

def seleccionar_personaje_interactivo():
    """Menú (usa prints/input). Devuelve instancia o None."""
    disponibles = obtener_personajes_disponibles()
    while True:
        print("\nSelecciona personaje:")
        for i, (nombre, _) in enumerate(disponibles, start=1):
            print(f"{i}. {nombre}")
        print("0. Salir")
        ele = input("-> ").strip()
        if ele == "0":
            return None
        try:
            idx = int(ele)
            if 1 <= idx <= len(disponibles):
                return disponibles[idx-1][1]()
        except Exception:
            pass
        for nombre, factory in disponibles:
            if nombre.lower() == ele.lower():
                return factory()
        print("Opción no válida, intenta de nuevo.")

def crear_enemigo_fijo(x=5, y=0, dano=1):
    """Crea y devuelve un enemigo en (x,y) — sin prints."""
    try:
        return Enemigo("Goomba", dano, 1, x, y)
    except TypeError:
        try:
            e = Enemigo("Goomba", dano, x, y)
            if not hasattr(e, "_daño"):
                e._daño = dano
            return e
        except Exception:
            e = Enemigo("Goomba", dano)
            if not hasattr(e, "_posicion_x"):
                e._posicion_x = x
            if not hasattr(e, "_posicion_y"):
                e._posicion_y = y
            if not hasattr(e, "_daño"):
                e._daño = dano
            return e

def obtener_posicion(obj):
    """Devuelve (x,y) o None — sin prints."""
    if hasattr(obj, "get_posicion") and callable(getattr(obj, "get_posicion")):
        try:
            return tuple(obj.get_posicion())
        except Exception:
            pass
    x = getattr(obj, "_posicion_x", None)
    y = getattr(obj, "_posicion_y", None)
    if x is not None and y is not None:
        return (x, y)
    return None

def mover_personaje(jugador, direccion):
    """Mueve objeto y devuelve True si se movió — sin prints."""
    if hasattr(jugador, "mover") and callable(getattr(jugador, "mover")):
        try:
            jugador.mover(direccion)
            return True
        except Exception:
            pass
    if hasattr(jugador, "_posicion_x"):
        if direccion == "izquierda":
            jugador._posicion_x -= 1
        elif direccion == "derecha":
            jugador._posicion_x += 1
        return True
    return False

def saltar_personaje(jugador, preguntar_direccion_en_aire=True, delay=0.25):
    """Realiza salto y devuelve True si se ejecutó — sin prints."""
    if hasattr(jugador, "salto") and callable(getattr(jugador, "salto")):
        try:
            jugador.salto()
            return True
        except Exception:
            pass
    if not hasattr(jugador, "_posicion_y"):
        return False
    jugador._posicion_y += 1
    if preguntar_direccion_en_aire and hasattr(__builtins__, "input"):
        dir_en_aire = input("Dirección en el aire (izquierda/derecha/ninguna): ").strip().lower()
        if dir_en_aire in ("izquierda", "derecha"):
            mover_personaje(jugador, dir_en_aire)
    time.sleep(delay)
    jugador._posicion_y -= 1
    return True

def accion_especial(jugador):
    """Ejecuta acción especial si existe y devuelve resultado (sin prints)."""
    candidatos = ("tirar_fuego", "tirarFuego", "planear_activado", "planear")
    for name in candidatos:
        if hasattr(jugador, name) and callable(getattr(jugador, name)):
            try:
                return getattr(jugador, name)()
            except Exception:
                try:
                    return getattr(jugador, name)
                except Exception:
                    return None
    return None

def obtener_estado(jugador, enemigo):
    """Devuelve dict con estado (sin prints)."""
    return {
        "jugador_pos": obtener_posicion(jugador),
        "jugador_vidas": getattr(jugador, "_vidas", getattr(jugador, "vidas", None)),
        "enemigo_pos": obtener_posicion(enemigo),
        "enemigo_dano": getattr(enemigo, "_daño', getattr(enemigo, '_dano', getattr(enemigo, 'dano', None))")    }

def comprobar_colision_y_aplicar(jugador, enemigo):
    """Comprueba colisión; aplica daño y devuelve cantidad aplicada (0 si no hay)."""
    pos_j = obtener_posicion(jugador)
    pos_e = obtener_posicion(enemigo)
    if pos_j is None or pos_e is None:
        return 0
    if pos_j == pos_e:
        dano = getattr(enemigo, "_daño", getattr(enemigo, "_dano", getattr(enemigo, "dano", 1)))
        try:
            dano = int(dano)
        except Exception:
            dano = 1
        if hasattr(jugador, "recibir_daño") and callable(getattr(jugador, "recibir_daño")):
            jugador.recibir_daño(dano)
        elif hasattr(jugador, "perder_vida") and callable(getattr(jugador, "perder_vida")):
            jugador.perder_vida(dano)
        elif hasattr(jugador, "_vidas"):
            try:
                jugador._vidas -= dano
            except Exception:
                pass
        elif hasattr(jugador, "vidas") and not callable(getattr(jugador, "vidas")):
            try:
                jugador.vidas -= dano
            except Exception:
                pass
        return dano
    return 0

def menu_personaje(jugador, enemigo):
    """Menú (usa prints/input). Llama a helpers que retornan resultados."""
    while True:
        print("\n--- MENÚ PERSONAJE ---")
        print("1. Mover izquierda")
        print("2. Mover derecha")
        print("3. Saltar")
        print("4. Acción especial")
        print("5. Mostrar estado")
        print("0. Volver al selector")
        opc = input("-> ").strip()

        if opc == "1":
            moved = mover_personaje(jugador, "izquierda")
            print("Te moviste a la izquierda." if moved else "No se pudo mover.")
        elif opc == "2":
            moved = mover_personaje(jugador, "derecha")
            print("Te moviste a la derecha." if moved else "No se pudo mover.")
        elif opc == "3":
            did = saltar_personaje(jugador)
            print("Saltaste." if did else "No se pudo saltar.")
        elif opc == "4":
            res = accion_especial(jugador)
            print(f"Acción especial: {res}" if res else "No tienes acción especial.")
        elif opc == "5":
            estado = obtener_estado(jugador, enemigo)
            print(f"Jugador posición: {estado['jugador_pos']}  Vidas: {estado['jugador_vidas']}")
            print(f"Enemigo posición: {estado['enemigo_pos']}  Daño: {estado['enemigo_dano']}")
        elif opc == "0":
            print("Volviendo al selector...")
            return
        else:
            print("Opción no válida.")

        dano = comprobar_colision_y_aplicar(jugador, enemigo)
        if dano:
            print(f"¡Colisión! Recibiste {dano} de daño.")

def main():
    print("Bienvenido al juego (modo consola).")
    while True:
        jugador = seleccionar_personaje_interactivo()
        if jugador is None:
            print("Saliendo del juego.")
            break
        enemigo = crear_enemigo_fijo(5, 0, 1)
        print("Enemigo situado en (5, 0). Muévete hasta esa posición para provocar colisión.")
        menu_personaje(jugador, enemigo)

if __name__ == "__main__":
    main()
# filepath: c:\Users\LENOVO\OneDrive\Escritorio\desarrollo7mo\POO\marioBros2\juego.py
from enemigo import Enemigo
from mario import Mario
from peach import Peach
from personaje import Personaje
import time

def obtener_personajes_disponibles():
    """Devuelve lista (nombre, factory) — sin prints."""
    return [
        ("Mario", lambda: Mario("Mario", 2, True)),
        ("Peach", lambda: Peach("Peach", 1, True)),
    ]

def seleccionar_personaje_interactivo():
    """Menú (usa prints/input). Devuelve instancia o None."""
    disponibles = obtener_personajes_disponibles()
    while True:
        print("\nSelecciona personaje:")
        for i, (nombre, _) in enumerate(disponibles, start=1):
            print(f"{i}. {nombre}")
        print("0. Salir")
        ele = input("-> ").strip()
        if ele == "0":
            return None
        try:
            idx = int(ele)
            if 1 <= idx <= len(disponibles):
                return disponibles[idx-1][1]()
        except Exception:
            pass
        for nombre, factory in disponibles:
            if nombre.lower() == ele.lower():
                return factory()
        print("Opción no válida, intenta de nuevo.")

def crear_enemigo_fijo(x=5, y=0, dano=1):
    """Crea y devuelve un enemigo en (x,y) — sin prints."""
    try:
        return Enemigo("Goomba", dano, 1, x, y)
    except TypeError:
        try:
            e = Enemigo("Goomba", dano, x, y)
            if not hasattr(e, "_daño"):
                e._daño = dano
            return e
        except Exception:
            e = Enemigo("Goomba", dano)
            if not hasattr(e, "_posicion_x"):
                e._posicion_x = x
            if not hasattr(e, "_posicion_y"):
                e._posicion_y = y
            if not hasattr(e, "_daño"):
                e._daño = dano
            return e

def obtener_posicion(obj):
    """Devuelve (x,y) o None — sin prints."""
    if hasattr(obj, "get_posicion") and callable(getattr(obj, "get_posicion")):
        try:
            return tuple(obj.get_posicion())
        except Exception:
            pass
    x = getattr(obj, "_posicion_x", None)
    y = getattr(obj, "_posicion_y", None)
    if x is not None and y is not None:
        return (x, y)
    return None

def mover_personaje(jugador, direccion):
    """Mueve objeto y devuelve True si se movió — sin prints."""
    if hasattr(jugador, "mover") and callable(getattr(jugador, "mover")):
        try:
            jugador.mover(direccion)
            return True
        except Exception:
            pass
    if hasattr(jugador, "_posicion_x"):
        if direccion == "izquierda":
            jugador._posicion_x -= 1
        elif direccion == "derecha":
            jugador._posicion_x += 1
        return True
    return False

def saltar_personaje(jugador, preguntar_direccion_en_aire=True, delay=0.25):
    """Realiza salto y devuelve True si se ejecutó — sin prints."""
    if hasattr(jugador, "salto") and callable(getattr(jugador, "salto")):
        try:
            jugador.salto()
            return True
        except Exception:
            pass
    if not hasattr(jugador, "_posicion_y"):
        return False
    jugador._posicion_y += 1
    if preguntar_direccion_en_aire and hasattr(__builtins__, "input"):
        dir_en_aire = input("Dirección en el aire (izquierda/derecha/ninguna): ").strip().lower()
        if dir_en_aire in ("izquierda", "derecha"):
            mover_personaje(jugador, dir_en_aire)
    time.sleep(delay)
    jugador._posicion_y -= 1
    return True

def accion_especial(jugador):
    """Ejecuta acción especial si existe y devuelve resultado (sin prints)."""
    candidatos = ("tirar_fuego", "tirarFuego", "planear_activado", "planear")
    for name in candidatos:
        if hasattr(jugador, name) and callable(getattr(jugador, name)):
            try:
                return getattr(jugador, name)()
            except Exception:
                try:
                    return getattr(jugador, name)
                except Exception:
                    return None
    return None

def obtener_estado(jugador, enemigo):
    """Devuelve dict con estado (sin prints)."""
    return {
        "jugador_pos": obtener_posicion(jugador),
        "jugador_vidas": getattr(jugador, "_vidas", getattr(jugador, "vidas", None)),
        "enemigo_pos": obtener_posicion(enemigo),
        "enemigo_dano": getattr(enemigo, "_daño', getattr(enemigo, '_dano', getattr(enemigo, 'dano', None))")
    }

def comprobar_colision_y_aplicar(jugador, enemigo):
    """Comprueba colisión; aplica daño y devuelve cantidad aplicada (0 si no hay)."""
    pos_j = obtener_posicion(jugador)
    pos_e = obtener_posicion(enemigo)
    if pos_j is None or pos_e is None:
        return 0
    if pos_j == pos_e:
        dano = getattr(enemigo, "_daño", getattr(enemigo, "_dano", getattr(enemigo, "dano", 1)))
        try:
            dano = int(dano)
        except Exception:
            dano = 1
        if hasattr(jugador, "recibir_daño") and callable(getattr(jugador, "recibir_daño")):
            jugador.recibir_daño(dano)
        elif hasattr(jugador, "perder_vida") and callable(getattr(jugador, "perder_vida")):
            jugador.perder_vida(dano)
        elif hasattr(jugador, "_vidas"):
            try:
                jugador._vidas -= dano
            except Exception:
                pass
        elif hasattr(jugador, "vidas") and not callable(getattr(jugador, "vidas")):
            try:
                jugador.vidas -= dano
            except Exception:
                pass
        return dano
    return 0

def menu_personaje(jugador, enemigo):
    """Menú (usa prints/input). Llama a helpers que retornan resultados."""
    while True:
        print("\n--- MENÚ PERSONAJE ---")
        print("1. Mover izquierda")
        print("2. Mover derecha")
        print("3. Saltar")
        print("4. Acción especial")
        print("5. Mostrar estado")
        print("0. Volver al selector")
        opc = input("-> ").strip()

        if opc == "1":
            moved = mover_personaje(jugador, "izquierda")
            print("Te moviste a la izquierda." if moved else "No se pudo mover.")
        elif opc == "2":
            moved = mover_personaje(jugador, "derecha")
            print("Te moviste a la derecha." if moved else "No se pudo mover.")
        elif opc == "3":
            did = saltar_personaje(jugador)
            print("Saltaste." if did else "No se pudo saltar.")
        elif opc == "4":
            res = accion_especial(jugador)
            print(f"Acción especial: {res}" if res else "No tienes acción especial.")
        elif opc == "5":
            estado = obtener_estado(jugador, enemigo)
            print(f"Jugador posición: {estado['jugador_pos']}  Vidas: {estado['jugador_vidas']}")
            print(f"Enemigo posición: {estado['enemigo_pos']}  Daño: {estado['enemigo_dano']}")
        elif opc == "0":
            print("Volviendo al selector...")
            return
        else:
            print("Opción no válida.")

        dano = comprobar_colision_y_aplicar(jugador, enemigo)
        if dano:
            print(f"¡Colisión! Recibiste {dano} de daño.")

def main():
    print("Bienvenido al juego (modo consola).")
    while True:
        jugador = seleccionar_personaje_interactivo()
        if jugador is None:
            print("Saliendo del juego.")
            break
        enemigo = crear_enemigo_fijo(5, 0, 1)
        print("Enemigo situado en (5, 0). Muévete hasta esa posición para provocar colisión.")
        menu_personaje(jugador, enemigo)

if __name__ == "__main__":
    main()