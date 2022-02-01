import math
from math import pi,tan,cos



g=(9.81)
vo=(44)
theta=(80*(pi/180))
x=(0.5)
yo=(1)

projectile=((yo+x*tan(theta)-((g*(x*x))/(2*(vo*cos(theta))*(vo*cos(theta))))))

print(projectile)

