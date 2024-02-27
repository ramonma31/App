from __future__ import annotations
import flet as f
from datetime import datetime as dt


class ModelBirthDate(object):

    @classmethod
    def _parse_birth_date(cls, birth_date: str) -> ModelBirthDate:
        return ModelBirthDate(
            day=int(birth_date[0:2]),
            month=int(birth_date[3:5]),
            year=int(birth_date[6:])
        )

    def __init__(self, day, month, year) -> None:
        self._day = day
        self._month = month
        self._year = year

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, value):
        self._day = value if value > 0 <= 31 else self._day

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value):
        self._month = value if value > 0 <= 12 else self._month

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value if value > 1000 <= dt.today().year else self._year


class ModelNumberPhone(object):

    @classmethod
    def _parse_number(cls, number: str) -> ModelNumberPhone:
        return ModelNumberPhone(
            number=int(number[4:]),
            cod_ddd=int(number[2:4]),
            cod_country=int(number[0:2]),
        )

    def __init__(self, number, cod_ddd, cod_country) -> None:
        self._cod_country = cod_country
        self._cod_ddd = cod_ddd
        self._number = number
        self._phone_number = f"{self.cod_country}{self.cod_ddd}{self.number}"

    @property
    def phone_number(self):
        return self._phone_number

    @property
    def cod_country(self):
        return self._cod_country

    @cod_country.setter
    def cod_country(self, value):
        self._cod_country = value

    @property
    def cod_ddd(self):
        return self._cod_ddd

    @cod_ddd.setter
    def cod_ddd(self, value):
        self._cod_ddd = value

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value


class User:
    def __init__(
        self,
        first_name: str,
        last_name: str,
        phone: str | ModelNumberPhone,
        birth_date: str | ModelBirthDate,
        e_mail: str,
        password: str,
        page: f.Page
    ) -> None:
        self._password = password
        self._e_mail = e_mail
        self._birth_date = ModelBirthDate._parse_birth_date(birth_date)
        self._phone = ModelNumberPhone._parse_number(phone)
        self._name = f"{first_name} {last_name}"
        self._first_name = first_name
        self._last_name = last_name
        self._page = page

    @property
    def name(self):
        return self._name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @property
    def e_mail(self):
        return self._e_mail

    @e_mail.setter
    def e_mail(self, value):
        self._e_mail = value

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value):
        self._birth_date = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
