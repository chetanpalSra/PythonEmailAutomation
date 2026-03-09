##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
from datetime import datetime
import pandas as pd
import random

df = pd.read_csv("./birthdays.csv")

total_birthdays = len(df)

for i in range(total_birthdays):
    date_of_birth = df['date'][i]
    month_of_birth = df['month'][i]
    name_of_person= df['name'][i].strip()
    receiver_email = df['email'][i].strip()

    current_day = int(datetime.today().day)
    current_month = datetime.today().month

    day_today = datetime.today().strftime("%A")

    if current_day ==  date_of_birth and current_month == month_of_birth:

        select_letter_number = random.randint(1,3)
        with open(f"./letter_templates/letter_{select_letter_number}.txt", "r") as file:
                letter = file.read()
                updated_letter = letter.replace('[NAME]',name_of_person)


        sender_email = "chetanpalsra83@gmail.com"

        #Fetch password:
        with open("fetch_file.txt", "r") as f:
            password = f.readline().strip()

        #Sending the data:
        with smtplib.SMTP('smtp.gmail.com',587) as connection:
            connection.starttls()
            connection.login(sender_email,password)
            connection.sendmail(sender_email,receiver_email,f"Subject:Happy Birthday🥳!\n{updated_letter}".encode("utf-8"))

#To send emoji use .encode().

