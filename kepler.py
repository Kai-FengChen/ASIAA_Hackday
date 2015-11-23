from visual.controls import *
import ruler
from pylab import *
import scipy.interpolate
from visual import *
from visual.controls import *
from visual.graph import *

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
giant.material = materials.emissive
giant.pos = vector(-1e11,0,0)
giant.radius = 4e10
giant.color = color.yellow
giant.mass = 4e30
dwarf = sphere()
dwarf.material = materials.earth
dwarf.pos = vector(1.5e11,0,0)
dwarf.radius = 1e10
dwarf.color = color.white
dwarf.mass = 1e29
dwarf.p = vector(0, 0, 2.6E4) * dwarf.mass
giant.p= -dwarf.p
initial = dwarf.pos.x
L = {}
'''def change(): # Called by controls when button clicked
      if b.text == 'Click me':
            b.text = 'Try again'
      else:
            b.text = 'Click me'
'''
'''c = controls() # Create controls window
# Create a button in the controls window:
b = slider( pos = (-50,0),
             action=lambda: change() )'''
t = 0
for a in [giant, dwarf]:
      a.orbit = curve(color=a.color, radius = 5e8)
      dt = 86400

size = 0.025
R = 5
scene = display(title='Light curve', center = (0,0,0),width=400, height=450)
'''
camera = vector(0,0,R) # for generality; need not be at origin
# Place center of scene at a distance R from the camera:
# Point the camera:
scene.forward = scene.center-camera
# scene.fov is "field of view" in radians. R times the tangent
#  of half the field of view is half of the width of the scene:
scene.range = R*tan(scene.fov/2)
scene.userspin = False
down = False
lastpos = None
'''
#ruler
ruler1 = ruler.ruler(vector(0, 0, 0), vector(2,0,0), unit = 0.1, length = 1.0, thickness = 0.01)
ruler2 = ruler.ruler(vector(0, 0, 0), vector(0,2,0), unit = 0.1, length = 1.1, thickness = 0.01)


#normal ball
ball = sphere(radius = size, color=color.white, make_trail=True) # ball 
ball.pos = vector( 0.0, 1.0, 0.0)
ball.orbit = curve(color=color.cyan, radius = 0.01)

while 1:
    rate(100)
    '''
    if scene.mouse.events:
      m = scene.mouse.getevent()
      if m.press == 'left':
        down = True
      elif m.release == 'left':
        down = False
      if down: # and scene.mouse.pos != lastpos:
        lastpos = scene.mouse.pos
        lastpos.y = 0 # force mouse position to have y=0
        # (lastpos-camera) is a vector parallel to screen.
        # (lastpos-camera) cross norm(forward) is a vector in the +y direction,
        #   and this y component of the cross product is proportional to
        #   how far to the right the mouse is (if mouse is to left, this y
        #   component is negative)
        rotation = cross((lastpos-camera),norm(scene.forward))
        # If the mouse is to the right, y component is positive, and we need to
        #   turn the view toward the right, which means rotating the forward
        #   vector toward the right, about the +y axis, which requires a
        #   negative angle (vice versa if mouse is to the left, in which case
        #   the cross product is in the -y direction. The factor of 1/100 was
        #   chosen experimentally as giving an appropriate sensitivity to how
        #   far to the right (or left) the mouse is. Bigger mouse displacement
        #   makes the rotation faster.
        scene.forward = scene.forward.rotate(angle=-rotation.y/100, axis=(0,1,0))
        # Move the center of the scene to be a distance R from the camera,
        #   in the direction of forward.
        scene.center = camera+R*norm(scene.forward)'''
    dist = dwarf.pos - giant.pos
    distance = int(abs(dwarf.pos.x - giant.pos.x))
    if distance < 2*giant.radius-5e9 and (dwarf.pos.z- giant.pos.z > 0):
      print distance, ll(distance)
      ball.pos.y =  ll(distance)
    else:
      ball.pos.y =  1

    force = 6.7e-11 * giant.mass * dwarf.mass / mag(dist)**2 * (dist/mag(dist))
    giant.p = giant.p + force*dt
    dwarf.p = dwarf.p - force*dt
    for a in [giant, dwarf]:
        a.pos = a.pos + a.p/a.mass * dt
        a.orbit.append(pos=a.pos)
    ball.pos.x=((t/30067200.)%1)
    if (t<30067200):
      ball.orbit.append(pos=ball.pos)
    t += dt
