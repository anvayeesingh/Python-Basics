class Dog:
    species = "Canis lupus familiaris"
    def __init__(self, breed, name):
        self.breed = breed  
        self.name = name    

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Breed: {self.breed}")
        print(f"Species: {self.species}")
        print("-" * 25)

dog1 = Dog("German Shepherd", "Rex")
dog2 = Dog("Golden Retriever", "Buddy")

print("--- Dog 1 Details ---")
dog1.display_details()

print("--- Dog 2 Details ---")
dog2.display_details()
