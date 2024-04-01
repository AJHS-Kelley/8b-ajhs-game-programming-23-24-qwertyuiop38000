# Input the Integers
# .split() the three integers into seperate variables
# assign correct values from least to greatest
# A < B < C

integers = input()
a, b, c = integers.split()
a = int(a)
b = int(b)
c = int(c)

#print(f"a: {a} b: {b} c: {c}")
if a >= b:
    a, b = b, a
if b >= c:
    b, c = c, b
if a >= b:
    a, b = b, a
#print(f"a: {a} b: {b} c: {c}")

order = input().upper()
myString = ""

for i in range(len(order)):
    if order[i] == "A":
        myString += str(a) + " "
    elif order[i] == "B":
        myString += str(b) + " "
    else:
        if i == range(len(order)):
            myString += str(c)
        else:
            myString += str(c) + " "
    i += 1
print(myString)
    