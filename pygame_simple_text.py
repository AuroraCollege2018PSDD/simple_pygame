import pygame as P

#initialise pygame
P.init()


# parameters
screen_size = width, height = 800, 600

# Define the colors we will use in RGB format
black = [ 0, 0, 0]
white = [255 ,255 ,255]
blue = [ 0, 0 ,255]
light_blue = [125,125,255]
green = [ 0 ,255 , 0]
red = [255 , 0, 0]

screen = P.display.set_mode(screen_size)
font = P.font.Font(None,30)

text = font.render("Hello World",1,red, light_blue)
screen.blit(text,[100,100])
P.display.flip()


over = True

while over:

    event = P.event.poll() #did the player do something?
    if event.type == P.QUIT: #player clicked close so quit
        over = False
        P.quit()
