class parrot:

    #class attribute
    species="bird"

    def __init__ (self, name, age):#instance attribute
        self.name=name
        self.age=age

    def sing(self,song):
        return "{} sings {}".format(self.name,song)
    
    def dance(self):
        return"{} is dancing...".format(self.name)
    

p=parrot("kitty",12)

print(p.sing("twinkle twinlke little stars"))
print(p.dance())
