from visual import *
import ruler

g=9.8 # g = 9.8 m/s^2
size = 0.25 # ball radius = 0.25 m
mass = 10
scene = display(title='bouncing projectile', center = (0,5,0),width=1200, height=800, background=(0.5,0.5,0))
floor = box(length=30, height=0.01, width=4, color=color.blue) # floor

#ruler
ruler1 = ruler.ruler(vector(-15, 0, 1), vector(1,0,0), unit = 2.0, length = 30.0, thickness = 0.2)
ruler2 = ruler.ruler(vector(-15, 0, 1), vector(0,1,0), unit = 1.0, length = 10.0, thickness = 0.2)

#common factor for both ball
v_initial = 10.0
theta_initial = 45.0*math.pi/180 #rad
dt = 0.001
drag_coef = 0.3
drag_power = 1.0

#normal ball
ball = sphere(radius = size, color=color.red, make_trail=True) # ball
ball.v = v_initial * vector(cos(theta_initial), sin(theta_initial), 0)
ball.pos = vector( -15.0, 0.0, 0.0) # ball initial position

#ball_1: ball with air drag
ball_1 = sphere(radius = size, color=color.green, make_trail=True)
ball_1.pos = vector( -15.0, 0.0, 0.0) # ball initial position
ball_1.v = v_initial * vector(cos(theta_initial), sin(theta_initial), 0)


#normal ball
while ball.pos.x < 15.0: # simulate until x=15.0m
    # ruler1 # ruler2
    rate(1000)
    ball.pos += ball.v*dt
    ball.v.y += - g*dt
    if ball.y <= size and ball.v.y < 0:
        ball.v.y = - ball.v.y

#ball with air drag
while ball_1.pos.x < 15.0: # simulate until x=15.0m
    # ruler1 # ruler2
    rate(1000)
    ball_1.pos += ball_1.v*dt
    ball_1.v.x += (-drag_coef * ball_1.v.x ** drag_power)*dt/mass
    ball_1.v.y += - g*dt
    if ball_1.y <= size and ball_1.v.y < 0:
        ball_1.v.y = - ball_1.v.y
    ball_1.v.y += (-drag_coef * ball_1.v.y ** drag_power)*dt/mass # this must be under if statment, otherwise the direction of air drag force will be wrong.

#testing the biggest distance
distance = {} #initial an empty dictionary
for th in range(91): #function range(n) gives integer between 0 to n-1
    theta = (th)*math.pi/180
    test_pos = vector( 0.0, 0.000001, 0.0)
    v = 100.0 * vector(cos(theta), sin(theta), 0) #v_initial should be fast enough to avoid bug
    while True:
        # ruler1 # ruler2
        test_pos += v*dt
        v.x += (-drag_coef * v.x ** drag_power)*dt/mass
        v.y += - g*dt
        v.y += (-drag_coef * v.y ** drag_power)*dt/mass
        if test_pos.y <= 0:
            print theta
            distance[th] = test_pos.x
            #th is the key while test_pos.x is current x_distance when hitting the ground the first time
            break #break the while loop

print distance
distance_max = max(distance, key=distance.get)
print distance_max
print 'end'
