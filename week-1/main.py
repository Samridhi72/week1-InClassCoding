# program to find area of circle using math library
import math
radius=float(input("Enter the radius of a circle :---> "))
sq=pow(radius,2)
area= math.pi * sq
print(f'Area of circle with radius {radius} is {area:.3f}')
print('---------------------------------------------------')
# program to compute current date and time using datetime module
import datetime
print("Today's Information")
Date=datetime.date.today()
print(f' Curent date is :---> {Date}')
time=datetime.datetime.now()
time=time.strftime("%H:%M:%S")
print(f'Current Time is :---> {time}')

