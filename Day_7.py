# ++++++++++++  ALGORITHME  ++++++++++++++++++
import math


# ***********  SEARCHING ALGORITHME ************

# 1 ---> LINEAR SEARCH
def linearSearch(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return f'index of searching value is {i}'
    return -1


# print(linearSearch([20, 40, 15, 19, 10, 150], 10))


# 1 ---> BINARY SEARCH  (Note: apply when array is sorted)
def binarySearch(array, value):
    start = 0
    end = len(array) - 1
    middle = math.floor((start + end) / 2)
    print(start, middle, end)
    while not (array[middle] == value):
        if value < array[middle]:
            end = middle - 1
        else:
            start = middle + 1
        middle = math.floor((start + end) / 2)
        print(start, middle, end)

    return f'Index of searching number is {middle}'


# my_array = [8, 9, 12, 15, 17, 19, 20, 25, 34]
# print(binarySearch(my_array, 15))


# ***********  SORTING ALGORITHME ************

# 1 ---> BUBBLE SORT
def bubbleSort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return f'Array is sorted {array}'


# my_array = [8, 34, 12, 5, 17, 14, 20, 25]
# print(bubbleSort(my_array))

# 2 ---> SELECTION SORT
def selectionSort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

    return f'Array is sorted {array}'


my_array = [8, 34, 12, 5, 17, 14, 20, 25]
print(selectionSort(my_array))
