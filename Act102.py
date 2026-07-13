class FamilyMember:
    def __init__(self, eye_color , height_cm):
        self.eye_color= eye_color
        self.height_cm = height_cm
    def show_traits(self):
        print("Height in cm ", self.height_cm)
        print("Eye color ", self.eye_color)

class Kid(FamilyMember):
    def __init__(self, name, age, eye_color, height_cm):
        self.name = name
        self.age = age
        super().__init__(eye_color, height_cm)

    def show_traits(self):
        print("Name ",self.name)
        print("Age:", self.age)
        super().show_traits()

    def Favorite_hobby(self, hobby):
        print(self.name,"loves" ,hobby)
child = Kid("Anvayee",10, "brown", 141)
child.show_traits()
child.Favorite_hobby("Crafting and painting")

print("Is Kid a sub class of FamilyMember? ", issubclass (Kid, FamilyMember))
    
    

        