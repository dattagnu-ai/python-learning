class Engine:
    def start_engine(self):
        print("Engine Started")


class GPS:
    def track(self):
        print("Location Displayed")


class Car(Engine, GPS):
    pass


c = Car()
c.start_engine()
c.track()


class A:

    def show(self):
        print("A")


class B(A):

    def show(self):
        print("B")


class C(A):

    def show(self):
        print("C")


class D(B, C):
    pass


d = D()

d.show()


class A:

    def show(self):
        print("A")


class B(A):

    def show(self):
        print("B")
        super().show()


class C(A):

    def show(self):
        print("C")
        super().show()


class D(B, C):
    def show(self):
        print("D")
        super().show()


d = D()
d.show()
