############ food invoice generator ##############


foods= []
prices = []
total=0
while True:
    food =input("enter food to buy(q to quit ): ")
    if food.lower()=="q":
        break
    else:
        price=float(input(f"enter the price of a {food}: RS"))
        foods.append(food)
        prices.append(price)

print("------your cart------")
for food in foods:
    print(food, end=" ")

for price in prices:
    total+=price

print(f"your total is :{total}")
