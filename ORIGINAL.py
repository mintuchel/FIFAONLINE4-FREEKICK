from vpython import *

import random

ground = box(pos=vec(0,0,0),size=vec(70,0.1,70),color=color.green)

# box center = mid position -> if height changes pos.y have to change
post1 = box(pos=vec(-4,2,-20),axis=vec(1,0,0),size=vec(0.5,4,2),color=color.red)
post2 = box(pos=vec(4,2,-20),axis=vec(1,0,0),size=vec(0.5,4,2),color=color.red)
post3 = box(pos=vec(0,4,-20),axis = vec(1,0,0),size=vec(8.5,0.5,2),color=color.red)

# post center 정사영
post2dpos = vec(0,0,-20)

ball = sphere(pos=vec(random.randint(-15,15),0.2,random.randint(8,15)),radius=0.2,color=color.white)
ball.m = 1
ball.r = 0.2