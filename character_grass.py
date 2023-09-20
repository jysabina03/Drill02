from pico2d import *
import math
open_canvas()

# fill here

grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y=90
r=180
while (1):
    
    while (1):
        clear_canvas_now()
        grass.draw_now(400,30)
        x = 400+200*(math.sin(r/360*2*math.pi))
        y = 300+200*(math.cos(r/360*2*math.pi))
        r+=5
        character.draw_now(x,y)
        delay(0.05)
        if (r>=360):
            r-=360
        if (r==180):
            break
    x=400
    y=90
    
    while (1):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        if (y==90 and x<750):
            x+=10
        elif (x>=750 and y<500):
            y+=10
        elif (y>=500 and x>50):
            x-=10
        elif (x<=50):
            y-=10
        if (x==400 and y==90):
            break
        delay(0.05)
close_canvas()
