import csv
import smtplib
import random
import pandas as pd
from datetime import datetime

today = datetime.now()
today_tuple = (today.month, today.day)

data = pd.read_csv('birthdays.csv')

birthdays_dict = {(row['month'],row['date']): row for index,row in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f'./letter_templates/letter_{random.randint(1,3)}.txt'
    with open(file_path) as file:
        letter = file.read()
        updated_letter = letter.replace('[NAME]', birthday_person['name'])

        sender_email = "chetanpalsra83@gmail.com"
        receiver_email = birthday_person['email']

        # Sending the data:
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(sender_email, password)
            connection.sendmail(sender_email, receiver_email,
                                f"Subject:Happy Birthday🥳!\n{updated_letter}".encode("utf-8"))

# To send emoji use .encode().
