class Bank_Account:
    roi = 10.5
    def __init__(self,name,amount):
        self.acc_balance = 0
        self.n = name
        self.amt = amount

    def deposit(self):
        self.acc_balance = self.acc_balance + self.amt
        #return self.acc_balance
        print(self.n, "Deposited :", self.acc_balance)

    def withdraw(self):
        wd_amt = int(input("Enter amount to be Withdrawn: "))
        if(self.acc_balance>=wd_amt):
            self.acc_balance = self.acc_balance - wd_amt
            #return self.acc_balance
            print("After withdrawal of amount the actual balance is:", self.acc_balance)
        else:
            return "Insufficient balance"

    def cal_roi(self):
        roi = float((self.acc_balance/100)*Bank_Account.roi)
        print("Rate of interest is : ",roi)
        #return self.roi

    def display(self):

       # print(self.n, "Deposited :", self.acc_balance)
       # print("After withdrawal of amount the actual balance is:", self.acc_balance)
      #  print("Rate of interest is : ", self.roi)
        print("Net Available Balance=", self.acc_balance)


def bank():

    cust_name = input("Enter customer name: ")
    dep_amt = int(input("Enter deposited amount:"))

    bank_obj = Bank_Account(cust_name,dep_amt)
    bank_obj.deposit()
    bank_obj.withdraw()
    bank_obj.cal_roi()
    bank_obj.display()



if __name__ == "__main__":
    bank()