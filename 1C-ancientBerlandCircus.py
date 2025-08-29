# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import math

def alif():
    x1, y1 = map(float, input().split())
    x2, y2 = map(float, input().split())
    x3, y3 = map(float, input().split())
    
    a = math.sqrt((x2 - x3)**2 + (y2 - y3)**2)
    b = math.sqrt((x1 - x3)**2 + (y1 - y3)**2)
    c = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    
    K = abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)) / 2
    R = (a * b * c) / (4 * K)

    d = 2 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    cx = ((x1**2 + y1**2) * (y2 - y3) + (x2**2 + y2**2) * (y3 - y1) + (x3**2 + y3**2) * (y1 - y2)) / d
    cy = ((x1**2 + y1**2) * (x3 - x2) + (x2**2 + y2**2) * (x1 - x3) + (x3**2 + y3**2) * (x2 - x1)) / d
    v1x, v1y = x1 - cx, y1 - cy
    v2x, v2y = x2 - cx, y2 - cy
    v3x, v3y = x3 - cx, y3 - cy
    
    def angle_between(vx1, vy1, vx2, vy2):
        dot = vx1 * vx2 + vy1 * vy2
        len1 = math.sqrt(vx1**2 + vy1**2)
        len2 = math.sqrt(vx2**2 + vy2**2)
        cos_theta = min(1, max(-1, dot / (len1 * len2)))
        return math.acos(cos_theta)
    
    theta1 = angle_between(v1x, v1y, v2x, v2y)
    theta2 = angle_between(v2x, v2y, v3x, v3y)
    theta3 = angle_between(v3x, v3y, v1x, v1y)
    min_area = float('inf')

    for n in range(3, 101):
        theta = 2 * math.pi / n
        k1 = round(theta1 / theta)
        k2 = round(theta2 / theta)
        k3 = round(theta3 / theta)
        tolerance = 1e-6
        
        if (abs(theta1 - k1 * theta) < tolerance and
            abs(theta2 - k2 * theta) < tolerance and
            abs(theta3 - k3 * theta) < tolerance):
            area = 0.5 * n * R**2 * math.sin(2 * math.pi / n)
            min_area = min(min_area, area)
    
    print(f"{min_area:.8f}")

if __name__ == "__main__":
    alif()