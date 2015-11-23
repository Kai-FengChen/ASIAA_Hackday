from visual import *
import ruler
from pylab import *
import scipy.interpolate

def get_func_for_luminosity(r_planet,r_star,scaling_factor=1e8):

  r_planet = int(r_planet/scaling_factor)
  r_star   = int(r_star  /scaling_factor)


  full_area=zeros((r_star,r_star))

  for x in range(r_star):
    for y in range(r_star):
      if x**2 + y**2 < r_star**2:
        full_area[x,y]=1

  r_planet_square  = r_planet**2
  sum_full_area_q  = sum(full_area)

  d_list=range(r_planet,r_star*2)
  l_list=[]

  for x_planet in d_list:

    area=copy(full_area)

    #print x_planet

    x1=max(0       ,x_planet-r_planet)
    x2=min(r_star-1,x_planet+r_planet)

    for x in range(x1,x2):
      for y in range(0,r_planet):
        if (x-x_planet)**2+y**2 < r_planet_square:
          area[x,y]=0.

    luminosity=(sum(area)*2+sum_full_area_q*2)/(sum_full_area_q*4)
    l_list.append(luminosity)

  d_list.insert(0,0)
  l_list.insert(0,l_list[0])

  d_list=array(d_list)*scaling_factor

  return scipy.interpolate.interp1d(d_list,l_list)

ll=get_func_for_luminosity(r_planet=10,r_star=200,scaling_factor=1)
### begin for test ###



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
    ball.pos.y = ll(t%2000)
    if (t<=1):
      ball.orbit.append(pos=ball.pos)
#    print t, tt
    t += dt

print 'end'
