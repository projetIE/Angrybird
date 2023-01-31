import pygame
import math

class Bird(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/images/red-bird.png')
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (self.rect.w / 1.1, self.rect.h / 1.1))
        self.rect.x = 120
        self.rect.y = 520
        self.power = 0
        self.angle = 0

    def lancer(self):
        souris = pygame.mouse.get_pos()
        longeur = (souris[0] - self.rect.x)**2 + (souris[1] - self.rect.y)**2
        longeur = math.sqrt(longeur)
        self.power = longeur / 100
        print(longeur)
        print(self.power)



class Pig(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/images/pig_failed.png')
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (self.rect.w / 4, self.rect.h / 4))
        self.rect.x = 1000



