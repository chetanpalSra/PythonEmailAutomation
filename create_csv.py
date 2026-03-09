import csv
import os
name = input("Enter name of person: ")
email = input("Enter email: ")
year = input("Enter year of birthday: ")
month = input("Enter month of birthday: ")
date = input("Enter date of birthday: ")

data_dict = {'name':name,'email':email,'year':year,'month':month,'date':date}

file_empty = not os.path.exists('birthdays.csv')

with open("birthdays.csv", "a") as csvfile:
    writer = csv.DictWriter(csvfile,fieldnames=["name","email","year","month","date"])
    if file_empty:
        writer.writeheader() #It is compulsory to call.
    writer.writerow(data_dict)
# lovishsumaria08@gmail.com","lovebrar3630@gmail.com"