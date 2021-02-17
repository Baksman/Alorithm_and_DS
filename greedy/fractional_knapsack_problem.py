# a problem in combinatorial algorithm
# first us sort according to highest density

class Item:
    def  __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value/weight


def knapsackMethod(items, capacity):
    items.sort(key=lambda x: x.ratio, reverse=True)

    used_capacity = 0
    totalValue = 0
    for i in items:
        if used_capacity + i.weight < capacity:
            used_capacity += i.weight
            totalValue += i.value
        else:
            unused_weight = capacity - used_capacity
            value = i.ratio * unused_weight
            used_capacity += value
            totalValue += value
        if used_capacity == capacity:
            break

    return totalValue


items = [
    Item(20, 100),
    Item(30, 120),
    Item(10, 60)
]


print(knapsackMethod(items, 50))
