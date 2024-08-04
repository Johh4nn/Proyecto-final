import pygame
import sys
from ajustes import Ajustes
from tanke import Tanke
from disparo import Bala
from enemigo import Enemigo

class prueba2:
    def __init__(self):
        pygame.init()
        self.ajustes = Ajustes()
        self.screen = pygame.display.set_mode((self.ajustes.anchura,self.ajustes.altura))
        self.fondo = pygame.image.load(self.ajustes.fondo)
        pygame.display.set_caption("TANK 2024")
        self.tanke = Tanke(self)
        self.balas = pygame.sprite.Group()
        self.enemigos = pygame.sprite.Group()
        self.enviarEnemigos()

    def enviarEnemigos(self):
        tankeMalvado = Enemigo(self)
        self.enemigos.add(tankeMalvado)


    def eliminarEnemigosViejos(self):
        for enemigo in self.enemigos.copy():
            if enemigo.rect.bottom >= self.ajustes.altura:
                self.enemigos.remove(enemigo)
                self.enviarEnemigos()

    def actualizarEnemigos(self):
        self.enemigos.update()

    def actualizarPantalla(self):
        self.screen.blit(self.fondo,(0,0))
        self.tanke.blime()
        for bala in self.balas.sprites():
            bala.pintarDisparo()
        self.enemigos.draw(self.screen)
        pygame.display.flip()

    def dispararbala(self):
        if len(self.balas)< self.ajustes.balasPermitidas:
            nuevaBala = Bala(self)
            self.balas.add(nuevaBala)
    

    def elmininarDisparosviejos(self):
        for bala in self.balas.copy():
            if bala.rect.bottom <= 0:
                self.balas.remove(bala)

    def comprobarEventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.tanke.moviendoDerecha = True
                    
                elif event.key == pygame.K_LEFT:
                    self.tanke.moviendoIzquierda = True

                    
                elif event.key == pygame.K_UP:
                    self.tanke.moviendoArriba = True

                    
                elif event.key == pygame.K_DOWN:
                    self.tanke.moviendoAbajo = True

                elif event.key == pygame.K_SPACE:
                    self.dispararbala()
                
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.tanke.moviendoDerecha = False
                elif event.key == pygame.K_LEFT:
                    self.tanke.moviendoIzquierda = False
                elif event.key == pygame.K_UP:
                    self.tanke.moviendoArriba = False
                elif event.key == pygame.K_DOWN:
                    self.tanke.moviendoAbajo = False

    def run_game(self):
        while True:
            self.comprobarEventos()
            self.tanke.actualizar()
            self.balas.update()
            self.elmininarDisparosviejos()
            self.actualizarEnemigos()
            self.eliminarEnemigosViejos()
            self.actualizarPantalla()
            




if __name__=='__main__':
    dc = prueba2()
    dc.run_game()