##inerting in array
my_array = [1,2,3,4,2,8]

##my_array.insert(0, 9)

##print(my_array)

def tranverseArray(my_array):
    for i in my_array:
        print(i)


##tranverseArray(my_array)

def accessElement(my_array, index):
    if index > len(my_array):
        print('There is not any element in this index')
    else:
        print(my_array[index])

##accessElement(my_array, 3)

def linearSearch(my_array, target):
    for i in range(len(my_array)):
        if my_array[i] == target:
            print(i, my_array[i])
    return -1

##linearSearch(my_array, 3)

## Array Methods

my_array.remove(2)
my_array.append(1340)
my_array.insert(0, 540)

new_array = [110, 150, 44]
my_array.extend(new_array)
my_array.pop()
my_array.count(8)



print(my_array)