fact = 1
print("Enter number :")
no = int(input())

for i in range(no,0,-1):
    fact = fact*i
print("Factorial of",no,"is",fact)