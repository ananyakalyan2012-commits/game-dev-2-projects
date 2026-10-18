import pygame
screen = pygame.display.set_mode((600,600))
screen.fill((255,255,255))
pygame.display.update()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill("blue")

    #to draw line
    start_pos = (50,200)
    end_pos = (150,290)
    pygame.draw.line(screen,(255,255,0),start_pos, end_pos,5)

    #hollow circle
    pygame.draw.circle(screen,(255,255,9),(100,200),30,5)
    pygame.draw.circle(screen,(155,145,155), (300,250),30,0)#filled circle
    #to draw 6 side polygon
    points = [(25,75),(50,75),(65,100),(50,125),(25,125),(10,100)] #6 vertices
    pygame.draw.polygon(screen,"pink",points)

    #to draw rectangle
    pygame.draw.rect(screen,"red",(200,100,100,50),5)

    #to draw ellipse
    pygame.draw.ellipse(screen,"green",(300,100,100,50),5)

    pygame.display.update()
                                            


