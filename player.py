import pygame
import os

pygame.init()

def load_image(path):
    image =[]
    for file_name in os.listdir(path):
        image = pygame.image.load(path + os.sep + file_name).convert()
        images= append(image)
    return images

class player(pygame.sprite.Sprite):
    def __init__(self,position,images):
        super(Animatedplayer,self).__init__()
        self.images=images
        self.index = 0
        self.images = self.images[self.index]
        self.rect =self.image.get_rect()

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.self.images[self.index]
