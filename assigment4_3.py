from functools import reduce

def Chkfunction(no):
    if(no>=70 and no<=90):
        return True
    else:
        return False

def Increment(no):
    return  no+10

def addition(a,b):
    return a + b


def main():   # Function call

    size = int(input("Enter elements you want:"))
    data= []

    print("Please enter number..")
    for i in range(size):
        data.append(int(input()))
    print("List contains are : ",data)


    newdata = list(filter(Chkfunction,data))
    print("Data after filter",newdata)



    Incrementlist = list(map(Increment,newdata))
    print("Data after map", Incrementlist)



    ans = reduce(addition,Incrementlist)
    print("Data after reduce :",ans)


if __name__ == "__main__":
    main()