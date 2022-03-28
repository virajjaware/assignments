def chkNum(value1):
    if(value1%2==0):
        print("The given number",value1, "is even")
    else:
        print("The given number",value1, "is odd")


def main():
    print("Enter number")
    no = int(input())

    ans = chkNum(no)

if __name__ == "__main__":
    main()