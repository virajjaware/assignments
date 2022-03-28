
def main():
    no=int(input("enter the number"))
  #  no1 = int(input("enter the end position"))
    #for i in range(no,20,2):
    if(no%2==0):
        for i in range(no,20,2):
            print(i)
    else:
        print("Odd number")

if __name__ == "__main__":
    main()