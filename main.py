import smtplib
import datetime as dt
import random
import pandas as pd
import os

MY_EMAIL = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("MY_PASSWORD")

today_day = dt.datetime.now().day
today_month = dt.datetime.now().month

birthdays = pd.read_csv('birthdays.csv')
birthdays_dict = {
    (row['month'], row['day']): row.to_dict()
    for _, row in birthdays.iterrows()
}

if (today_month, today_day) in birthdays_dict:
    birthday_person = (birthdays_dict[today_month, today_day])
    birthday_email = birthday_person['email']
    birthday_name = birthday_person['name']

letters_list = []
with open('letter_templates/letter_1.txt', 'r') as letter1:
    x = letter1.read()
    letters_list.append(x.replace('[NAME]', birthday_name))
with open('letter_templates/letter_2.txt', 'r') as letter2:
    y = letter2.read()
    letters_list.append(y.replace('[NAME]', birthday_name))
with open('letter_templates/letter_3.txt', 'r') as letter3:
    z = letter3.read()
    letters_list.append(z.replace('[NAME]', birthday_name))

random_letter = random.choice(letters_list)

with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL,
                         to_addrs=birthday_email,
                         msg= 'Subject:Happy Birthday!\n\n' \
                         f'{random_letter}')