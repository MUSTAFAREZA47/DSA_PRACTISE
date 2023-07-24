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


# my_array = [8, 34, 12, 5, 17, 14, 20, 25]
# print(selectionSort(my_array))

# 3 ---> INSERTION SORT
def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array


# my_array = [8, 34, 12, 5, 17, 14, 20, 25]
# print(insertionSort(my_array))

# 4 ---> BUCKET SORT
def bucketSort(array):
    numberOfBuckets = round(math.sqrt(len(array)))
    maxValue = max(array)
    temp_array = []

    for i in range(numberOfBuckets):
        temp_array.append([])

    for j in array:
        indexOfBucket = math.ceil(j * numberOfBuckets / maxValue)
        temp_array[indexOfBucket - 1].append(j)

    for i in range(numberOfBuckets):
        temp_array[i] = insertionSort(temp_array[i])

    k = 0
    for i in range(numberOfBuckets):
        for j in range(len(temp_array[i])):
            array[k] = temp_array[i][j]
            k += 1
    return array


# my_array = [8, 34, 12, 5, 17, 14, 20, 25]
# print(bucketSort(my_array))

# 5 ---> MERGER SORT
def merge(array, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = array[l + i]

    for j in range(0, n2):
        R[j] = array[m + 1 + j]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1

    while j < n2:
        array[k] = R[j]
        j += 1
        k += 1


def mergeSort(array, l, r):
    if l < r:
        m = (l + (r - 1)) // 2
        mergeSort(array, l, m)
        mergeSort(array, m + 1, r)
        mergeSort(array, l, m, r)
    return array


# my_array = [8, 34, 12, 5, 17, 14, 20, 25]
# print(mergeSort(my_array, 0, 8))


# 6 ---> QUICK SORT
def swap(array, index1, index2):
    array[index1], array[index2] = array[index2], array[index1]


def pivot(array, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index + 1):
        if array[i] < array[pivot_index]:
            swap_index += 1
            swap(array, swap_index, i)
    swap(array, pivot_index, swap_index)
    return swap_index


def quickSort_helper(array, left, right):
    if left < right:
        pivot_index = pivot(array, left, right)
        quickSort_helper(array, left, pivot_index - 1)
        quickSort_helper(array, pivot_index + 1, right)
    return array


def quickSort(array):
    return quickSort_helper(array, 0, len(array) - 1)


# my_array = [8, 34, 12, 5, 17, 14, 20, 25]
# print(quickSort(my_array))


# 7 ---> HEAP SORT
def heapify(array, n, i):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and array[l] < array[smallest]:
        smallest = l

    if r < n and array[r] < array[smallest]:
        smallest = r

    if smallest != r:
        array[i], array[smallest] = array[smallest], array[i]
        heapify(array, n, smallest)


def heapSort(array):
    n = len(array)
    for i in range(int(n / 2) - 1, -1, -1):
        heapify(array, n, i)

    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)


my_array = [8, 34, 12, 5, 17, 14, 20, 25]
heapSort(my_array)
print(my_array)
