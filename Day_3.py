from array import array

arr = [1, 5, 4, 8, 3, 9, 2, 4]
first = 0
second = 0

for i in arr:
    if i > first:
        second = first
        first = i
    elif i > second:
        second = i
# print(first, second)


target = 7


def pairSum(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                continue
            elif arr[i] + arr[j] == target:
                print(i, j)


# pairSum(arr, target)

# my_dict = dict()
# my_arr = array.append
# print(my_dict)
# my_dict2 = {}
# print(my_dict2)

my_dict = {'name': 'Ahmed', 'age': 24, 'address': 'sasaram'}


#  TRAVERSING DICTIONARY
# for key in my_dict:
#     print(key, my_dict[key])


#  SEARCHING DICTIONARY
def searchDict(dic, value):
    for key in dic:
        if dic[key] == value:
            return key, value
    return 'Nothing Found'


# print(searchDict(my_dict, 24))

#  METHODS IN DICTIONARY
# Link : https://www.w3schools.com/python/python_dictionaries_methods.asp
# my_dict.clear()
# my_dict.copy()
# my_dict.formkeys()

