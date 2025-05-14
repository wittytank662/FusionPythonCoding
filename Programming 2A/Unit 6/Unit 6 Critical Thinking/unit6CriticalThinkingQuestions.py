import copy
order = [["sweater", "large", "white"], ["jeans", "10 tall", "boot cut"], ["sunglasses", "oval", "silver"]]
deepOrder = copy.deepcopy(order)
copiedItem = deepOrder[1]
deepOrder.remove(deepOrder[1])

deepOrder.insert(2, copiedItem)   

print(order)
print(deepOrder)

'''
OUTPUT:

[['sweater', 'large', 'white'], ['jeans', '10 tall', 'boot cut'], ['sunglasses', 'oval', 'silver']]
[['sweater', 'large', 'white'], ['sunglasses', 'oval', 'silver'], ['jeans', '10 tall', 'boot cut']]
'''


# QUESTION 3

from abc import ABC, abstractmethod

class OrderableItem(ABC):
    @abstractmethod
    def get_price(self):
        pass

    @abstractmethod
    def get_description(self):
        pass


