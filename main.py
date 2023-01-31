import pygame
pygame.init()
from characters import Bird
from characters import Pig
from blocks import Breakable_Block
from blocks import Unbreakable_Block
bird = Bird()
pig = Pig()
pig2 = Pig()
blockB1 = Breakable_Block()
blockB2 = Breakable_Block()
blockB3 = Breakable_Block()
blockB4 = Breakable_Block()
blockB5 = Breakable_Block()
blockB6 = Breakable_Block()
blockU1 = Unbreakable_Block()
blockU2 = Unbreakable_Block()
blockU3 = Unbreakable_Block()


# fenetre du jeu
background = pygame.image.load('assets/images/background2.jpg')
icon = pygame.image.load('assets/images/red-bird.png')
screen = pygame.display.set_mode((1442, 719))
pygame.display.set_caption("Angry Birds")
pygame.display.set_icon(icon)


# transformation des blocs
blockB2.image = pygame.transform.scale(blockB2.image, (blockB2.rect.w + 8, blockB2.rect.h + 70))
blockB2.image = pygame.transform.rotate(blockB2.image, 90)
blockU1.image = pygame.transform.scale(blockU1.image, (blockU1.rect.w + 8, blockU1.rect.h + 70))
blockU1.image = pygame.transform.rotate(blockU1.image, 90)
blockB6.image = pygame.transform.scale(blockB6.image, (blockB6.rect.w + 8, blockB6.rect.h + 70))
blockB6.image = pygame.transform.rotate(blockB6.image, 90)


# boucle du jeu
running = True
while running:
    # actualisation de la fenetre
    pygame.display.flip()

    # affichage de l'arriere plan
    screen.blit(background, (0, 0))

    # affichage de l'oiseau
    screen.blit(bird.image, bird.rect)

    # affichage des cochon
    screen.blit(pig.image, (pig.rect.x, 350))
    screen.blit(pig2.image, (pig2.rect.x, 600))

    # affichage des blocs
    screen.blit(blockB1.image, (969, 340))
    screen.blit(blockB2.image, (969, 317))
    screen.blit(blockB3.image, (1090, 340))
    screen.blit(blockB4.image, (969, 470))
    screen.blit(blockB5.image, (1090, 470))
    screen.blit(blockB6.image, (969, 574))
    screen.blit(blockU1.image, (969, 447))
    screen.blit(blockU2.image, (969, 600))
    screen.blit(blockU3.image, (1090, 600))

    # debug
    souris = pygame.mouse.get_pos()

    # boucle d'évenements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            # debug
            if event.key == pygame.K_m:
                print(souris)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                bird.lancer()





