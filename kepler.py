from visual import *
from visual.controls import *
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
dwarf.p = vector(0, 0, 2.6E4) * dwarf.mass
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
b = slider( pos = (-50,0),
             action=lambda: change() )

for a in [giant, dwarf]:
      a.orbit = curve(color=a.color, radius = 2e9)
      dt = 86400
while 1:
    rate(100)
    dist = dwarf.pos - giant.pos
    print dist
    force = 6.7e-11 * giant.mass * dwarf.mass / mag(dist)**2 * (dist/mag(dist))
    giant.p = giant.p + force*dt
    dwarf.p = dwarf.p - force*dt
    for a in [giant, dwarf]:
        a.pos = a.pos + a.p/a.mass * dt
        a.orbit.append(pos=a.pos)
