# data types and operators, william castengera, v0.6

# varible rules
# cannot start with a number
# varible name should describe the data that it stores
# snake_case varibles use _ to seperate words all lowercase
# camalCase varibles do not use spaces, 1st word lowercase, rest of words uppercase

# string literal examples
playerName = "Jack"
emptyString = ""
spaceString = " "
questName = "AHHH"

# Integer data types
health = 100
extraLives = 5
jackMoney = -10000

# floating point data type
pi = 3.1415926535
lapTime = 3.5
velocity = -2.0
friction = 5.5

# boolean data types
isFireType = False
weaponEquipped = True
pvpEnabled = False
running = True

# arithmetic operators
# pemdas applies
print(9 + 3) # addition
print(9 - 3) # subtraction
print(9 * 3) # multiplication
print(9 / 3) # division
print(9 ** 3) # exponents
print(9 % 3) # modulous

# comparison operators
# evaluate the expression then return true or false
print(5 > 3) # greater than
print(7 >= 4) # greater than or equal to
print(-23 < 25) # less than
print(0 <= 3748234892389479238749839749328472937938478239) # less than or equal to
print(6 == 1) # equal to
print(-99 != 489569345349548) # not equal to

# assignment operators
myVariable = "myValue" # assign variable on the left to the value on the right. throws out any current value
myOtherVariable = (10 + 5)

myVariableAgain = 1
myVariableAgain = 5
print(myVariableAgain)

# addition assignment -- add the value on the right keeping any current value
myWallet = 0
myWallet += 1
myWallet += 5
print(myWallet)

# same effect
x = 0
x += 1
x = x + 1

# logical operators
print(3 > 5 and 4 < 3) # and requires all expressions to be true
print(3 > 2 and 4 < 3) 
print(3 > 2 and 4 != 3)
print(3 > 2 and 4 != 3 and favColor == "blue" and temp == -5)
# when writing expressions, put the value most likely to be false first