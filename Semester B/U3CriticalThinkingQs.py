Order = ["Cheeseburger", "Milkshake", "Small Fries"]
Size = 3 # Global

def FastFoodOrder():
    Size = 5 # Local
    if Size == 5:
        Order = ["Cheeseburger", "Plain burger", "Milkshake", "Water", "Medium Fries"]
    print("Your order is:", Order, "and it holds", Size, "items.")
    
FastFoodOrder()
print("Your order is:", Order, "and it holds", Size, "items.")