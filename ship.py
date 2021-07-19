import pygame

class Ship:
    """ all the gamers ship functionality is here """
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.image = pygame.image.load(r"game_objects\ship_nbg.bmp")

        self.settings = ai_game.settings

        self.screen_rect = ai_game.screen.get_rect()
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        self.rect.x = self.x