import pygame
import sys
from Bird import Bird
from Pipe import Pipe
from Menu import Menu


pygame.init()
screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Click the Bird - Grupo 11")
clock = pygame.time.Clock()

background_image = pygame.image.load("images/background.jpg")
bird = Bird(100, 300)
pipes = []
menu = Menu()
playing = False
score_file = open("score.txt", "r+")
high_score = int(score_file.read())

font = pygame.font.SysFont("Roboto", 30)

while True:
    screen.blit(background_image, (0, 0))

    for event in pygame.event.get():

        
        if event.type == pygame.QUIT:
            score_file.close()
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.jump()
                if not playing:
                    playing = True
                    pipes.append(Pipe(800))

    bird.update()


    for pipe in pipes:
        pipe.update()
        pipe.score(bird)

    if bird.collide(pipes) or bird.y < 0 or bird.y > 550:
        playing = False
        menu.show()
        if bird.score > high_score:
            high_score = bird.score
            score_file.seek(0)
            score_file.write(str(high_score))
        bird.reset()
        pipes.clear()


    if playing and pipes and 800 - pipes[-1].x > 400: 
        pipes.append(Pipe(800))
    if pipes and pipes[0].x < -100:
        pipes.pop(0)

    bird.draw(screen)
    for pipe in pipes:
        pipe.draw(screen)

    score_text = font.render(f"Puntaje: {bird.score}", True, (63, 77, 114))
    screen.blit(score_text, (10, 10))


    high_score_text = font.render(f"Puntaje más alto: {high_score}", True, (63, 77, 114))

    screen.blit(high_score_text, (10, 30))
    pygame.display.flip()

    clock.tick(60)