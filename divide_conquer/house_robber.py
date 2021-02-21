
def houseRobber(houses, currentHouse):
    if currentHouse >= len(houses):
        return 0
    else:
        # two options either we are stealing/skipping  the first  house
        steal_first_house = houses[currentHouse] + \
            houseRobber(houses, currentHouse+2)
        skip_first_house = houseRobber(houses, currentHouse+1)
        print(steal_first_house)
        print(skip_first_house)
        return max(steal_first_house, skip_first_house)


houses = [6, 7, 1, 30, 8, 2, 4]
# 0 signifies that we are stealing from first house
print(houseRobber(houses, 0))
