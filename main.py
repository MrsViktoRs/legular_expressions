import re
from pprint import pprint
import csv

contacts_list = []
fio_pattern = r'([А-ЯЁ]\w+).([А-ЯЁ]+\w+)\ ([А-ЯЁ]+\w+)'
organization_pattern = r'\b(ФНС|Минфин)\b'
phone_pattern = r'(\+\d{1}|\,8)\D*(\d{3})\D*(\d{3})\D*(\d{2})\D*(\d{2})'
email_pattern = r'\b[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


with open('phonebook_raw.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for rows in reader:
        line = ','.join(rows)
        fio = re.search(fio_pattern, line)
        org = re.search(organization_pattern, line)
        phone_sub = re.sub(phone_pattern, r'+7(\2)\3-\4-\5', line)
        phone = re.search(phone_pattern, phone_sub)
        email_match = re.search(email_pattern, line)
        if fio:
            lastname = fio.group(1)
            firstrname = fio.group(2)
            surname = fio.group(3)
            if org:
                organization = org.group(0)
                if phone:
                    number = phone.group(0)
                    if email_match:
                        email = email_match.group(0)
                        key = f'\n{lastname} {firstrname} {surname}, {organization}, {number}, {email}'
                        contacts_list.append(key)
                    else:
                        key = f'\n{lastname} {firstrname} {surname}, {organization}, {number}'
                        contacts_list.append(key)
with open("phonebook.csv", "w", encoding='utf-8') as file:
    datawriter = csv.writer(file)
    datawriter.writerow(contacts_list)
print(contacts_list)
