import pygame
import time

pygame.init()

WIDTH=600
HEIGHT=600

output_screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Birthday Greeting Card")#title
running=True

while running:
    img = pygame.image.load("")
    image = pygame.transform.scale(img, (WIDTH,HEIGHT))
    font = pygame.font.SysFont("Times New Roman",72)
    text=font.render("Happy",True, (0,255,0),"yellow")
