# Data Types and Operatoers, Tajuan Terry, v0.3

# Variable Rules
# CANNOT START WITH A NUMBER!!!!!!!!!
# CANNOT USE BUILT- IN KEYWORDS AS VARIABLES.
# VARIABLE NAME SHOULD DESCRIBE THE DATA BEING STORES.
# snake_case variable use _ to separate words, all lower case.
# camelCase Variables do not use spaces, 1st word lower, rest upper

# String Literal Examples
playerName = "Taiyo"
EmptyString = ""
spaceString = "" 
monsterName = "Chaos"

# Integer Data Types
Health = 100
extraLIves = 5
Temperature = -17
Speed = 50

# Floating point Data Types
pi = 3.1415768
lapTaime = 3.5
velocity = 2.0

# boolean Data Types
isFIreType = False
weaponEquipped = True
pvpEnable = False
# Arithmetic Operateors
# PEMDAS APPLIES JUST LIKE IN MATH CLASS!
print(3 + -1) # Addition
print(0 - 25) # Subutarction
print(2 * -2) # Multiplication
print(1 / -2) # Division
print(3 ** 2) # Exponents
print(18 % 3) # Modulus -- Divides, then returns reminder, most commonly used to determine even/odd

# Comparison Operators 
# Evaluate the expression then return  True or False 
print(5 > 3) #Greater Than 
print(7 >= -1) # greater Than or Equal To
print(-1 < -2) # Less Than
print(0 <= 0) # Less Than or Equal To
print(5 == 3) # IS Equal To
print(-99 != 99) # Not Equal To

# Assignment Operators 
myVariable = "myValue" # Assign variable on left the value on the right, throw out any current value 
myOtherVariable = (10 + 5)

#Addition Assignment -- Add the value on the right, keeping any current value 
myWallet = 0
myWallet +=1
myWallet +=5
print(myWallet)

# Same Effect
x = 0
x += 1
x = x + 1

# Logical Operators
print(3 > 5 and 4 < 3) # AND Requires ALL expressions to be True.
print(3 > 2 and 4 < 3)
print(3 > 2 and 4 != 3)
print(3 > 2 and 4 != 3 and favColor == "Blue" and temp == -5)
# When writing and expressions, put the value most likely to be False firsts!
# Logical OR -- Requires ONE expression to be True.
print(5 > 2 or 2 < -2)
print(3 != 3 or 5 = 5)

# AND OR Combined 
print(3 > 2 and 4 < 3 or 5 != 7)
print(True and False or True)

# NOT Logical operator
print(not (3 > 2))
print(not (not (not (5 != 3))))
