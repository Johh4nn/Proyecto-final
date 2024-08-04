import pygame, sys
from  pygame.locals import *


#Tamaño de pantalla 
pygame.init()
W,H = 1000,600
pantalla = pygame.display.set_mode((W,H))



pygame.display.set_caption('Tanque 1990')
icon = pygame.image.load("imagenes/tanque.png")
fondo = pygame.image.load("imagenes/suelo.jpg").convert()
x=0
pygame.display.set_icon(icon)

#Personaje
quieto = pygame.image.load('imagenes/tanque1.png')

caminaDerecha = [pygame.image.load('imagenes/tanque1D.png'),
                pygame.image.load('imagenes/tanque2D.png'),
                pygame.image.load('imagenes/tanque1D.png'),
                pygame.image.load('imagenes/tanque2D.png'),]

caminaizquierda =  [pygame.image.load('imagenes/tanque1I.png'),
                pygame.image.load('imagenes/tanque2I.png'),
                pygame.image.load('imagenes/tanque1I.png'),
                pygame.image.load('imagenes/tanque2I.png')]

caminaArriba =  [pygame.image.load('imagenes/tanque1.png'),
                pygame.image.load('imagenes/tanque2.png'),
                pygame.image.load('imagenes/tanque1.png'),
                pygame.image.load('imagenes/tanque2.png')]

caminaAbajo =  [pygame.image.load('imagenes/tanque1A.png'),
                pygame.image.load('imagenes/tanque2A.png'),
                pygame.image.load('imagenes/tanque1A.png'),
                pygame.image.load('imagenes/tanque2A.png')]

x= 0
px = 50
py = 200
ancho = 40
velocidad = 10

reloj = pygame.time.Clock()
#Varibale direccion
izquierda = False
derecha = False
abajo = False
arriba = False


#pasos
cuentaPasos = 0

def recargarPantalla():
    #Variables globales
    global cuentaPasos
    global x
    
    #Fondo de movimiento
    x_relativa = x % fondo.get_rect().width
    pantalla.blit(fondo,(x_relativa - fondo.get_rect().width,0))
    if x_relativa < W:
        pantalla.blit(fondo,(x_relativa,0))
        x -= 1
    #Contador de pasos
    if cuentaPasos + 1 >= 5 :
        cuentaPasos = 0
    #movimiento a la izquierda
    if izquierda:
        pantalla.blit(caminaizquierda[cuentaPasos // 1], (int(px), int(py)))
        cuentaPasos += 1
    elif derecha:
        pantalla.blit(caminaDerecha[cuentaPasos // 1], (int(px),int(py)))
        cuentaPasos +=1
    elif arriba:
        pantalla.blit(caminaArriba[cuentaPasos // 1], (int(px),int(py)))
        cuentaPasos +=1
    elif abajo:
        pantalla.blit(caminaAbajo[cuentaPasos // 1], (int(px),int(py)))
        cuentaPasos +=1
    else:
        pantalla.blit(quieto,(int(px),int(py)))

ejecuta = True

#Bucle de ventana y controles y accion
while ejecuta:
    reloj.tick(18)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecuta= False

    keys = pygame.key.get_pressed()

    #Tecla A - Movimiento a la izquierda
    if keys[pygame.K_a] and px > velocidad:
        px -= velocidad
        izquierda = True
        derecha= False
    #Tecla D - Movimiento a la derecha
    elif keys[pygame.K_d] and px < 900 - velocidad -ancho:
        px += velocidad
        izquierda = False
        derecha = True

    else:
        izquierda = False
        derecha = False
        cuentaPasos = 0 

    #Tecla W - Movimiento hacia arriba
    if keys[pygame.K_w] and py > 100:
        py -= velocidad
        abajo = False
        arriba = True
    
    #Tecla S - Movmiento hacia abajo
    if keys[pygame.K_s] and py < 900:
        py += velocidad
        abajo = True
        arriba = False

    #Actualizar la ventana
    pygame.display.update()
    recargarPantalla()

pygame.quit()
