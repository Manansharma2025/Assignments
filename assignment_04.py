#QUE - Create a CSV file for address book, CSV file should have column for name, address, mobile, email. Insert 2-3 dummy data

import csv
data = [["name","address", "mobile","email"],
        ["kanishk", "jaipur","9079123493","kanishkgargggc@gmail.com"],
        ["jatin","alwar","9764548624","khandu@gmail.com"],
        ["krishna", "jaipur","8784568465","krishna@yahoo.com"]]
with open("address.csv","w",newline="") as file:
    writer = csv.writer(file)
    for i in data:
        writer.writerow(i)

import requests as req
def weather(city,apiid):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiid}"
    try :
        response = req.get(url)
        response.raise_for_status()
        data = response.json()

        print(f"CITY NAME : {data['name']}".center(30))
        print("-"*30)
        print(f"Temperature : {data['main']['temp'] - 273}\u00b0C")
        print(f"feels like : {data['main']['feels_like'] - 273}\u00b0C")
        print(f"Humidity : {data['main']['humidity']}%")
        print(f"wind speed : {data['wind']['speed']}")
    except req.exceptions.RequestException as e:
        print(f"Error fetching weather data : {e}")
apiid = "e6615296908e9bad7a1a1e9189585698"
city = input("enter city name : ")
weather(city,apiid)



import sqlite3
con = sqlite3.connect("university_assignment.db")


con.execute("""
CREATE TABLE students(
S_ID INTEGER PRIMARY KEY AUTOINCREMENT,
S_NAME VARCHAR(50),
S_CLASS VARCHAR(50),
c_ID INT,
S_EMAIL VARCHAR(30),
S_PHONE VARCHAR(10),
S_ADD VARCHAR(100))
""")

con.execute("""
CREATE TABLE faculty(
F_ID INTEGER PRIMARY KEY AUTOINCREMENT,
F_NAME VARCHAR(50),
F_EMAIL VARCHAR(30),
F_PHONE VARCHAR(10),
F_ADD VARCHAR(100),
F_SALARY INT)
""")

con.execute("""
CREATE TABLE courses(
C_ID INTEGER PRIMARY KEY AUTOINCREMENT,
C_NAME VARCHAR(50),
C_DURATION INT,
C_FEE INT,
F_ID INT)
""")

con.execute('''
INSERT INTO students VALUES
(01, "Kanishk", "B.Tech", 001, "Kanishkgargggc@gmail.com","9079123493","jaipur city"),
(02, "jatin", "B.Tech", 001, "jatinkhandu@gmail.com","9784585593","alwar"),
(03, "yash", "B.Tech", 001, "yashmohnani@gmail.com","8785878583","pali"),
(04, "keshav", "BCA", 002, "keshavsoni1304@yahoo.com","8058405772","gangapur city")
''')

con.execute('''
INSERT INTO faculty VALUES
(1001, "Vikram","vikram78@skit.ac.in","9898989898","jaipur",85000),
(1002, "manish","manishbh@skit.ac.in","7858578548","udaypur",80000),
(1003, "ramesh","rameshkumar@gmail.com","7789456158","kota",95000)
''')

con.execute('''
INSERT INTO courses VALUES
(001, "B.Tech",4,100000,1002),
(002,"BCA",3,600000,1001),
(003,"B.Sc",3,450000,1003)
''')
con.commit()

data_student = con.execute("SELECT * FROM students")
data_faculty = con.execute("SELECT * FROM faculty")
data_courses = con.execute("SELECT * FROM courses")

print("\nSTUDENT TABLE : ")
for i in data_student:
    print(i)
print("\nFACULTY TABLE : ")
for i in data_faculty:
    print(i)
print("\nCOURSES TABLE : ")
for i in data_courses:
    print(i)

print("showing data of faculties whose salary is more than 82000 : ")
data_faculty = con.execute("SELECT * FROM faculty WHERE F_SALARY > 82000")
for i in data_faculty:
    print(i)

id_del_stu = input("\nEnter id to be deleted from student table : ")
con.execute(f"DELETE FROM students WHERE S_ID={id_del_stu}")
con.commit()
print("\nData After Deletion : ")
data_student = con.execute("SELECT * FROM students")
data_faculty = con.execute("SELECT * FROM faculty")
data_courses = con.execute("SELECT * FROM courses")

print("\nSTUDENT TABLE : ")
for i in data_student:
    print(i)
print("\nFACULTY TABLE : ")
for i in data_faculty:
    print(i)
print("\nCOURSES TABLE : ")
for i in data_courses:
    print(i)

id_up_stu = input("\nEnter the id you want to change name for in students : ")
new_name = input(f"Enter the new name for id {id_up_stu} : ")
con.execute(f"UPDATE students set S_NAME = {new_name} WHERE S_ID = {id_up_stu}")
con.commit()

print("\nData After Updation : ")
data_student = con.execute("SELECT * FROM students")
data_faculty = con.execute("SELECT * FROM faculty")
data_courses = con.execute("SELECT * FROM courses")

print("\nSTUDENT TABLE : ")
for i in data_student:
    print(i)
print("\nFACULTY TABLE : ")
for i in data_faculty:
    print(i)
print("\nCOURSES TABLE : ")
for i in data_courses:
    print(i)