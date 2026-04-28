# Typecasting = The process of converting a value of one data type to another.
#               (string, integer, float, boolean)
#               Explicit vs Implicit


# Explicit Typecasting:


# Variables
name = "Dolphor"
age = 13
gpa = 3.5
is_student = True

# Printing the type of any variable
print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

# Typecasting existing variables
name = bool(name)
print(name)
print(type(name))

age = float(age)
print(age)
print(type(age))

age = bool(age)
print(age)
print(type(age))

gpa = int(gpa)
print(gpa)
print(type(gpa))

is_student = str(is_student)
print(is_student)
print(type(is_student))


# Implicit Typecasting:


x = 2
y = 2.0
x = x/y

print(x)
