import math

# Arithmetic Operators

friends = 5

friends += 1 # the same as friends = friends + 1

friends -= 2 # the same as friends = friends - 2

friends *= 3 # the same as friends = friends * 3

friends /= 2 # the same as friends = friends / 2

# Friends logic

raw_friends = friends
rounded_friends = round(friends)

remainder = int(rounded_friends) % 2

portion_of_friend = raw_friends - rounded_friends

if (portion_of_friend != 0):
    friend_portion = True
else:
    friend_portion = False

if friend_portion:
    print(f"You have {rounded_friends} friends,")
    print(f"and {round(portion_of_friend, 2)} portions of a friend which doesn't need a pair.\n")
else:
    print(f"You have {rounded_friends} friends.\n")

if remainder != 0:
    print(f"{remainder} friend doesn't have a pair.\n")

# Built-in Functions

x = 3.14
y = -4
z = 5

max_value = max(x, y, z)
min_value = min(x, y, z)
xresult = round(x)
yresult = abs(y)
zresult = pow(z, 3)

print(f"Maximum value: {max_value}")
print(f"Minimum value: {min_value}")
print(xresult)
print(yresult)
print(zresult)

# Math module usage

print(math.pi)
print(math.e)

a = 9
b = 7.3
c = 6.7

sqrt_result = math.sqrt(a)
ceil_result = math.ceil(b)
floor_result = math.floor(c)

print(sqrt_result)
print(ceil_result)
print(floor_result)

# Circumference of a Circle (Exercise 1)

radius1 = float(input("Enter the radius of a circle: "))
circumference = 2 * math.pi * radius1

print(f"The circumference is: {round(circumference, 2)}cm")

# Area of a Circle (Exercise 2)

radius2 = float(input("Enter the radius of a circle: "))
area = math.pi * pow(radius2, 2)

print(f"The area is {round(area, 2)}cm^2")

# Hypotenuse of a Right Triangle (Exercise 3)

side_a = float(input("Enter side A: "))
side_b = float(input("Enter side B: "))
side_c = math.sqrt(pow(side_a, 2) + pow(side_b, 2))

print(f"The Hypotenuse is: {round(side_c, 2)}")
