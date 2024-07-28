#!/usr/bin/python
import pygame

pygame.init()
pygame.display.set_caption('Credits')
screen = pygame.display.set_mode((800, 600))
font = pygame.font.Font("BricolageGrotesque-VariableFont_opsz,wdth,wght.ttf", 40)
clock = pygame.time.Clock()

def main():

    credit_list = ["Credits - The Snake Game"," ","Logic - Arnav Mehra","Colouring - Arnav Mehra", "Programming - Arnav Mehra", "Configuration File - Zebra Robotics", "My Sanity - Gone"]

    texts = []
    for i, line in enumerate(credit_list):
        print(i, line)
        text = font.render(line, 1, (10, 10, 10))
        text_rectangle = text.get_rect(centerx=screen.get_rect().centerx, y=screen.get_rect().bottom + i * 45)
        texts.append((text_rectangle, text))

    running = True

    while running:

        screen.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        for text_rectangle, text in texts:
            text_rectangle.move_ip(0, -10)
            screen.blit(text, text_rectangle)

        if not screen.get_rect().collidelistall([text_rectangle for (text_rectangle, text) in texts]):
            running = False
            pygame.quit()

        pygame.display.update()

        clock.tick(60)

main()