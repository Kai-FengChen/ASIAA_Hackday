#!/usr/bin/env python

from pylab import *
import scipy.interpolate

r_planet=100  # unit is in pix
r_star  =400

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

  print x_planet

  x1=max(0       ,x_planet-r_planet)
  x2=min(r_star-1,x_planet+r_planet)

  for x in range(x1,x2):
    for y in range(0,r_planet):
      if (x-x_planet)**2+y**2 < r_planet_square:
        area[x,y]=0.

  luminosity=(sum(area)*2+sum_full_area_q*2)/(sum_full_area_q*4)
  l_list.append(luminosity)
  #print luminosity

  #area_star=r_star*r_star*pi/4
  #area_planet=r_planet**2*pi/2
  #print area_star-area_planet

d_list.insert(0,0)
l_list.insert(0,l_list[0])


figure(1)
clf()
plot(d_list,l_list)
show()

ll=scipy.interpolate.interp1d(d_list,l_list)




