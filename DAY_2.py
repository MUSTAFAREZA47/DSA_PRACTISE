## TWO DIMENSIONAL ARRAY
import random

##     Day 1 - [11, 15, 10, 6]
##     Day 2 - [10, 14, 11, 5]
##     Day 3 - [12, 17, 12, 8]
##     Day 4 - [15, 18, 14, 9]



twoDArray = [[11, 15, 10, 6], [105, 14, 110, 5], [12, 17, 150, 8], [180, 18, 14, 9] ]
##print(twoDArray[3])

def accessElement(array, rowIndex, colIndex):
    if rowIndex >= len(array) and colIndex >= len(array[0]):
        print('Incorrect Index')
    else:
        print(array[rowIndex][colIndex])

##accessElement(twoDArray, 2, 2)

def traverseElement(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])

##traverseElement(twoDArray)

def searchElement(array, number):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == number:
                print(f'Number {number} has index {i, j}')


##searchElement(twoDArray, 8)

##print(twoDArray.delete(twoDArray[0]))

##  LIST

my_list = ["apple", "banana", "apple"]

##for i in range(len(my_list)):
##    print(f'{my_list[i]} at index of {i}')

##  Using Delete function

##del my_list[2]

listOne = [11, 15, 10, 6, "a"]


stringList = 'Python'
new_list = [item for item in stringList]
# print(stringList)
# print(new_list)

listOne.pop()
listOne.pop()
print(listOne)


#  AVERAGE TEMPERATURE CALCULATOR

numDays = int(input("How many day's temperature?"))
total = 0
temp = []
for i in range(numDays):
    nextDay = int(input("Day" + str(i) + "'s high temp :"))
    total += nextDay

avg = round(total/numDays, 2)
print("\nAverage =" + str(avg))
























