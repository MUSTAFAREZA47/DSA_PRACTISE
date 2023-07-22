nums = [1, 2, 3, 1]


def duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


# print(duplicate(nums))

#  TUPLES

newTuples = ('a', 'b', 'c', 'd', 'e')
oneTuples = (1, 2, 3, 4, 5, 6)
twoTuples = 'A','X','Z','D','P','L'
# zipTup = zip(newTuples, twoTuples)

# print(newTuples * 2)
print(" ".join(newTuples))

# print('c' in newTuples)

# for i in newTuples:
#     print(i)

# print(newTuples[1:3])
