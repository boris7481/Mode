class Animal:
    def __init__(self, name,age,color,fav_food):
        self.name = name
        self.age = age
        self.color = color
        self.fav_food = fav_food

    def sleep(self):
        print("ich schlafe gerade")

class Dog(Animal):

    def bark(self):
        print("wav wav")
class Cat(Animal):

    def purr(self):
        print("schnurr , schnurr")

dog = Dog("bello" , 4, "brown" , "Fleisch")
dog.sleep()
print(dog.color)
print(dog.age)
print(dog.name)
print(dog.fav_food)