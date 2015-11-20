from visual import *
'''
In this module, a ruler object is constructed.
It includes position(pos), direction(axis), unit(unit), length(length), and thickness(thickness).
Please see __init__() to see its original setting.
When ruler object is called, a ruler is built with one end at pos, stretching in the axis direction.
MFS 2015/6/21
'''

class ruler:
    def __init__(self, pos=vector(0,0,0), axis=vector(0,1,0), unit=1.0, length=10.0, thickness=0.1):
        self.__dict__['pos'] = vector(pos)
        self.__dict__['axis'] = vector(axis)
        self.__dict__['unit'] = float(unit)
        self.__dict__['length'] = float(length)
        self.__dict__['thickness'] = float(thickness)
        self.drawruler()
        return

    def drawruler(self):
        pos = self.pos
        axis = self.axis/abs(self.axis)
        unit = self.unit 
        length = self.length 
        thickness = self.thickness

        colormap = [color.yellow, color.green]
        x, y, z = axis.x, axis.y, axis.z
        
        self.__dict__['vruler'] = [box(length=unit, height = thickness, width = thickness,
                      pos = (pos.x + x*(0.5+i)*unit  , pos.y + y*(0.5+i)*unit, pos.z + z*(0.5+i)*unit),
                      axis = (x,y,z),
                      color=colormap[i%2]) for i in range(int(length/unit))]
        if int(length/unit) != length / unit:
            num = int(length/unit)
            rem = length - num*unit
            base = num*unit + rem/2
            self.vruler.append(box(length=rem, height = thickness, width = thickness,
                      pos = (pos.x + x*base  , pos.y + y*base, pos.z + z*base),
                      axis = (x,y,z),
                      color=colormap[num%2]))
            
        L = length / unit + 0.5
        self.vruler.append(label(pos=(pos.x + x*L*unit  , pos.y + y*L*unit, pos.z + z*L*unit), box =False, text=str(length)))
        return

    def __setattr__(self, name, value):
        for b in self.vruler:
            b.visible = False
            del b
        if name in ['pos', 'axis']:
            self.__dict__[name]=vector(value)
        else:
            self.__dict__[name]=float(value)
        self.drawruler()
        return

