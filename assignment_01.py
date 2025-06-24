# QUE 01 - Write a python program that takes in a student name, class. It should also take in five subject marks of the students and find the total mark and percentage. Display a result in such a way that their name, class,  and percentage are printed.

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

#printing result
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
print(f"PERCENTAGE OBTAINED : {percentage}")
if percentage<40:
    print("RESULT : fail")
else:
    print("RESULT : pass")
    if(percentage>=80):
        print("grade A")
    elif percentage<80 and percentage>60:
        print("grade B")
    else :
        print("grade C")
print("====================================")

# QUE 02 - Input 2 strings concatinate them and store in another variable. then perform generally used string methods on it like.

a = input("enter string 1 : ")
b = input("enter string 2 : ")

c = "\t"+a + b
print(f"concatinated string : {c}")

print(c.capitalize())
print(c.casefold())
print(c.lower())
print(c.upper())
print(c.swapcase())
print(c.title())

print(c.center(30,"="))
print(c.ljust(15,"*"))
print(c.rjust(15,"*"))
print(c.zfill(30))
print(c.expandtabs(5))

print(c.isalnum())
print(c.isalpha())
print(c.isascii())
print(c.isdecimal())
print(c.isdigit())
print(c.isidentifier())
print(c.islower())
print(c.isnumeric())
print(c.isprintable())
print(c.isspace())
print(c.istitle())
print(c.isupper())

print(c.count('l'))
print(c.find('world'))
print(c.rfind('o'))
print(c.index('o'))
print(c.rindex('o'))
print(c.startswith('he'))
print(c.endswith('ld'))

print(c.join(['1','2']))
print(c.split())
print(c.rsplit())
print(c.splitlines())
print(c.partition(' '))
print(c.rpartition(' '))

print(c.strip())
print(c.lstrip())
print(c.rstrip())
print(c.removeprefix('he'))
print(c.removesuffix('ld'))

print(c.replace('l','L'))
trans = str.maketrans('el','EL')
print(c.translate(trans))