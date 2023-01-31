import pygame

class Breakable_Block(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/images/column.png')
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (self.rect.w * 1.3, self.rect.h * 1.3))


class Unbreakable_Block(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/images/column2.png')
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (self.rect.w * 1.3, self.rect.h * 1.3))
