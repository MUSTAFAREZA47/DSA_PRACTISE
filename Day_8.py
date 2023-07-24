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


houses = [6, 7, 1, 30, 8, 2, 4]
print(houseRobber(houses, 1))

# INTERVIEW QUESTIONS ---> https://docs.google.com/document/d/1pYTmtRnmM14JpHFQQhUOLb5zAzyn4stSFyTtMJIGUYo/edit
