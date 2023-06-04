from vpython import *

import random

scene.background = color.white

ground = box(pos=vec(0,0,0),size=vec(50,0.1,50),color=color.green)

# box center = mid position -> if height changes pos.y have to change
post1 = box(pos=vec(-4,2,-20),axis=vec(1,0,0),size=vec(0.5,4,2),color=color.red)
post2 = box(pos=vec(4,2,-20),axis=vec(1,0,0),size=vec(0.5,4,2),color=color.red)
post3 = box(pos=vec(0,4,-20),axis = vec(1,0,0),size=vec(8.5,0.5,2),color=color.red)

# post center 정사영
post2dpos = vec(0,0,-20)

ball = sphere(pos=vec(random.randint(-15,15),0.2,random.randint(8,15)),radius=0.2,color=color.white)
ball.m = 1
ball.r = 0.2

right_zd = 0
left_zd = 0
direct_d = 0

dpower = 5 # power+=dpower

scene.waitfor('keydown')

while True:
    rate(100)  # Limit the loop rate for smooth animation

    s = keysdown()  # Get the keys that are currently pressed

    print(s)
    if 'z' in s and 'right' in s :
        right_zd += dpower
        print("right zd Power :", right_zd)
    else if 'z' in s and 'left' in s :
        left_zd += dpower
        print("left zd Power :", left_zd)
    else if 'q' in s and 'd' in s :
        direct_d +=dpower
        print("direct shoot :",direct_d)