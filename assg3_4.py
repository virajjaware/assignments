def Frequency(list,value):
    frequency = 0
    for i in list:
        if(i == value):
            frequency = frequency + 1
    return frequency


def main():
    no = int(input("How many numbers do you want ? .."))
    list1 =[]
    print("Enter the numbers..")

    for i in range(no):
        list1.append(int(input()))
    print("your entered list is",list1)

    srch_no = int(input("Searching number is : "))

    ret = Frequency(list1,srch_no)

    print("Frenquncy of number is :",ret)

if __name__ == "__main__":
    main()