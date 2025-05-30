"""Describes the items in the game."""
__author__ = 'Phillip Johnson'


class Item():
    """The base class for all items"""
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)


class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)


class Rock(Weapon):
    def __init__(self):
        super().__init__(name="Rock",
                         description="A fist-sized rock, suitable for bludgeoning.",
                         value=0,
                         damage=5)


class Dagger(Weapon):
    def __init__(self):
        super().__init__(name="Dagger",
                         description="A small dagger with some rust. Somewhat more dangerous than a rock.",
                         value=10,
                         damage=10)
        
# Added rusty sword as a better weapon than dagger
class RustySword(Weapon):
    def __init__(self):
        super().__init__(name="Rusty Sword",
                         description="A sword covered in rust. Somehow more dangerous than a dagger even though it looks like it will break every swing.",
                         value=20,
                         damage=15)


class Gold(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Gold",
                         description="A round coin with {} stamped on the front.".format(str(self.amt)),
                         value=self.amt)

# Added diamond as a better prize than gold
class Diamond(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Diamond",
                         description="A rare shiny gem.",
                         value=self.amt)