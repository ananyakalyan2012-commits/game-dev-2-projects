import pygame
pygame.init()
screen = pygame.display.set_mode((600,600))
screen.fill((255,255,255))
pygame.display.update()

#loading images
ludo = pygame.image.load("match_the_following\\ludo.png")
subway = pygame.image.load("match_the_following\\subwaysurfer.png")
temple = pygame.image.load("match_the_following\\templerun.png")
candy = pygame.image.load("match_the_following\\candycrush.jpg")

# positioning images
screen.blit(ludo,(150,100))
screen.blit(subway,(150,200))
screen.blit(temple,(150,300))
screen.blit(candy,(150,400))

#creating of text
font=pygame.font.SysFont("Times New Roman",35)
text1=font.render("Ludo",True,(0,0,255))
text2=font.render("Subway",True,(255,0,0))
text3=font.render("Temple",True,(0,255,0))
text4=font.render("Candy",True,(0,0,0))

#positioning of text
screen.blit(text1,(400,100))
screen.blit(text2,(400,200))
screen.blit(text3,(400,300))
screen.blit(text4,(400,400))

pygame.display.update()

running = True

while running:
    event = pygame.event.poll()
    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        pygame.display.update()
    elif event.type == pygame.MOUSEBUTTONUP:
        pos2 = pygame.mouse.get_pos()
        pygame.draw.line(screen, (128,115,15), (pos),(pos2),5)
        pygame.draw.circle(screen, (128,115,15), (pos2), 20,1)
    #to quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.display.update()

