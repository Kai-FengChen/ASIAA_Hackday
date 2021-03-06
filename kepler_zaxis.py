from visual.controls import *
import ruler
from pylab import *
import scipy.interpolate
from visual import *

def get_func_for_luminosity(r_planet,r_star,scaling_factor):

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

ll=get_func_for_luminosity(r_planet=1e10,r_star=4e10,scaling_factor=1e8)

giant = sphere()
giant.pos = vector(-1e11,0,0)
giant.radius = 4e10
giant.color = color.yellow
giant.mass = 4e30
dwarf = sphere()
dwarf.pos = vector(1.5e11,0,0)
dwarf.radius = 1e10
dwarf.color = color.green
dwarf.mass = 1e29
dwarf.p = vector(0, 2.6E4,0) * dwarf.mass
giant.p= -dwarf.p
L = {}
'''def change(): # Called by controls when button clicked
      if b.text == 'Click me':
            b.text = 'Try again'
      else:
            b.text = 'Click me'
'''
#c = controls() # Create controls window
# Create a button in the controls window:
#b = slider( pos = (-50,0),
#             action=lambda: change() )

for a in [giant, dwarf]:
      a.orbit = curve(color=a.color, radius = 2e9)
      dt = 86400
while 1:
    rate(100)
    dist = dwarf.pos - giant.pos
    #print ll(mag(dist)/1e8-1194)

    force = 6.7e-11 * giant.mass * dwarf.mass / mag(dist)**2 * (dist/mag(dist))
    giant.p = giant.p + force*dt
    dwarf.p = dwarf.p - force*dt
    for a in [giant, dwarf]:
        a.pos = a.pos + a.p/a.mass * dt
        a.orbit.append(pos=a.pos)
