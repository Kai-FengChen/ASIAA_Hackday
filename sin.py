from pylab import *
from visual import *

ball = sphere(radius=0.5, color=color.white)
ball.pos= vector(0,0)
ball.orbit = curve(color=ball.color, radius = 0.01)

pi2 = 2*pi

sequence = 1

for theta in arange(0,pi2*sequence,pi2/100):
    rate(100)
    ball.pos = vector(mod(theta,pi2),sin(theta))
    ball.orbit.append(pos=ball.pos)
