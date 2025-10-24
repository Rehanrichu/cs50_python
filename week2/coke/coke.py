amount_due = 50

while amount_due > 0 :
    print("Amount Due:",amount_due)
    coin = int(input("insert coin:"))

    if coin in [25 , 10, 5]:
        amount_due -= coin
print("change owed:",abs(amount_due))
