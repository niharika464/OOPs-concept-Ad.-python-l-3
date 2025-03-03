class parrot:

    #class attribute
    species="bird"

    def __init__ (self, name, age):#instance attribute
        self.name=name
        self.age=age

blu=parrot("blue",15)
woo=parrot("wook",18)

print("blu is a {}".format(blu.species))
print("woo is a {}".format(woo.species))
print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(woo.name, woo.age))
