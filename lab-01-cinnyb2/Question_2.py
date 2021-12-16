"""
Question 2 : How many can of paint does it take to paint a room
"""
import math
# 4L can of paint can cover 40m^2
coverage = 40

length_metres = float(input("What is the length of the room in metres? "))

width_metres = float(input("What is the width of the room in metres? "))

height_metres = float(input("What is the height of the room in metres? "))

coats = int(input("How many coats of paint do you want? "))

# Calculates the total surface area of a rectangular room without the floors
surface_area = ((2 * (width_metres * height_metres)) + (2 * (length_metres * height_metres)) +
                (length_metres * width_metres))

coverage_needed = surface_area * coats

cans_of_paint_required = coverage_needed / coverage
# formula for rounding the paint cans
# rounded_cans = int(cans_of_paint_required - 0.5) + 1


print("You need to buy %s can/s of paint, of which you will use %s." % (math.ceil(cans_of_paint_required),
                                                                        cans_of_paint_required))
