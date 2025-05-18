import pgzrun
from time import time
from random import randint

WIDTH=800
HEIGHT=600

start_time=0
total_time=0
current_satellite=0
number_of_satellites=8
satellites=[]
lines=[]

def create_satellites():
    global start_time
    for count in range(number_of_satellites):
        satellite=Actor("satellite")
        satellite.pos=randint(40,WIDTH-40),randint(40,HEIGHT-40)
        satellites.append(satellite)
    start_time=time()

def draw():

    global total_time
    screen.blit("bg",(0,0))
    num=1
    for satellite in satellites:
        satellite.draw()
        screen.draw.text(str(num),(satellite.pos[0],satellite.pos[1]+20))
        num+=1
    for line in lines:
        screen.draw.line(line[0],line[1],"white")

    if current_satellite<number_of_satellites:
        total_time=time()-start_time
        screen.draw.text(str(round(total_time,1)),(10,10),fontsize=30)
    else:
        screen.draw.text(str(round(total_time,1)),(10,10),fontsize=30)

    

def update():
    
    pass

create_satellites()


      
        









pgzrun.go()
    




