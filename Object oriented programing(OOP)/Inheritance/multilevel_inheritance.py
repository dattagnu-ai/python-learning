class Animal:

    def eat(self):
        print("Animal eating")


class Dog(Animal):
    def bark(self):
        print("Dog barking")


class Puppy(Dog):
    def Play(self):
        print("Puppy playing")


puppy = Puppy()
puppy.eat()
puppy.bark()
puppy.Play()
