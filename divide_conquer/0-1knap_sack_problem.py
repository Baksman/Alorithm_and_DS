# cannot break item into smaller unit
# has capacity C

# find maximum profit such that weight is less than so so..


class Item:
    def __init__(self, weight, profit):
        self.profit = profit
        self.weight = weight


def zoKnapSackProblem(items: list(Item), capacity, currentIndex):
    if capacity <= 0 or currentIndex < 0 or currentIndex < len(items):
        return 0
    elif items[currentIndex].weight <= capacity:
        # if we pick current item
        profit1 = items[currentIndex].profit + \
            zoKnapSackProblem(
                items, capacity-items[currentIndex].weight, currentIndex+1)
        # if we decide to choose next item for the next
        profit2 = zoKnapSackProblem(
            items, capacity, currentIndex+1)
        return max(profit1, profit2)
    else:
        return 0
