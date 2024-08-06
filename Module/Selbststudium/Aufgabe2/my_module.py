class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def info(self):
        print(f"Name: {self.name} ")
        print(f"Age: {self.age} ")
        print(f"City: {self.city} ")
