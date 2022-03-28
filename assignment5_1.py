class Demo:

    Value = 10

    def __init__(self,no1,no2):
        self.no1 = no1
        self.no2 = no2

    def fun(self):
        print("This first number is from Fun class :",self.no1)
        print("This Second number is from Fun class :", self.no2)

    def gun(self):
        print("This first number is from Gun Class :", self.no1)
        print("This second number is from Gun class :", self.no2)


def main():

    #value1 = int(input("Enter first number..."))
    #value2 = int(input("Enter Second number..."))
    #value3 = int(input("Enter Third number..."))
    # value4 = int(input("Enter Fourth number..."))

  #  obj1 = Demo(value1, value2)
  #  obj2 = Demo(value3, value4)


    obj1 = Demo(51,101)
    obj2 = Demo(11,21)

    obj1.fun()
    obj1.gun()
    obj2.fun()
    obj2.gun()

    print("This is class variable : ",Demo.Value)




if __name__ == "__main__":
    main()