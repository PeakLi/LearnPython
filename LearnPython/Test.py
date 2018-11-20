#!/bin/usr/env python3
# coding=gbk
def max_min(x,y,z):
	if(x>y):
		max=x
	else:
		max=y
	if(max<z):
		max=z

	if(x>y):
		min=y
	else:
		min=x
	if(min>z):
		min=z
	return max,min
		

print(max_min(5,-34,-2))

import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
r = move(100, 100, 60, math.pi / 6)
print(x,y)
print(r)

def quadratic(a,b,c):
	x = pow(b,2)-4*a*c
	print("x===:",pow(b,2),4*a*c)
	if(x==0):
		return -(b/2*a)
	elif(x<0):
		return None
	else:
		return ((-math.sqrt(x)-b)/(2*a)),((math.sqrt(x)-b)/(2*a))

print(quadratic(2, 3, 1))