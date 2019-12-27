#!/usr/bin/python3

# Thunderbird UTF-8 CSV to abook

import sys
import csv
import typing
import datetime

class Counter():
    def __init__(self):
        self.counter = -1

    def next(self):
        self.counter = self.counter + 1
        return self.counter


class Contact():
    def __init__(self):
        self.id = ''
        self.name = ''
        self.emails = [ ]
        self.birthday = None
        self.firstname = ''
        self.lastname =''
        self.country = ''
        self.state = ''
        self.zip = ''
        self.city = ''
        self.address = ''
        self.address2 = ''
        self.worktitle = ''
        self.workname = ''
        self.workdept = ''
        self.workcountry = ''
        self.workstate = ''
        self.workzip = ''
        self.workcity = ''
        self.workaddress = ''
        self.workaddress2 = ''
        self.phone = ''
        self.workphone = ''
        self.mobile = ''
        self.fax = ''
        self.pager = ''
        self.nick = ''
        self.url = ''
        self.url2 = ''
        self.notes = ''
        self.anniversary = ''

    def get_id (self):
        return self.id

    def set_id (self, id):
        self.id = id

    def get_name(self):
        return self.name

    def set_name(self, name: typing.List[str]):
        self.name = name

    def get_emails(self) -> typing.List[str]:
        return self.emails

    def set_emails(self, emails):
        self.emails = emails

    def get_birthday(self) -> datetime.date:
        return self.birthday

    def set_birthday(self, birthday: datetime.date):
        self.birthday = birthday

    def get_firstname(self):
        return self.firstname

    def set_firstname(self, firstname):
        self.firstname = firstname

    def get_lastname(self):
        return self.lastname

    def set_lastname(self, lastname):
        self.lastname =lastname

    def get_country(self):
        return self.country

    def set_country(self, country):
        self.country = country

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

    def get_zip(self):
        return self.zip

    def set_zip(self, zip):
        self.zip = zip

    def get_city(self):
        return self.city

    def set_city(self, city):
        self.city = city

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_address2(self):
        return self.address2

    def set_address2(self, address2):
        self.address2 = address2

    def get_worktitle(self):
        return self.worktitle

    def set_worktitle(self, worktitle):
        self.worktitle = worktitle

    def get_workname(self):
        return self.workname

    def set_workname(self, workname: str):
        self.workname = workname

    def get_workdept(self):
        return self.workdept

    def set_workdept(self, workdept):
        self.workdept = workdept

    def get_workcountry(self):
        return self.workcountry

    def set_workcountry(self, workcountry):
        self.workcountry = workcountry

    def get_workstate(self):
        return self.workstate

    def set_workstate(self, workstate):
        self.workstate = workstate

    def get_workzip(self):
        return self.workzip

    def set_workzip(self, zip):
        self.workzip = zip

    def get_workcity(self):
        return self.workcity

    def set_workcity(self, workcity):
        self.workcity = workcity

    def get_workaddress(self):
        return self.workaddress

    def set_workaddress(self, workaddress):
        self.workaddress = workaddress

    def get_workaddress2(self):
        return self.workaddress2

    def set_workaddress2(self, workaddress2):
        self.workworkaddress2 = workaddress2

    def get_phone(self):
        return self.phone

    def set_phone(self, phone):
        self.phone = phone

    def get_workphone(self):
        return self.workphone

    def set_workphone(self, workphone):
        self.workphone = workphone

    def get_mobile(self):
        return self.mobile

    def set_mobile(self, mobile):
        self.mobile = mobile

    def get_fax(self):
        return self.fax

    def set_fax(self, fax):
        self.fax = fax

    def get_pager(self):
        return self.pager

    def set_pager(self, pager):
        self.pager = pager

    def get_nick(self):
        return self.nick

    def set_nick(self, nick):
        self.nick = nick

    def get_url(self):
        return self.url

    def set_url(self, url):
        self.url = url

    def get_url2(self):
        return self.url2

    def set_url2(self, url2):
        self.url2 = url2

    def get_notes(self):
        return self.notes

    def set_notes(self, notes):
        self.notes = notes

    def get_anniversary(self):
        return self.anniversary

    def set_anniversary(self, anniversary):
        self.anniversary = anniversary


class Reader():
    def __init__(self, counter):
        self.counter = counter

    def read(self, file_in):
        tb_csv_reader = csv.DictReader(file_in, delimiter = ',', quotechar = '"')
        contacts = [ ]
        for row in tb_csv_reader:
            contact = Contact()
            contact.set_id(counter.next())
            contact.set_name(row["Display Name"])
            contact.set_firstname(row["First Name"])
            contact.set_lastname(row["Last Name"])

            contact.get_emails().append(row["Primary Email"])
            contact.get_emails().append(row["Secondary Email"])

            birthday_year = row["Birth Year"]
            birthday_month = row["Birth Month"]
            birthday_day = row["Birth Day"]
            birthday = None
            if birthday_year is not '' and birthday_month is not '' and birthday_day is not '':
                birthday = datetime.date(int(birthday_year), int(birthday_month), int(birthday_day))
            contact.set_birthday(birthday)

            contact.set_worktitle(row["Job Title"])
            contact.set_workname(row["Organization"])
            contact.set_workdept(row["Department"])
            contact.set_workcountry(row["Work Country"])
            contact.set_workstate(row["Work State"])
            contact.set_workzip(row["Work ZipCode"])
            contact.set_workcity(row["Work City"])
            contact.set_workaddress(row["Work Address"])
            contact.set_workaddress2(row["Work Address 2"])

            contact.set_country(row["Home Country"])
            contact.set_state(row["Home State"])
            contact.set_zip(row["Home ZipCode"])
            contact.set_city(row["Home City"])
            contact.set_address(row["Home Address"])
            contact.set_address2(row["Home Address 2"])

            contact.set_phone(row["Home Phone"])
            contact.set_workphone(row["Work Phone"])
            contact.set_mobile(row["Mobile Number"])
            contact.set_fax(row["Fax Number"])
            contact.set_fax(row["Pager Number"])

            contact.set_nick(row["Nickname"])
            contact.set_url(row["Web Page 1"])
            contact.set_notes(row["Notes"])
            contact.set_anniversary(row[""])

            contacts.append(contact)

        return contacts

class Writer():
    def __init__(self):
        pass

    def header_text(self):
        text = ''

        text = text + "# abook addressbook file\n"
        text = text + "\n"
        text = text + "[format]\n"
        text = text + "program=abook\n"
        text = text + "version=0.6.1\n"
        text = text + "\n"

        return text

    def emails_text(self, emails):
        text = ''

        text = text + "email="

        for i in range(0, len(emails)):
            if i > 0:
                text = text + ","

            text = text + emails[i]

        text = text + '\n'

        return text

    def attr_str_text(self, attr: str, value: str) -> str:
        text = ''
        text = text + attr
        text = text + '='
        text = text + value
        text = text + '\n'
        return text

    def attr_date_text(self, attr: str, value: datetime.date) -> str:
        text = ''

        if value is not None:
            text = text + attr
            text = text + '='
            text = text + str(value.year) + '-' + str(value.month) + '-' + str(value.day)
            text = text + '\n'

        return text

    def contact_text(self, contact) -> str:
        text = ''

        text = text + "\n"
        text = text + "[" + str(contact.get_id()) + "]" + "\n"
        text = text + self.attr_str_text('name', contact.get_name())
        text = text + self.emails_text(contact.get_emails())
        text = text + self.attr_date_text('birthday', contact.get_birthday())
        text = text + self.attr_str_text('firstname', contact.get_firstname())
        text = text + self.attr_str_text('lastname', contact.get_lastname())
        text = text + self.attr_str_text('country', contact.get_country())
        text = text + self.attr_str_text('state', contact.get_state())
        text = text + self.attr_str_text('zip', contact.get_zip())
        text = text + self.attr_str_text('city', contact.get_city())
        text = text + self.attr_str_text('address', contact.get_address())
        text = text + self.attr_str_text('address2', contact.get_address2())
        text = text + self.attr_str_text('worktitle', contact.get_worktitle())
        text = text + self.attr_str_text('workname', contact.get_workname())
        text = text + self.attr_str_text('workdept', contact.get_workdept())
        text = text + self.attr_str_text('workstate', contact.get_workstate())
        text = text + self.attr_str_text('workzip', contact.get_workzip())
        text = text + self.attr_str_text('workcity', contact.get_workcity())
        text = text + self.attr_str_text('workaddress', contact.get_workaddress())
        text = text + self.attr_str_text('workaddress2', contact.get_workaddress2())
        text = text + self.attr_str_text('phone', contact.get_phone())
        text = text + self.attr_str_text('workphone', contact.get_workphone())
        text = text + self.attr_str_text('mobile', contact.get_mobile())
        text = text + self.attr_str_text('fax', contact.get_fax())
        text = text + self.attr_str_text('pager', contact.get_pager())
        text = text + self.attr_str_text('nick', contact.get_nick())
        text = text + self.attr_str_text('url', contact.get_url())
        text = text + self.attr_str_text('url2', contact.get_url2())
        text = text + self.attr_str_text('anniversary', contact.get_anniversary())
        text = text + self.attr_str_text('notes', contact.get_notes())
        text = text + "\n"

        return text

    def write(self, file_out, contacts):
        header_text = self.header_text()

        file_out.write(header_text)

        for contact in contacts:
            contact_text = self.contact_text(contact)
            file_out.write(contact_text)


if __name__ == "__main__":
    counter = Counter()
    reader = Reader(counter)
    writer = Writer()

    contacts = reader.read(sys.stdin)
    writer.write(sys.stdout, contacts)


