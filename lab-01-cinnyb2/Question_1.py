"""
Question 1
"""
import math
# creating var PI with value of 3.14159
# PI = 3.14159

# prompts the user to enter a radius value for a sphere and assigns that float as the var radius
radius = float(input('Enter a radius value for a sphere: '))

# calculates the surface area of a sphere with given radius input
surface_area = (4 * math.pi * radius ** 2)

# prints the surface area of the sphere
print('surface area of the sphere: ', surface_area)

# calculates the volume of a sphere and stores it in var volume
volume = (4/3 * math.pi * radius ** 3)

# prints the volume of the sphere
print('the volume of the sphere: ', volume)

# var double radius will store 2X the inputted radius
double_radius = radius * 2

double_surface_area = (4 * math.pi * double_radius ** 2)

double_volume = (4 / 3 * math.pi * double_radius ** 3)

# added an optional fun print statement to show the calculation for double the radius what it does to volume and sa
print('Wow lets double the fun, '
      'if we double your inputted radius of %s to %s, '
      'we will get a surface area of %s,'
      ' and volume of %s.' % (radius, double_radius, double_surface_area, double_volume))

surface_area_increase = (double_surface_area / surface_area)

volume_increase = (double_volume / volume)

print('when you double the radius the surface area increase by %s times, '
      '\n and the volume increase by %s times. So volume is always double the surface area of a sphere '
      'when the radius is doubled!' % (surface_area_increase, volume_increase))





