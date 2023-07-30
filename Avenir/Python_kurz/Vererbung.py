class Dog:
    def __init__(self, name,age,color,fav_food):
        self.name = name
        self.age = age
        self.color = color
        self.fav_food = fav_food

    def sleep(self):
        print("ich schlafe gerade")

    def bark(self):
        print("wav wav")

class Cat:
    def __init__(self, name,age,color,fav_food):
        self.name = name
        self.age = age
        self.color = color
        self.fav_food = fav_food

    def sleep(self):
        print("Ich schlafe gerade")

    def purr(self):
        print("schnurr , schnurr")