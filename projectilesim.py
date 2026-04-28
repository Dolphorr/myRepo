# Imports
import math

v = float(input("Velocity: ")) # initial velocity input
angle_deg = float(input("Angle (degrees): ")) # initial angle for projectile launch
gravity = 9.8  # acceleration due to gravity (m/s^2)

angle_rad = math.radians(angle_deg) # angle conversion of degrees to radians

vy = v * math.sin(angle_rad) # vertical velocity (upward)
vx = v * math.cos(angle_rad) # horizontal velocity (sideward)

print("\nTrajectory:")

t = 0.0
dt = 0.1

while True:
    y = (vy * t) - (0.5 * gravity * t**2) # vertical position = upward motion − gravity effect over time
    x = vx * t # horizontal distance = horizontal speed × time
    
    if y <= 0 and t > 0:
        print(f"t={round(t, 1)}s | x={round(x, 2)}, y=0.0 (hit ground)")
        break
    
    print(f"t={round(t, 1)}s | x={round(x, 2)}, y={round(y, 2)}")
    t += dt
