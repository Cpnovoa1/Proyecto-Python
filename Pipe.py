import pygame
import random

class Pipe:
    def __init__(self,x):
        self.x=x
        self.gap=150 
        self.gap_y=random.randint(200, 400)
        self.vel=-5 
        self.passed=False 

        self.top_image = pygame.Surface((100, 600)) 
        self.top_image.fill((87, 179, 116)) 
        self.top_rect=self.top_image.get_rect() 
        
        self.bottom_image= pygame.Surface((100, 600)) 
        self.bottom_image.fill((87, 179, 116)) 
        self.bottom_rect=self.bottom_image.get_rect() 

    def update(self):
        self.x += self.vel
        self.top_rect.bottomleft = (self.x, self.gap_y-self.gap/2) 
        self.bottom_rect.topleft = (self.x, self.gap_y+self.gap/2) 

    def draw(self,screen):
        screen.blit(self.top_image, self.top_rect) 
        screen.blit(self.bottom_image, self.bottom_rect) 

    def score(self,bird):
        if not self.passed and bird.x > self.x+100:
            bird.score+=1
            self.passed=True