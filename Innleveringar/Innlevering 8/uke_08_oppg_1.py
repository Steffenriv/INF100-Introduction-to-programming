coins = [20,10,5,1]

def return_change(payment, price):
    change = payment - price
    new_coins = []
    for i in coins:
        while change >= i:
            new_coins.append(i)
            change -= i
    return new_coins
