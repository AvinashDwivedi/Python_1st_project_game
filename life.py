import pygame
from pygame.sprite import Sprite

class Life(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.image = pygame.image.load(r"E:\python_progg\project1\game_objects\heart.bmp")

        self.screen_rect = self.screen.get_rect()
        self.rect = self.image.get_rect()

    def blitme(self):
        self.screen.blit(self.image, self.rect)