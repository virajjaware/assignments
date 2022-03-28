def Minimum(list):
    min_num = list[0]
   # print(list[0])
    for i in list:
        if i<min_num:
            min_num = i
    return min_num

def main():
    num = 0
    i=0
    list1 = []
    num = int(input("How many numbers do you want? :: "))
    print("Enter the numbers")
    for i in range(num):
            list1.append(int(input()))
    print("Your entered numbers are ",list1)
    ans = Minimum(list1)
    print("Maximum number is",ans)
   # print("Maximum number is ",min(list1))

if __name__ == "__main__":
    main()