def Addition(value1,value2):
    sum = value1+value2
    return  sum

def main():
    no1 =0
    no2 =0

    print("Enter first number")
    no1 = int(input())
    print("Enter second number ")
    no2 = int(input())

    ans = Addition(no1,no2)
    print("The addition of two number is",ans)



if __name__ == "__main__":
    main()