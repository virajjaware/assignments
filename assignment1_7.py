def divisible(value1):
    if(value1%5==0):
       print("The value is",True)
    else:
       print("The value is",False)


def main():
    print("Enter number")
    no = int(input())
    ans = divisible(no)

if __name__ == "__main__":
    main()