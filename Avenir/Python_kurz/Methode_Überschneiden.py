class Animal:
    def __init__(self, name,age,color,fav_food):
        self.name = name
        self.age = age
        self.color = color
        self.fav_food = fav_food

    def sleep(self):
        print("ich schlafe gerade")

    def move_fast(self):
        print("Aktuelle Geschwindigkeit : 20km/h")

class Dog(Animal):

    def bark(self):
        print("wav wav")
class Cat(Animal):

    def purr(self):
        print("schnurr , schnurr")

class Tiger(Animal):

    def move_fast(self):
        print("Aktuelle Geschwindigkeit : 80km/h")



dog = Dog("bello" , 4, "brown" , "Fleisch")
tiger = Tiger("Tigriss" , 5, "Orange" , "Fleisch")

dog.move_fast()
tiger.move_fast()
