class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        return f"{self.name} is eating."

    def sleep(self):
        return f"{self.name} is sleeping."


class Cow(Animal):
    def __init__(self, name, age, milk_production):
        super().__init__(name, age)
        self.milk_production = milk_production

    def produce_milk(self):
        return f"{self.name} produces {self.milk_production} liters of milk daily."


class Chicken(Animal):
    def __init__(self, name, age, eggs_per_day):
        super().__init__(name, age)
        self.eggs_per_day = eggs_per_day

    def lay_eggs(self):
        return f"{self.name} lays {self.eggs_per_day} eggs per day."


class Horse(Animal):
    def __init__(self, name, age, speed):
        super().__init__(name, age)
        self.speed = speed

    def run(self):
        return f"{self.name} runs at {self.speed} km/h."



cow = Cow("Bessie", 5, 10)
chicken = Chicken("Clucky", 2, 5)
horse = Horse("Thunder", 7, 50)

print(cow.eat())
print(cow.produce_milk())
print(chicken.sleep())
print(chicken.lay_eggs())
print(horse.run())