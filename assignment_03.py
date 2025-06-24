#QUE - Write a function for basic math operations like add multiply substract divide and use this in your program, take 2 number input from user.

def addition(a,b):
    print(f"Addition {a}+{b} is : {a+b}")
def subtraction(a,b):
    print(f"subtraction {a}-{b} is : {a-b}")
def multiply(a,b):
    print(f"multiply {a}*{b} is : {a*b}")
def divide(a,b):
    print(f"division {a}/{b} is : {a/b}")

print("-"*50)
print("BASIC CALCULATOR".center(50))
print("-"*50)
while True:
    a = int(input("enter first number : "))
    b = int(input("enter second number : "))

    print("""
    1. addition
    2. subtraction
    3. multiplication
    4. division
    """)

    n = int(input("Enter your choice : "))

    if n == 1:
        addition(a,b)
        break
    elif n == 2:
        subtraction(a,b)
        break
    elif n == 3:
        multiply(a,b)
        break
    elif n == 4:
        divide(a,b)
        break
    else:
        print("invalid choice\nplease enter correct choice")

#QUE - Write a program to check Palindrome Number
#          1. The Number  which is equal to reverse number know as Palindrome Number.
#          For example Number 12321 is a Palindrome Number, because 12321 is equal to its reverse Number 12321.
#          2. Steps for checking Palindrome number
#               1. Find reverse of the given number.
#               2. Compare that number with the reverse number.
#               3. If number and its reverse is equal then it is a Palindrome Number otherwise not.

def is_palindrome(n):
    x = n
    rev = 0
    while n!=0:
        rev =rev*10 + n%10
        n = n//10
    if x == rev:
        print(f"number {x} is a palindrome number.")
    else :
        print(f"number {x} is not a palindrome number.")

num = int(input("enter a number : "))
is_palindrome(num)

