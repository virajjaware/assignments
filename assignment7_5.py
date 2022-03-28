fact = 1
def Fact_fun(n):
    global fact
    for i in range (n,0,-1):
        fact = fact*i
    return fact
    Fact_fun()


def main():
    num = int(input("Enter the number : "))

    ans = Fact_fun(num)
    print("Factorial number is:",ans)

if __name__ == "__main__":
    main()