from visual import *
import ruler

t=0
size = 0.025 
scene = display(title='Light curve', center = (0.52,0.58,0),width=400, height=450)

#ruler
ruler1 = ruler.ruler(vector(0, 0, 0), vector(1,0,0), unit = 0.1, length = 1.0, thickness = 0.01)
ruler2 = ruler.ruler(vector(0, 0, 0), vector(0,1,0), unit = 0.1, length = 1.1, thickness = 0.01)

#Setup for ball
dt = 0.001

#normal ball
ball = sphere(radius = size, color=color.white, make_trail=True) # ball 
ball.pos = vector( 0.0, 1.0, 0.0) # ball initial position
ball.orbit = curve(color=color.cyan, radius = 0.01)

#normal ball
while True:
    rate(100)
    tt=t%1
    ball.pos.x=(tt)
    ball.pos.y=1 if ((tt-0.5)**2>0.01) else 0.9
    if (t<=1):
      ball.orbit.append(pos=ball.pos)
#    print t, tt
    t += dt

print 'end'
