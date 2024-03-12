import pygame

class Level:
    def __init__(self):

        # setup de sprites
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()

    def run(self):
        # update and draw the game
        self.visible_sprites.draw(self.display_surface)