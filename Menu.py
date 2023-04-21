import pygame
import sys

class Menu:
    def __init__(self):
        self.image = pygame.Surface((800, 600))
        background_image = pygame.image.load("images/game_over.jpg")
        self.image.blit(background_image, (0, 0))
        self.rect=self.image.get_rect() 

        self.font = pygame.font.SysFont("Roboto", 70) 
        self.title_text = self.font.render("Click the Bird", True, (63,77,114))
        self.title_rect=self.title_text.get_rect() 
        self.title_rect.center = (400,200) 

        self.instruction_text = self.font.render("Presiona 'ESPACIO' para jugar", True, (73,204,126)) 
        self.instruction_rect=self.instruction_text.get_rect()
        self.instruction_rect.center = (400,400) 

        self.font = pygame.font.SysFont("Roboto", 45) 
        self.footer_text = self.font.render("Desarrollado por: Grupo 11", True, (217,229,243)) 
        self.footer_rect=self.footer_text.get_rect() 
        self.footer_rect.center = (400,575) 

    def draw(self,screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.title_text, self.title_rect)
        screen.blit(self.instruction_text, self.instruction_rect) 
        screen.blit(self.footer_text, self.footer_rect) 

    def show(self):
        menu_window = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Click the Bird - Menu")
        menu_window.fill((135,206, 235))
        
        self.draw(menu_window)
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return