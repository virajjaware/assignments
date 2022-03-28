class Arithmatic:
    def __init__(self,value1,value2):
       # value1 = 0
       # value2 = 0
        ans = 0.0

        self.value1 = value1
        self.value2 = value2

    def Accept(self):

        return self.value1,self.value2

    def Addition(self):
        self.add = self.value1 + self.value2
        return self.add

    def Substraction(self):
        self.sub = self.value1 - self.value2
        return self.sub

    def Multiplication(self):
        self.mul = self.value1 * self.value2
        return self.mul

    def Division(self):
        self.ans = self.value1 / self.value2
        return self.ans

    def Display(self):
        print("The addition of two number is : ",self.add)
        print("The Substraction of two number is : ", self.sub)
        print("The Multiplication of two number is : ", self.mul)
        print("The Division of two number is : ", self.ans)


def main():

    no1 = int(input("Enter the first number ::"))
    no2 = int(input("Enter the first number ::"))

    art_obj = Arithmatic(no1,no2)
    art_obj.Accept()
    art_obj.Addition()
    art_obj.Substraction()
    art_obj.Multiplication()
    art_obj.Division()
    art_obj.Display()


if __name__ == "__main__":
    main()