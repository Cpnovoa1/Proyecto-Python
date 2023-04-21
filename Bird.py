import pygame

class Bird:
    def __init__(self,x,y):
        self.x=x 
        self.y=y 
        self.vel = 0 
        self.acc= 0.5 
        self.score= 0 
        self.image = pygame.Surface((50,50)) 

        self.image = pygame.image.load("images/bird.png")
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect=self.image.get_rect() 

    def update(self):
        self.vel += self.acc
        self.y += self.vel 
        self.rect.center = (self.x,self.y)

    def jump(self):
        self.vel=-10 

    def draw(self, screen):
        screen.blit(self.image,self.rect)

    def collide(self, pipes):
        for pipe in pipes:
            if self.rect.colliderect(pipe.top_rect) or self.rect.colliderect(pipe.bottom_rect):
                return True
            
            
        return False

    def reset(self):
        self.y = 300
        self.vel = 0
        self.score = 0