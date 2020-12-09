# Finding Factors
def findFactors(num):
    factorList = []
    for i in range(1, num):
        if num % i == 0:
            factorList.append(i)
    return factorList

# Sum of Factors
def factorSum(factorList):
    sum = 0
    for i in factorList:
        sum += i
    return sum

# Comparing Sum to Number
def perfectNum(num, sum):
    if num == sum:
        print(num)

# Finding Perfect Numbers from 2 to 1000

for num in range(2, 10001):
    factorList = findFactors(num)
    sum = factorSum(factorList)
    perfectNum(num, sum)
print ("List Complete")