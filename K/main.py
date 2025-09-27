coins_om, own_coins = map(int, input().split())

if coins_om < own_coins:
    print(coins_om + 1)
elif coins_om > own_coins:
    print(0)
else:
    print(coins_om)