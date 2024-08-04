import pygame
class Tanke:
    def __init__(self,dc_game):
        self.screen = dc_game.screen
        self.screen_rect = dc_game.screen.get_rect()

        self.imagen = pygame.image.load('imagenes/tanque1.png')
        


        self.rect = self.imagen.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        

        self.moviendoIzquierda = False
        self.moviendoDerecha = False
        self.moviendoArriba = False
        self.moviendoAbajo = False

    def blime(self):
        self.screen.blit(self.imagen,self.rect)

    def actualizar(self):
        if self.moviendoDerecha:
            self.rect.x +=1
        if self.moviendoIzquierda:
            self.rect.x -=1
        if self.moviendoArriba:
            self.rect.y -=1
        if self.moviendoAbajo:
            self.rect.y +=1