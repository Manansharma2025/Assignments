#QUE -  Do practise of the session
#ANS - Done

#QUE -  In your last program where you find the total and percentage of a student's marks of 5 subject, find the grade of the student using conditional statement. Eg. grade 'A' if percentage is greator than or equals to 60, 'B' for  percentage is greator than or equals to 50 and less than 60,  'C' for  percentage is greator than or equals to 40 and less than 50,  'D' for  percentage is greator than or equals to 33 and less than 40, otherwise 'Fail'

name = input("enter the name of student : ")
Class = input("enter the class of student : ")

m1 = int(input("enter the marks of subject 1 : "))
m2 = int(input("enter the marks of subject 2 : "))
m3 = int(input("enter the marks of subject 3 : "))
m4 = int(input("enter the marks of subject 4 : "))
m5 = int(input("enter the marks of subject 5 : "))

total_marks_ob = m1+m2+m3+m4+m5
total_marks = 500
percentage = total_marks_ob/total_marks*100

print("====================================")
a = "RESULTS 2025"
print(a.center(35))
print("====================================")
print(f"Name : {name}")
print(f"class : {Class}")
print("====================================")
print(f"subject 1 : {m1}")
print(f"subject 2 : {m2}")
print(f"subject 3 : {m3}")
print(f"subject 4 : {m4}")
print(f"subject 5 : {m5}\n")
print(f"TOTAL MARKS OBTAINED : {total_marks_ob}")
print("====================================")
print(f"PERCENTAGE OBTAINED : {round(percentage,2)}")
if percentage<33:
    print("RESULT : fail")
else:
    print("RESULT : pass")
    if(percentage>=60):
        print("grade : A")
    elif percentage<60 and percentage>=50:
        print("grade : B")
    elif percentage<500 and percentage>=40:
        print("grade : C")
    else :
        print("grade : D")
print("====================================")

#QUE - Input a number from user and find its factorial using for loop

n = int(input("enter the number : "))
fact=1
for i in range(1,n+1):
    fact *= i
print(fact)
'''

#QUE - Create a billing program using list. Program should have options to
# 1. Create Bill
# 2. Display Item Price and total bill amount
# 3. Display Total
# 4. Exit

'''
items = []
quantities = []
prices = []

print("===================BILLING SYSTEMS==================")

while True:
    print("Billing System Menu : ")
    print("1. Create Bill")
    print("2. Display Items and Total")
    print("3. Display Total Amount")
    print("4. Exit")

    choice = input("Enter your choice (1-4) : ")

    if choice == '1':
        while True:
            item = input("Enter item name (or 'done' to finish): ")
            if item.lower() == 'done':
                break

            items.append(item)

            while True:
                qty_input = input("Enter quantity: ")
                if qty_input.isdigit():
                    quantity = int(qty_input)
                    break
                else:
                    print("Error: Quantity must be a whole number!")

            quantities.append(quantity)


            while True:
                price_input = input("Enter price per unit: ")
                if price_input.isdigit():
                    price = int(price_input)
                    break
                else:
                    print("Error: Price must be a number!")

            prices.append(price)

    elif choice == '2':
        if not items:
            print("No items in the bill yet!")
        else:
            print("\n{:<20} {:<10} {:<10} {:<10}".format("Item", "Quantity", "Price", "Total"))
            print("-" * 50)
            grand_total = 0
            for i in range(len(items)):
                total = quantities[i] * prices[i]
                grand_total += total
                print("{:<20} {:<10} {:<10} {:<10}".format(items[i], quantities[i], prices[i], total))
            print("\nGrand Total : ",grand_total)

    elif choice == '3':
        if not items:
            print("No items in the bill yet!")
        else:
            grand_total = 0
            for i in range(len(items)):
                grand_total += quantities[i] * prices[i]
            print("\nTotal Bill Amount : ", grand_total)

    elif choice == '4':
        print("Thank you for using the billing system!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 4.")


#QUE - Write a  Python program to find the smallest number in a list.
#QUE - Write a  Python program to find the second greatest number in a list.
#QUE - Write a  Python program to find the second smallest number in a list.

#method 1
list1 = []
n = int(input("Enter the number of elements you want to add: "))
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    list1.append(element)

smallest = float("inf")
largest = float("-inf")
for i in list1:
    smallest = min(smallest, i)
    largest = max(largest, i)
print(f"Smallest number is : {smallest}")

second_small = float("inf")
for i in list1:
    if i > smallest and i < second_small:
        second_small = i
print(f"Second smallest number is : {second_small}")

second_large = float("-inf")
for i in list1:
    if i > second_large and i < largest:
        second_large = i
print(f"Second largest number is : {second_large}")

#method 2
list1.sort()
print(f"smallest element is : {list1[0]}")
print(f"second smallest element is : {list1[1]}")
print(f"second largest element is : {list1[-2]}")