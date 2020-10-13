import math
number1 = int(input ("Enter a value: "))
number2 = int(input ("Enter another value: "))
numbers = [5, 2, 8, 1, 3, 7]

print (numbers)
print (numbers[2]) # Prints the third number in the list (computers start counting from 0)

for i in numbers:
    print (i, end = " ")
print ()

answer = number1 * number2
print (answer)

answer = number1 / number2
print (answer)
print (math.floor(answer)) # Cuts off to the next lowest integer, same as trunc for positive
print (math.ceil(answer)) # Goes up to the next highest interger, same as trunc for negative
print (math.trunc(answer)) # Cutts off to the next lowest integer, same a floor for positive same as ciel for negative


answer = number1 // number2
print (answer) # Removes the float when you use // instead of /

answer = number1 % number2

print (answer) # Shows the remainder

if number2 > number1:
    hold = number1
    number1 = number2
    number2 = hold

if number1 % number2 == 0:
    print (str(number1) + " is a multiple of " + str(number2))
else:
    str(number1) + " is not a multiple of " + str(number2)

counter = 0

while counter < 10: # This loop will go through exactly 10 times
    print (counter)
    counter += 2 # Same as saying counter = counter + 1


for counter in range (10, 0, -2) # First integer is what to start at, second is what to end at, third is how much to go by
    print (counter)
