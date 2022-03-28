def chkNum(value1):
    if(value1>0):
        print("The number is positive")
    elif (value1==0):
        print("the value is 0")
    else:
        print("the value is negative")


def main():

    no= int(input("enter a number"))
    chkNum(no)
    #print("The given number",chkNum)


if __name__ == "__main__":
    main()