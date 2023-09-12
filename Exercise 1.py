#Problem 1
Inventory = {"daffodil":0.35,"tulip":0.33,"crocus":0.25,"hyacinth":0.75,"bluebell":0.50}

#Problem 2
MaryOrder = {"daffodil":50,"tulip":100}

#Problem 3
Inventory["tulip"] = round(Inventory["tulip"]*1.25,2)

#Problem 4
MaryOrder["hyacinth"] = 30

#Problem 5
BulbCount = 0
TotalPrice = 0
OrderList = []
for key in MaryOrder:
    BulbName = key[:3].upper()
    BulbAmount = MaryOrder[key]
    BulbPrice = Inventory[key]*BulbAmount
    BulbCount += BulbAmount
    TotalPrice += BulbPrice
    OrderList.append(f"{BulbName:5} * {BulbAmount:>4} = ${BulbPrice:>6.2f}")
OrderList.sort()
print("You have purchased the following bulbs: ")
for i in OrderList:
    print(i)

#Problem 6
print(f"\nThank you for {BulbCount} bulbs from Bluebell Greenhouses.")
print(f"Your total comes to ${TotalPrice:>6.2f}")