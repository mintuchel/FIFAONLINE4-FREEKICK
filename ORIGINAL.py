from vpython import *
 
import random

scene = canvas(width = 1400, height = 600, title = "피파온라인4")
scene.background = color.white


def shootbtn(b) :
    b.disabled=True
    return b.disabled

btnShoot = button(text="shoot",bind=shootbtn)

# setting

ground = box(pos=vec(0,0,0),size=vec(50,0.1,50),color=color.green)

# box center = mid position -> if height changes pos.y have to change
post1 = box(pos=vec(-4,2,-20),axis=vec(1,0,0),size=vec(0.5,4,2),color=color.red) # left post
post2 = box(pos=vec(4,2,-20),axis=vec(1,0,0),size=vec(0.5,4,2),color=color.red) # right post
post3 = box(pos=vec(0,4.25,-20),axis = vec(1,0,0),size=vec(8.5,0.5,2),color=color.red) # top post

# post center 정사영
post2dpos = vec(0,0,-20)

ball = sphere(pos=vec(random.randint(-15,15),0.3,random.randint(8,15)),radius=0.3,color=color.white)
ball.m = 1
ball.r = 0.2

# ball pos 정사영
ball2dpos = ball.pos - vec(0,0.3,0)

eyedir = hat(ball2dpos-post2dpos)
eye2dpos = vec(ball.pos.x/(ball.pos.z+20)*(18+20),0,18)
eyepos = eye2dpos + vec(0,2,0)

shootdir = arrow(pos=ball2dpos,axis=4*hat(ball2dpos-eye2dpos),shaftwidth = 0.15,color=color.black)

scene.camera.pos = eyepos
scene.camera.axis = shootdir.axis


# update camera control to only respond to 'left' and 'right' keystroke
angle = radians(1)
axis = vec(0,1,0)
origin = ball.pos

while !btnShoot.disabled :
    rate(100)
        
    s = keysdown()
    print("You pressed the key", s)  
    
    if 'left' in s: 
        scene.camera.rotate(angle=radians(-1), axis=axis, origin=origin)
        shootdir.axis=6*hat(scene.camera.axis)
    if 'right' in s: 
        scene.camera.rotate(angle=radians(1), axis=axis, origin=origin)
        shootdir.axis=6*hat(scene.camera.axis)

# the most important variable
# used in final shooting
shootvec = shootdir.axis

right_zd = 0
left_zd = 0
direct_d = 0

dpower = 1 # power+=dpower

scene.waitfor('keydown')

while True:
    rate(100)  # Limit the loop rate for smooth animation
    
    s = keysdown()  # Get the keys that are currently pressed
    
    print(s)
    if 'z' in s and 'right' in s :
        right_zd += dpower
        print("right zd Power :", right_zd)
    else if  'z' in s and 'left' in s :
        left_zd += dpower
        print("left zd Power :", left_zd)
    else if 'q' in s and 'd' in s :
        direct_d +=dpower
        print("direct shoot :",direct_d)
    else if s==[] :
        break