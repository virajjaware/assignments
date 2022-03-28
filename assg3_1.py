def Addition(value):
    sum = 0
    for i in range(len(value)):
        sum = sum+value[i]
    return sum

def main():
    num = 0
    i=0
    list1 = []

    print("How many numbers do you want? :: ")
    num = int(input())

    print("Enter the numbers")

    for i in range(num):
            list1.append(int(input()))
    print("Your entered numbers are ",list1)

    ans = Addition(list1)

    print("Addition of number",ans)

if __name__ == "__main__":
    main()