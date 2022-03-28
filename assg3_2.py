def Maximum(list):
    max_num = list[0]
    for i in list:
        if i>max_num:
            max_num = i
    return max_num

def main():
    num = 0
    i=0
    list1 = []
    num = int(input("How many numbers do you want? :: "))
    print("Enter the numbers")
    for i in range(num):
            list1.append(int(input()))
    print("Your entered numbers are ",list1)
    ans = Maximum(list1)
    print("Maximum number is",ans)
   # print("Maximum number is ",max(list1))

if __name__ == "__main__":
    main()