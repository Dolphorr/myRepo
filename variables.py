# Variable = A container for a value (string, integer, float, boolean).
#            A variable behaves as if it was the value it contains.

# Strings
name = "Dolphor"
food = "pizza"
email = "dolphor.business@gmail.com"

print(f"Hello {name}.")
print(f"You like {food}.")
print(f"Your email is: {email}")

# Integers
age = 13
quantity = 3
num_of_students = 30

print(f"You are {age} years old.")
print(f"You are buying {quantity} items.")
print(f"Your class has {num_of_students} students.")

# Floats
price = 10.99
gpa = 3.5
distance = 5.5

print(f"The price is ${price}")
print(f"Your gpa is: {gpa}/4")
print(f"You ran {distance}km")

# Booleans
is_student = True
for_sale = True
is_online = True

if is_student:
    print("You are a student!")
else:
    print("You are not a student!")

if for_sale:
    print("That item is for sale.")
else:
    print("That item is not available.")

if is_online:
    print("You are online.")
else:
    print("You are offline.")
