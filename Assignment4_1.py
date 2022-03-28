powerX = lambda a ,b: a ** b

def main():

    base = int(input("Enter a base value.."))
    exp = int(input("Enter a Exponent value"))

    ans = powerX(base,exp)
    print("Power of",base ,"base is : ",ans)

if __name__ == "__main__":
    main()
