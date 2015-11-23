#!/usr/bin/env python

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


### begin for test ###

ll=get_func_for_luminosity(r_planet=10,r_star=200,scaling_factor=1)







