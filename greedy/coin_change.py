
def coinChange(totalNumber, coins):
    N = totalNumber
    coins.sort()
    # highest number in the list
    index = len(coins) - 1

    while True:
        coinValue = coins[index]
        if N >= coinValue:
            print(coinValue)
            N = N - coinValue
        if N < coinValue:
            index -= 1

        if N <= 0:
            break


coins = [1,2,5,20,50,100]