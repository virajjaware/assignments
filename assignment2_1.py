import Arithmatic

def main():
    no1 =0
    no2 =0

    print("Enter first number")
    no1 = int(input())
    print("Enter second number ")
    no2 = int(input())

    add = Arithmatic.sum(no1,no2)
    print("The addition of two number is",add)

    sub = Arithmatic.sub(no1, no2)
    print("The Substraction of two number is", sub)

    mul = Arithmatic.mul(no1, no2)
    print("The Multiplication of two number is", mul)

    div = Arithmatic.div(no1, no2)
    print("The Division of two number is", div)



if __name__ == "__main__":
    main()