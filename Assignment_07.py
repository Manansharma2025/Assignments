'''1) Explore more regex patterns
	Eg. The regex pattern used to validate email addresses, mobile no, string, and more '''
 
 
import re

email = "example123@mail.com"
mobile = "+91-9876543210"
username = "Jatin_007"
url = "https://www.example.com"
ip_address = "192.168.0.1"
password = "StrongPass@123"

email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
mobile_pattern = r'^(\+91[-\s]?)?[6-9]\d{9}$'
username_pattern = r'^[A-Za-z0-9_]{3,16}$'
url_pattern = r'^https?://[^\s/$.?#].[^\s]*$'
ip_pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
password_pattern = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,}$'

print(bool(re.match(email_pattern, email)))
print(bool(re.match(mobile_pattern, mobile)))
print(bool(re.match(username_pattern, username)))
print(bool(re.match(url_pattern, url)))
print(bool(re.match(ip_pattern, ip_address)))
print(bool(re.match(password_pattern, password)))

 
 
 
'''2) Explore more datetime function and uses in pandas'''


import pandas as pd

data = {
    'Date': ['2024-01-01', '2024-02-14', '2024-03-20', '2024-04-01']
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

# Display Year
df['Year'] = df['Date'].dt.year

# Display Month number 
df['Month'] = df['Date'].dt.month

# Display Month naam 
df['Month_Name'] = df['Date'].dt.month_name()

# Display Days
df['Day'] = df['Date'].dt.day

# Display names of Day
df['Day_Name'] = df['Date'].dt.day_name()

# Display Weekday number 
df['Weekday'] = df['Date'].dt.weekday

# Display Week number 
df['Week_Number'] = df['Date'].dt.isocalendar().week

# Display Quarter 
df['Quarter'] = df['Date'].dt.quarter

# Check Leap year (is or not)
df['Is_Leap_Year'] = df['Date'].dt.is_leap_year

# Display Day of year
df['Day_of_Year'] = df['Date'].dt.dayofyear

# Check last day of month (is in or not)
df['Is_Month_End'] = df['Date'].dt.is_month_end

# Check First day of month 
df['Is_Month_Start'] = df['Date'].dt.is_month_start

# Display custom formatted date
df['Formatted'] = df['Date'].dt.strftime('%d-%b-%Y')

# Print final DataFrame
print(df,"\n")



'''3) Import an meaningful csv file for data analysis and perform data cleaning, and analysis for meaningful output'''



df = pd.read_csv('students_scores.csv')
print("Original Data:\n", df)

df = df.drop_duplicates()

df['Marks'] = df['Marks'].fillna(df['Marks'].mean())
df['Name'] = df['Name'].fillna('Unknown')
df['City'] = df['City'].fillna('Unknown')

print("\nCleaned Data:\n", df)

average_marks = df['Marks'].mean()
max_marks = df['Marks'].max()
min_marks = df['Marks'].min()
top_students = df[df['Marks'] == max_marks]

print("\nAverage Marks:", average_marks)
print("Maximum Marks:", max_marks)
print("Minimum Marks:", min_marks)
print("\nTop Scoring Student(s):\n", top_students)

city_group = df.groupby('City')['Marks'].mean()
print("\nAverage Marks by City:\n", city_group)


