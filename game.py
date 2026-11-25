import pygame
import random
import escenas
import math

pygame.init()

# Variables
colores = escenas.colores
fuentetitulo = pygame.font.Font(None, 30)
fuenteabajo = pygame.font.Font(None, 20)
volumen_general = 1
volumen_musica = 1 * volumen_general
volumen_sonidos = 1 * volumen_general
disparos = []
up, left, down, right = False, False, False, False
shopm = False
iframes, colision, contador, facen, colorn = 0, 0, 0, 0, 0
screen = pygame.display.set_mode((1200, 640))
player = pygame.image.load("sprites/skin/player.png").convert_alpha()
cara = pygame.image.load("sprites/skin/caras/0.png").convert_alpha()
skinnormal = pygame.image.load("sprites/skin/skin.png").convert_alpha()
skin = pygame.image.load("sprites/skin/skin.png").convert_alpha()
icon = pygame.image.load("sprites/icon.png").convert_alpha()
heart = pygame.image.load("sprites/heart.png").convert_alpha()
emptyheart = pygame.image.load("sprites/empty_heart.png").convert_alpha()
disparo = pygame.image.load("sprites/disparo.png").convert_alpha()
dragon = pygame.image.load("sprites/dragon.png").convert_alpha()
shop = pygame.image.load("sprites/shop.png")
play = pygame.image.load("sprites/play.png")
exit = pygame.image.load("sprites/exit.png")
menu = pygame.image.load("sprites/menu.png")
info = pygame.image.load("sprites/informacion.png").convert_alpha()
configuracion = pygame.image.load("sprites/configuracion.png").convert_alpha()
running = True
x = 0
y = 0
vida = 3
heart1, heart2, heart3 = heart, heart, heart
menumusic = pygame.mixer.Sound("music/OST_music_menu.wav")
shopmusic = pygame.mixer.Sound("music/Ost music tienda.wav")
canal1 = pygame.mixer.Channel(0)
canal2 = pygame.mixer.Channel(1)
clock = pygame.time.Clock()
canal1.play(menumusic, loops=-1)
canal2.play(shopmusic, loops=-1)
canal1.set_volume(1.0)
canal2.set_volume(0.0)
mezcla = 0.0
duracion_segundos = 1.0
duracion_iframes = 1.0
cooldown_disparos = 5.0
cooldownd = cooldown_disparos
hitbox = pygame.Rect(x, y, player.get_width(), player.get_height())
arrastrando = None
mejorpuntuacion = 0

sliders = {
    "General": pygame.Rect(400, 180, 400, 10),
    "Musica": pygame.Rect(400, 280, 400, 10),
    "Sonidos": pygame.Rect(400, 380, 400, 10),
}


def actualizar_slider(rect, mouse_x):
    x_limitado = max(rect.left, min(mouse_x, rect.right))
    return (x_limitado - rect.left) / rect.width


def dibujar_slider(rect, volumen, nombre):
    texto = fuentetitulo.render(nombre, True, (0, 0, 0))
    screen.blit(texto, texto.get_rect(center=(600, rect.y - 30)))

    pygame.draw.rect(screen, (150, 150, 150), rect, border_radius=5)

    ancho = int(rect.width * volumen)

    pygame.draw.rect(
        screen, (100, 50, 255), (rect.x, rect.y, ancho, rect.height), border_radius=5
    )

    pygame.draw.circle(screen, (0, 0, 0), (rect.x + ancho, rect.centery), 12)

    porcentaje = fuenteabajo.render(f"{int(volumen * 100)}%", True, (0, 0, 0))

    screen.blit(porcentaje, porcentaje.get_rect(center=(600, rect.y + 30)))


def escalar(name, scale):
    name = pygame.transform.scale(
        name, (name.get_width() * scale, name.get_height() * scale)
    )
    return name


def change_color(sprite, color):
    new_sprite = sprite.copy()
    new_sprite.fill(color, special_flags=pygame.BLEND_RGBA_MULT)
    return new_sprite


def change_face(num):
    cara = pygame.image.load(f"sprites/skin/caras/{num}.png").convert_alpha()
    cara = escalar(cara, 10)
    return cara


def button(name, scale, x, y):
    name = escalar(name, scale)
    rect = pygame.Rect(x, y, name.get_width(), name.get_height())
    screen.blit(name, (x, y))
    return rect


def mostrar_informacion(datos):
    y = 10

    for titulo, texto in datos.items():
        titulo_render = fuentetitulo.render(titulo, True, (0, 0, 0))
        texto_render = fuenteabajo.render(texto, True, (0, 0, 0))

        titulo_rect = titulo_render.get_rect(center=(600, y + 20))
        texto_rect = texto_render.get_rect(center=(600, y + 65))

        screen.blit(titulo_render, titulo_rect)
        screen.blit(texto_render, texto_rect)

        y += 90


def disparar(balas):
    for i in range(balas):
        angulo = math.radians(random.randint(0, 359))

        disparos.append(
            {"x": 600, "y": 300, "dx": math.cos(angulo), "dy": math.sin(angulo)}
        )


def actualizar_disparos(delta_time):
    colision = False
    for bala in disparos[:]:
        bala["x"] += bala["dx"] * 400 * delta_time
        bala["y"] += bala["dy"] * 400 * delta_time
        hitbox_bala = pygame.Rect(
            bala["x"], bala["y"], disparo.get_width(), disparo.get_height()
        )
        if hitbox_bala.colliderect(hitbox):
            colision = True
            disparos.remove(bala)
            continue
        screen.blit(disparo, (bala["x"], bala["y"]))
        global iframes
        if iframes > 0:
            iframes -= delta_time

        elif colision == True:
            global vida
            vida -= 1
            iframes = duracion_iframes

        if bala["x"] < -20 or bala["x"] > 1220 or bala["y"] < -20 or bala["y"] > 660:
            disparos.remove(bala)


disparo = escalar(disparo, 2)
cara = escalar(cara, 10)
player = escalar(player, 10)
skin = escalar(skin, 10)
skinnormal = escalar(skinnormal, 10)
heart = escalar(heart, 3)
emptyheart = escalar(emptyheart, 3)
dragon = escalar(dragon, 7)
title = pygame.display.set_caption("Esquiva al Dragón")
icon = pygame.display.set_icon(icon)


skin = change_color(skin, colores[0])


scene = 0


while running:

    delta_time = clock.tick(60) / 1000
    velocidad_cambio = delta_time / duracion_segundos
    if shopm:
        mezcla = min(1.0, mezcla + velocidad_cambio)
    else:
        mezcla = max(0.0, mezcla - velocidad_cambio)
    volumen_tienda = mezcla * mezcla * (3 - 2 * mezcla)
    volumen_menu = 1.0 - volumen_tienda
    screen.fill((255, 255, 255))
    canal1.set_volume(volumen_menu * volumen_musica * volumen_general)
    canal2.set_volume(volumen_tienda * volumen_musica * volumen_general)
    if scene == 0:
        mejorpuntuacionstr = fuentetitulo.render(
            f"Mejor Puntuaciòn: {mejorpuntuacion}", True, (0, 0, 0)
        )
        screen.blit(mejorpuntuacionstr, (950, 10))
        shopm = False
        play_rect = button(play, 5, 520, 100)
        shop_rect = button(shop, 5, 520, 200)
        exit_rect = button(exit, 5, 520, 300)
        info_rect = button(info, 3, 5, 5)
        configuracion_rect = button(configuracion, 2.9, 55, 7)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if play_rect.collidepoint(event.pos):
                        scene = 1
                        vida = 3
                        cooldown_disparos = 5.0
                        heart1, heart2, heart3 = heart, heart, heart
                        cara = escalar(cara, 0.5)
                        player = escalar(player, 0.5)
                        skin = escalar(skin, 0.5)
                        x, y = 0, 0
                        contador = 0
                    elif shop_rect.collidepoint(event.pos):
                        scene = 2
                    elif exit_rect.collidepoint(event.pos):
                        running = False
                    elif info_rect.collidepoint(event.pos):
                        scene = 3
                    elif configuracion_rect.collidepoint(event.pos):
                        scene = 4
    elif scene == 1:
        contador += delta_time
        if mejorpuntuacion < int(contador):
            mejorpuntuacion = int(contador)
        if vida == 2:
            heart3 = emptyheart
        elif vida == 1:
            heart2 = emptyheart
        elif vida == 0:
            heart1 = emptyheart
            scene = 0
            cara = escalar(cara, 2)
            player = escalar(player, 2)
            skin = escalar(skin, 2)
            disparos = []
        titulo_render = fuentetitulo.render(str(int(contador)), True, (0, 0, 0))
        screen.blit(titulo_render, (600, 10))
        screen.blit(skin, (x, y))
        screen.blit(player, (x, y))
        screen.blit(cara, (x, y))
        screen.blit(heart1, (10, 10))
        screen.blit(heart2, (60, 10))
        screen.blit(heart3, (110, 10))
        screen.blit(dragon, (500, 200))
        if iframes > 0:
            iframes -= delta_time

        elif colision == 1:
            vida -= 1
            iframes = duracion_iframes
        hitbox = pygame.Rect(x, y, player.get_width(), player.get_height())
        target1 = pygame.Rect(200, 300, disparo.get_width(), disparo.get_height())
        target2 = pygame.Rect(500, 200, dragon.get_width(), dragon.get_height())
        colision = hitbox.colliderect(target1)
        colision = hitbox.colliderect(target2)
        print(cooldownd)
        if cooldownd <= 0:
            disparar(5 + random.randint(1, 10))
            cooldownd = cooldown_disparos
            cooldown_disparos = max(0.5, cooldown_disparos - 0.5)
        else:
            cooldownd -= delta_time
            if cooldownd % 4 == 0:
                disparar(1)
        actualizar_disparos(delta_time)
        if up == True:
            if y >= 10:
                y -= 350 * delta_time
        if left == True:
            if x >= 0:
                x -= 350 * delta_time
        if down == True:
            if y <= 540:
                y += 350 * delta_time
        if right == True:
            if x <= 1100:
                x += 350 * delta_time
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    up = True
                if event.key == pygame.K_a:
                    left = True
                if event.key == pygame.K_s:
                    down = True
                if event.key == pygame.K_d:
                    right = True
                if event.key == pygame.K_m:
                    shopm = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    up = False
                if event.key == pygame.K_a:
                    left = False
                if event.key == pygame.K_s:
                    down = False
                if event.key == pygame.K_d:
                    right = False
    elif scene == 2:
        shopm = True
        menu_rect = button(menu, 5, 5, 5)
        screen.blit(skin, (520, 200))
        screen.blit(player, (520, 200))
        screen.blit(cara, (520, 200))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if menu_rect.collidepoint(event.pos):
                        scene = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    facen += 1
                    try:
                        cara = change_face(facen)
                    except:
                        facen -= 1
                if event.key == pygame.K_LEFT:
                    facen -= 1
                    try:
                        cara = change_face(facen)
                    except:
                        facen += 1
                if event.key == pygame.K_UP:
                    colorn = (colorn + 1) % len(colores)
                    skin = change_color(skinnormal, colores[colorn])
                if event.key == pygame.K_DOWN:
                    colorn = (colorn - 1) % len(colores)
                    skin = change_color(skinnormal, colores[colorn])
    elif scene == 3:
        menu_rect = button(menu, 5, 5, 5)
        mostrar_informacion(escenas.informacion)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if menu_rect.collidepoint(event.pos):
                        scene = 0
    elif scene == 4:
        menu_rect = button(menu, 5, 5, 5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if menu_rect.collidepoint(event.pos):
                        scene = 0
                    for nombre, rect in sliders.items():
                        if rect.inflate(20, 20).collidepoint(event.pos):
                            arrastrando = nombre
                            break

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    arrastrando = None
        if arrastrando is not None:
            nuevo_volumen = actualizar_slider(
                sliders[arrastrando], pygame.mouse.get_pos()[0]
            )
            if arrastrando == "General":
                volumen_general = nuevo_volumen
            elif arrastrando == "Musica":
                volumen_musica = nuevo_volumen
            elif arrastrando == "Sonidos":
                volumen_sonidos = nuevo_volumen

        dibujar_slider(sliders["General"], volumen_general, "Volumen general")
        dibujar_slider(sliders["Musica"], volumen_musica, "Musica")
        dibujar_slider(sliders["Sonidos"], volumen_sonidos, "Efectos de sonido")
    pygame.display.flip()
pygame.quit()
