# ---------->>>>>  way one
# def findProfit(price):
#     profit = 0
#     for i in range(len(price) - 1):
#         for j in range(i + 1, len(price)):
#             profit = max(profit, price[j] - price[i])
#     return profit
#
#
# my_price = [7, 1, 5, 3, 6, 4]
# print(findProfit(my_price))

# ---------->>>>>  way two
# def findProfit(price):
#     profit = 0
#     minimum = price[0]
#     for i in range(1, len(price)):
#         profit = max(profit, price[i] - minimum)
#         minimum = min(minimum, price[i])
#     return profit
#
#
# my_price = [7, 1, 5, 3, 6, 4]
# print(findProfit(my_price))

# def find_Min_Max(array):
#     minimum = float("inf")
#     maximum = float("-inf")
#     for i in array:
#         minimum = min(minimum, i)
#         maximum = max(maximum, i)
#     return minimum, maximum
#
#
# my_array = [3, 5, 4, 1, 9]
# print(find_Min_Max(my_array))

def maxProduct(array):
    if len(array) == 0:
        return 0

    max_so_far = array[0]
    min_so_far = array[0]
    result = array[0]

    for i in array:
        current = i
        tem_max = max(current, max(max_so_far * current, min_so_far * current))

        min_so_far = min(current, min(max_so_far * current, min_so_far * current))
        max_so_far = tem_max
        result = max(max_so_far, result)

    return result


my_array = [2,3,-2,4]
print(maxProduct(my_array))
