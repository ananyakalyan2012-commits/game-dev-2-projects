import pygame
screen= pygame.display.set_mode((600,600))
screen.fill((72,236,189))
pygame.display.update()
white = (255,255,255)
blue = (0,0,255)

class Circle:
    def __init__(self,color,pos,rad,width):
        self.circle_color=color
        self.circle_pos=pos
        self.circle_rad=rad
        self.circle_width=width
        self.circle_surface=screen
    
    def draw(self):
        self.draw_circle=pygame.draw.circle(self.circle_surface,
                                            self.circle_color,
                                            self.circle_pos,
                                            self.circle_rad,
                                            self.circle_width)
        
    def grow(self,r):
        self.circle_rad += r
        self.draw_circle=pygame.draw.circle(self.circle_surface,
                                            self.circle_color,
                                            self.circle_pos,
                                            self.circle_rad,
                                            self.circle_width)
        
c1 = Circle((255,0,0),(300,300),50,5)
running = True
while running:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            running=False

        if event.type==pygame.MOUSEBUTTONDOWN:
                c1.draw()
                pygame.display.update()

        elif event.type==pygame.MOUSEBUTTONUP:
             c1.grow(5) 
             pygame.display.update()       



