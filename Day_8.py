# ++++++++++++++ DIVIDE AND CONQUER ALGORITHME +++++++++++++

# Number Factor
def numberFactor(n):
    if n in (0, 1, 2):
        return 1
    elif n == 3:
        return 2
    else:
        subP1 = numberFactor(n - 1)
        subP2 = numberFactor(n - 3)
        subP3 = numberFactor(n - 4)
        return subP1 + subP2 + subP3


# print(numberFactor(5))


# HOUSE ROBBER PROBLEM
def houseRobber(houses, currenIndex):
    if currenIndex >= len(houses):
        return 0
    else:
        stealFirstHouse = houses[currenIndex] + houseRobber(houses, currenIndex + 2)
        skipFirstHouse = houseRobber(houses, currenIndex + 1)
        return max(stealFirstHouse, skipFirstHouse)


# houses = [6, 7, 1, 30, 8, 2, 4]
# print(houseRobber(houses, 1))

# INTERVIEW QUESTIONS ---> https://docs.google.com/document/d/1pYTmtRnmM14JpHFQQhUOLb5zAzyn4stSFyTtMJIGUYo/edit

# CONVERT ONE STRING TO ANOTHER WITH MINIMUM OPERATION
def findMinOperation(s1, s2, index1, index2):
    if index1 == len(s1):
        return len(s2) - index2
    if index2 == len(s2):
        return len(s1) - index1
    if s1[index1] == s2[index2]:
        return findMinOperation(s1, s2, index1 + 1, index2 + 1)
    else:
        deleteOp = 1 + findMinOperation(s1, s2, index1, index2 + 1)
        insertOp = 1 + findMinOperation(s1, s2, index1 + 1, index2)
        replaceOp = 1 + findMinOperation(s1, s2, index1 + 1, index2 + 1)
        return min(deleteOp, insertOp, replaceOp)


# print(findMinOperation("cat", "cta", 0, 0))


# ZERO ONE KNAPSACK
class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight


def zoKnapsack(items, capacity, currentIndex):
    if capacity <= 0 or currentIndex < 0 or currentIndex >= len(items):
        return 0
    elif items[currentIndex].weight <= capacity:
        profit1 = items[currentIndex].profit + zoKnapsack(items, capacity - items[currentIndex].weight,
                                                          currentIndex + 1)
        profit2 = zoKnapsack(items, capacity, currentIndex + 1)
        return max(profit1, profit2)
    else:
        return 0


mango = Item(31, 3)
apple = Item(26, 1)
orange = Item(17, 2)
banana = Item(72, 5)

items = [mango, apple, orange, banana]


# print(zoKnapsack(items, 7, 0))


# LONGEST COMMON SEQUENCE
def findCommonString(s1, s2, index1, index2):
    if index1 == len(s1) or index2 == len(s2):
        return 0
    if s1[index1] == s2[index2]:
        return 1 + findCommonString(s1, s2, index1 + 1, index2 + 1)
    else:
        op1 = findCommonString(s1, s2, index1, index2 + 1)
        op2 = findCommonString(s1, s2, index1 + 1, index2)
        return max(op1, op2)


# print(findCommonString("elephant", "eretpat", 0, 0))

# LONGEST PALINDROMIC SUBSEQUENCE
def findLPS(s, startIndex, endIndex):
    if startIndex > endIndex:
        return 0
    elif startIndex == endIndex:
        return 1
    elif s[startIndex] == s[endIndex]:
        return 2 + findLPS(s, startIndex + 1, endIndex - 1)
    else:
        op1 = findLPS(s, startIndex, endIndex - 1)
        op2 = findLPS(s, startIndex + 1, endIndex)
        return max(op1, op2)


# print(findLPS("HAKKAFHDDKKAH", 0, 4))
