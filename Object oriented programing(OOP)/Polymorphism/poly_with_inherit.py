class Animal:
    def sound(self):
        print("Animal make a sound")


class Dog(Animal):
    def sound(self):
        print("Bark")


class Cat(Animal):
    def sound(self):
        print("Meow")


class Cow(Animal):
    def sound(self):
        print("Moo")


def animal_sound(animal):
    animal.sound()


dog = Dog()
cat = Cat()
cow = Cow()

animal_sound(dog)
animal_sound(cat)
animal_sound(cow)
