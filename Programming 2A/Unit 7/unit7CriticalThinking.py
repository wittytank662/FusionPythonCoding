'''
Use pseudocode to describe how an application (of your choice) performs a task. 
Be sure to include potential variables, functions, inheritance, and other black box programming techniques that might be used.



CLASS User
    FUNCTION placeOrder(foodItem)
        order = new Order(foodItem)
        order.process()

CLASS Order
    VAR foodItem
    FUNCTION __init__(item)
        foodItem = item

    FUNCTION process()
        checkAvailability()
        confirmOrder()
        sendToRestaurant()

FUNCTION checkAvailability()
    # Black box: checks if the item is in stock

FUNCTION confirmOrder()
    # Black box: confirms the payment and delivery details

FUNCTION sendToRestaurant()
    # Black box: sends the order to the restaurant system

# Example use
user = new User()
user.placeOrder("Pizza")
'''