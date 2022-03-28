import os
import threading

def Even(no):

    if(no%2==0):
        return 'even'


def Odd(no):
    if(no%1==0):
        print("Odd",no)


def main():
    print("Controls inside the main")

   # no1 = [1,2,3,4,5,6]

    for i in range(0, 10):
        t1 = threading.Thread(target=Even, args=(i,))
       # t2 = threading.Thread(target=Odd, args=(i,))



    t1.start()
  #  t2.start()

    t1.join()
   # t2.join()



if __name__ == "__main__":
    print("Starting application..")
    main()