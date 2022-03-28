from functools import reduce

def Even(eno):
    if(eno%2==0):
        return True
    else:
        return False

def Increment(no):
    return  no**2

def addition(a,b):
    return a + b


def main():   # Function call

    size = int(input("Enter elements you want:"))
    data= []

    print("Please enter number..")
    for i in range(size):
        data.append(int(input()))
    print("List contains are : ",data)


    newdata = list(filter(Even,data))
    print("Data after filter",newdata)



    Incrementlist = list(map(Increment,newdata))
    print("Data after map", Incrementlist)



    ans = reduce(addition,Incrementlist)
    print("Data after reduce :",ans)


if __name__ == "__main__":
    main()