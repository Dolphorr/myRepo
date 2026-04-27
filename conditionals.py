<<<<<<< HEAD
# if = Do some code only IF some condition is True
#      Else do something else

# Eligibility to sign-up
age = int(input("Enter your age: "))

if age < 0:
    print("You haven't been born yet?")
elif age >= 100:
    print("You are too old to sign up, sorry!")
elif age >= 18:
    print("You are now signed up!")
else:
    print("You must be 18+ to sign up.")

# Ordering Food (Exercise 1)
response = input("Would you like food? (Y/N): ")

if response == "Y":
    print("Have some food!")
else:
    print("No food for you!")

# Name collection (Exercise 2)
name = input("Enter your name: ")

if name == "":
    print("You did not type in your name!")
else:
    print(f"Hello {name}")

# Use of Bools in conditions
for_sale = True

if for_sale: # if the var (for_sale)'s value is True, do something, else do another thing.
    print("This item is for sale!")
else:
    print("This item is not for sale!")

online = False

if online: # if the var (online) is True, do something, else do another thing.
    print("The user is online.")
else:
    print("The user is offline.")
=======
# if = Do some code only IF some condition is True
#      Else do something else

# Eligibility to sign-up
age = int(input("Enter your age: "))

if age < 0:
    print("You haven't been born yet?")
elif age >= 100:
    print("You are too old to sign up, sorry!")
elif age >= 18:
    print("You are now signed up!")
else:
    print("You must be 18+ to sign up.")

# Ordering Food (Exercise 1)
response = input("Would you like food? (Y/N): ")

if response == "Y":
    print("Have some food!")
else:
    print("No food for you!")

# Name collection (Exercise 2)
name = input("Enter your name: ")

if name == "":
    print("You did not type in your name!")
else:
    print(f"Hello {name}")

# Use of Bools in conditions
for_sale = True

if for_sale: # if the var (for_sale)'s value is True, do something, else do another thing.
    print("This item is for sale!")
else:
    print("This item is not for sale!")

online = False

if online: # if the var (online) is True, do something, else do another thing.
    print("The user is online.")
else:
    print("The user is offline.")
>>>>>>> 782069ddcaa8d91aee6441175fdaea429cc10405
