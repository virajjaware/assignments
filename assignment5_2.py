class circle:
    pi = 3.14

    def __init__(self,radius):
        self.radius = 0.0
        self.circumference = 0.0
        self.area = 0.0

        self.radius = radius


    def accept(self):

        return self.radius

    def calArea(self):

        self.area = circle.pi * self.radius * self.radius
        return self.area

    def calcircumference(self):

        self.circumference = 2 * circle.pi * self.radius
        return self.circumference

    def display(self):

        print("The radius of circle is : ",self.radius)
        print("The area of circle is : ",self.area)
        print("The area of circumference is : ",self.circumference)





def main():

    r = int(input("Enter radius : "))

    cir_obj = circle(r)
    cir_obj.accept()
    cir_obj.calArea()
    cir_obj.calcircumference()
    cir_obj.display()


if __name__ == "__main__":
    main()