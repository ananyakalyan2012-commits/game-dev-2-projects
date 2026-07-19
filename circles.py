import pygame
screen=pygame.display.set_mode((600,600))
screen.fill((26,156,179))

pygame.display.update()

#creating class
class Circle:
    #creating a constructor
    def __init__(self,color,pos,radius,width):
        self.circle_clr = color
        self.circle_pos = pos
        self.circle_rad = radius
        self.circle_wth = width
        self.circle_surface=screen
    
    def draw(self):
        self.draw_circle=pygame.draw.circle(self.circle_surface,
                                            self.circle_clr,
                                            self.circle_pos,
                                            self.circle_rad,
                                            self.circle_wth)
        

#creating objects
redcircle = Circle("red",(70,70),50,0)
greencircle = Circle("green",(180,180),70,0)
bluecircle = Circle("blue",(350,350),120,0 )

running=True
while running:
    redcircle.draw()
    greencircle.draw()
    bluecircle.draw()
    pygame.display.update()


    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            running=False

