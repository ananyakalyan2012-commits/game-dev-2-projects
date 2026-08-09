import pygame
screen=pygame.display.set_mode((600,600))
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
yellow=(255,255,0)
white=(255,255,255)
screen.fill(white)

class Mycircle:
    def __init__(self,clr,pos,rad,wth=0):
        self.circle_clr=clr
        self.circle_pos=pos
        self.circle_rad=rad
        self.circle_wth=wth
        self.circle_scr=screen

    def draw(self): 
           pygame.draw.circle(self.circle_scr,
                              self.circle_clr,
                              self.circle_pos,
                              self.circle_rad,
                              self.circle_wth)
    def grow(self,r):
          self.circle_rad += r
          pygame.draw.circle(self.circle_scr,
                              self.circle_clr,
                              self.circle_pos,
                              self.circle_rad,
                              self.circle_wth)

pos = (300,300)
rad = 60
wth = 3

#creating object
rcircle = Mycircle(red, (pos),rad,wth) 
ycircle= Mycircle(yellow, (pos),rad + 100,5) 

running= True

while running:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running= False

        if event.type == pygame.MOUSEBUTTONDOWN:
             rcircle.draw()
             ycircle.draw()
             pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP:
             rcircle.grow(6)     
             ycircle.grow(3)
             pygame.display.update()
        elif event.type == pygame.MOUSEMOTION:
             pos=pygame.mouse.get_pos()
             gcircle = Mycircle(green, pos,5)
             gcircle.draw()
             pygame.display.update()
                  
               
             
            
         


     


        
        
