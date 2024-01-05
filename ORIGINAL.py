Web VPython 3.2

# power 35-40 정도면 인게임에서 구석으로 꽂힘
# 여기서도 35-40이면 들어감

# ball2dpos = ball 정사영
# eye2dpos = eye 정사영
 
import random

scene = canvas(width = 1400, height = 600, title = "피파온라인4")
scene.background = color.white

# constants
g = 9.8
rho = 1.204 # air density
Cd = 0.3 # air resistance
Cm = 1 # air magnus
w = 15*pi #각속도

def shootbtn(b) :
    b.disabled=True
    return b.disabled

def check_groundhit() :
    if ball.pos.y < 0.3 :
        ball.pos.y = 0.3
        ball.v.y = -0.8*ball.v.y

def check_goalposthit() :
    # right left post hit
    if 3.75 <= abs(ball.pos.x) <= 4.25 and 0 <= ball.pos.y <= 4 and -21 <= ball.pos.z <= -19 : 
        ball.v.z = -0.3*ball.v.z
    # top post hit
    elif -3.75 < ball.pos.x < 4.25 and 4 < ball.pos.y < 4.5 and -21 <= ball.pos.z <= -19 : 
        ball.v.y = 0.8*ball.v.y
        ball.v.z = -0.5*ball.v.z

def check_goal() :
    if abs(ball.pos.x) < 3.5 and 0 <= ball.pos.y < 4 and -21<= ball.pos.z <=-19 : goal_label.visible = True

def check_wallhit() :
    if mag(ball.pos - wall.pos) < 1.2 :
        ball.v.y = 0.8*ball.v.y
        ball.v.z = -0.5*ball.v.z
    
    
    
def shoot_directd(direct_d) :

    # direct_d have no deceleration in the given power
    ball.v = direct_d*hat(shootvec)+vec(0,direct_d/5,0)
    
    dt = 0.01
    t = 0
    
    while t<2.5 :
        rate(1/dt)
        ball.v+=vec(0,-g*ball.m,0)*dt
        ball.pos += ball.v*dt
        
        #check_wallhit()
        check_groundhit()
        check_goalposthit()
        check_goal()
        
        t+=dt
        
        
def shoot_rightzd(right_zd) :
    
    ball.v = right_zd/2*hat(shootvec)+vec(right_zd/3,right_zd/3,-right_zd/4)
    
    dt = 0.01
    t = 0
    
    while t<2.5 : 
        rate(1/dt)
        
        Fg = vec(0,-g*ball.m,0)
        Fd = -0.5*Cd*rho*(pi*ball.r**2)*mag(ball.v)**2*hat(ball.v)
        Fm = 0.5*Cm*rho*(pi*ball.r**2)*ball.r*mag(ball.v)*w*cross(vec(0,1,0),hat(ball.v))
    
        Fnet = Fg+Fd+Fm
        ball.a = Fnet/ball.m
        
        ball.v+=ball.a*dt
        ball.pos+=ball.v*dt

        #check_wallhit()
        check_groundhit()
        check_goalposthit()
        check_goal()
        
        t+=dt
        
def shoot_leftzd(left_zd) :

    ball.v = left_zd/2*hat(shootvec)+vec(-left_zd/3,left_zd/3,-left_zd/4)
    
    dt = 0.01
    t = 0
    
    while t<2.5 : 
        rate(1/dt)
        
        Fg = vec(0,-g*ball.m,0)
        Fd = -0.5*Cd*rho*(pi*ball.r**2)*mag(ball.v)**2*hat(ball.v)
        Fm = 0.5*Cm*rho*(pi*ball.r**2)*ball.r*mag(ball.v)*w*cross(vec(0,-1,0),hat(ball.v))
    
        Fnet = Fg+Fd+Fm
        ball.a = Fnet/ball.m
        
        ball.v+=ball.a*dt
        ball.pos+=ball.v*dt
        
        #check_wallhit()
        check_groundhit()
        check_goalposthit()
        check_goal()
           
        t+=dt
        
def set_wall(linepos) :
    global player1, player2, player3, player4
    global head1, head2, head3, head4
    
    midpoint = linepos+vec(0,0.75,0)
    wall_axis = cross(vec(0,1,0), shootdir.axis)
    
    # have problems here
    startpoint = midpoint - 1.05*hat(wall_axis)
    
    player1 = box(pos = startpoint, axis = wall_axis, size = vec(0.6,1.5,0.2), texture = textures.wood)
    head1 = sphere(pos = startpoint + vec(0,0.75+0.3,0), radius = 0.3, texture = textures.wood)
    
    startpoint+= hat(wall_axis)*0.7
    
    player2 = box(pos=startpoint, axis = wall_axis, size = vec(0.6,1.5,0.2), texture = textures.wood)
    head2 = sphere(pos = startpoint + vec(0,0.75+0.3,0), radius = 0.3, texture = textures.wood)
    
    startpoint+= hat(wall_axis)*0.7
    
    player3 = box(pos=startpoint, axis = wall_axis, size = vec(0.6,1.5,0.2), texture = textures.wood)
    head3 = sphere(pos = startpoint + vec(0,0.75+0.3,0), radius = 0.3, texture = textures.wood)
    
    startpoint+= hat(wall_axis)*0.7
    
    player4 = box(pos=startpoint, axis = wall_axis, size = vec(0.6,1.5,0.2), texture = textures.wood)
    head4 = sphere(pos = startpoint + vec(0,0.75+0.3,0), radius = 0.3, texture = textures.wood)

def erase_wall() :
    player1.visible = False
    player2.visible = False
    player3.visible = False
    player4.visible = False
    
    head1.visible = False
    head2.visible = False
    head3.visible = False
    head4.visible = False
    
def check_wallhit() :
    
    if
    if 3.75 <= abs(ball.pos.x) <= 4.25 and 0 <= ball.pos.y <= 4 and -21 <= ball.pos.z <= -19 : 
        ball.v.z = -0.3*ball.v.z
    # top post hit
    elif -3.75 < ball.pos.x < 4.25 and 4 < ball.pos.y < 4.5 and -21 <= ball.pos.z <= -19 : 
        ball.v.y = 0.8*ball.v.y
        ball.v.z = -0.5*ball.v.z
        
# setting
    
ground = box(pos=vec(0,0,0),size=vec(50,0.1,50),color=color.green)

# box center = mid position -> if height changes pos.y have to change
post1 = box(pos=vec(-4,2,-20),axis=vec(1,0,0),size=vec(0.5,4,2),color=color.red) # left post
post2 = box(pos=vec(4,2,-20),axis=vec(1,0,0),size=vec(0.5,4,2),color=color.red) # right post
post3 = box(pos=vec(0,4.25,-20),axis = vec(1,0,0),size=vec(8.5,0.5,2),color=color.red) # top post

# post center 정사영
post2dpos = vec(0,0,-20)

btnShoot = button(text="shoot",bind=shootbtn)

goal_label = label(pos=post2dpos+vec(0,10,0),box=False,height = 30,text='GOAL!',color=color.blue,visible = False)
miss_label = label(pos=post2dpos+vec(0,10,0),box=False,height=30,text='프리킥더연습하세요',color=color.blue,visible =False)

while True :
    ball=sphere(pos=vec(random.randint(-15,15),0.3,random.randint(8,15)),radius=0.25,color=color.white)
    ball.m = 1
    ball.r = 0.2

    ball2dpos = ball.pos - vec(0,0.25,0)

    eyedir = hat(ball2dpos-post2dpos)
    eye2dpos = vec(ball.pos.x/(ball.pos.z+20)*(18+20),0,18)
    eyepos = eye2dpos + vec(0,2,0)

    shootdir = arrow(pos=ball2dpos,axis=6*hat(ball2dpos-eye2dpos),shaftwidth=0.15,color=color.black)

    scene.camera.pos = eyepos
    scene.camera.axis = shootdir.axis
    
    linepos = ball.pos + hat(shootdir.axis)*10 - vec(0,0.3,0)
    
    # setting defender wall
    set_wall(linepos)
    
    angle = radians(1)
    axis = vec(0,1,0)
    origin = ball.pos

    while btnShoot.disabled==False :

        rate(100)
    
        if btnShoot.disabled : break

        s = keysdown()
        #print("You pressed the key", s)  
    
        if 'left' in s: 
            scene.camera.rotate(angle=radians(1), axis=axis, origin=origin)
            shootdir.axis=6*hat(scene.camera.axis)
        if 'right' in s: 
            scene.camera.rotate(angle=radians(-1), axis=axis, origin=origin)
            shootdir.axis=6*hat(scene.camera.axis)

    
    # the most important variable
    # used in final shooting
    shootvec = shootdir.axis

    right_zd = 0
    left_zd = 0
    direct_d = 0

    dpower = 1 # power+=dpower

    scene.waitfor('keydown')
    
    while btnShoot.disabled :
        rate(100)  # Limit the loop rate for smooth animation
    
        s = keysdown()  # Get the keys that are currently pressed
            
        print(s)
        if 'z' in s and 'right' in s :
            right_zd += dpower
            print("right zd Power :", right_zd)
        elif 'z' in s and 'left' in s :
            left_zd += dpower
            print("left zd Power :", left_zd)
        elif 'q' in s and 'd' in s :
            direct_d +=dpower
            print("direct shoot :",direct_d)
        elif s==[] :
            break

    if right_zd > 0 :
        shoot_rightzd(right_zd)
    elif left_zd > 0 :
        shoot_leftzd(left_zd)
    elif direct_d > 0 :
        shoot_directd(direct_d)
    
    if !goal_label.visible :
        miss_label.visible = True
        
    scene.waitfor('click')
    goal_label.visible = False
    miss_label.visible = False
    btnShoot.disabled = False
    erase_wall()
    ball.visible = False
    shootdir.visible = False