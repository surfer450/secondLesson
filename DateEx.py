from __future__ import annotations
from typing import List, Tuple

JANUARY = 31
DAY1 = 1


class ValidationError(Exception):
    def __init__(self, error_message):
        self.error_message = error_message

    def __str__(self):
        return self.error_message


class Date:
    def __init__(self, date: str):
        """
        constructor
        :param date: date as string to create as date object
        """
        try:
            date = date.split('.')
            Date.validate_date(int(date[0]), int(date[1]), int(date[2]))
            self.day = int(date[0])
            self.month = int(date[1])
            self.year = int(date[2])

        except ValidationError as ve:
            print(ve.__str__() + "\nyou had a ValidationError. couldn't build the object!")
            exit(0)

    @staticmethod
    def validate_date(day: int, month: int, year: int):
        """
          this function checks if all input for creating new date is valid(make sense)
          :param day: day of the date
          :param month: month of the date
          :param year: year of the date
          :return: None
          """

        if not (day > 0 and month > 0 and year >= 0):
            raise ValidationError("cant enter negative date!")

        if not day <= 31:
            raise ValidationError("too many days!")

        if not month <= 12:
            raise ValidationError("too many months!")

    def set_day(self, day: int):
        """
        set day of date object
        :param day: new day
        :return: None
        """
        self.day = day

    def set_month(self, month: int):
        """
        set month of date object
        :param month: new month
        :return: None
        """
        self.month = month

    def set_year(self, year: int):
        """
        set year of date object
        :param year: new year
        :return: None
        """
        self.year = year

    def get_day(self) -> int:
        """
        get day of date object
        :return: the day of the current date object
        """
        return self.day

    def get_month(self) -> int:
        """
        get month of date object
        :return: the month of the current date object
        """
        return self.month

    def get_year(self) -> int:
        """
        get year of date object
        :return: the year of the current date object
        """
        return self.year

    def get_bigger_date(self, other: Date) -> Date:
        """
        this function finds the bigger date between two
        :param other: one of the dates to compare
        :return: the bigger date
        """
        if self.__ge__(other):
            return self
        return other

    def get_smaller_date(self, other: Date) -> Date:
        """
        this function finds the smaller date between two
        :param other: one of the dates to compare
        :return: the smaller date
        """
        if self.__le__(other):
            return self
        return other

    def get_days_per_month(self) -> List[int]:
        """
        this function calculate amount of days par month(including leap years)
        :return: list of amount of days par month
        """
        days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.is_leap_year():
            days_per_month[1] = 29
        return days_per_month

    def is_leap_year(self) -> bool:
        """
        this function finds if date object year value is a leap year
        :return: true if self year is a leap year
        """
        return (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)

    def find_differance(self, other: Date | int) -> Tuple[Date, int]:
        """
        function that helps for __add__. it finds the differance between a date and a date or a date and an int
        :param other: date object or int
        :return: the date to add to, and amount to add to
        """

        if type(other) is Date:
            smaller_date = self.get_smaller_date(other)
            bigger_date = self.get_bigger_date(other)
            difference_in_days = smaller_date.__sub__(Date.get_smallest_date()) + JANUARY
            date_added_to = bigger_date
        else:
            difference_in_days = other

            date_added_to = Date(self.__str__())
        return date_added_to, difference_in_days

    @staticmethod
    def get_smallest_date() -> Date:
        """
        this function find the smallest from the dates
        :return: date object that is the smallest
        """
        return Date("01.01.0")

    def __str__(self) -> str:
        """
        this function turns the date object to string
        :return: the date object as string
        """
        full_date = str(self.day) + "." + str(self.month) + "." + str(self.year)
        return full_date

    def __gt__(self, other: Date) -> bool:
        """
        this function finds if date self is bigger than date other
        :param other: a date object
        :return: true if self > other
        """
        return (self.year > other.year) or (self.year == other.year and self.month > other.month) or (
                self.year == other.year and self.month == other.month and self.day > other.day)

    def __eq__(self, other: Date) -> bool:
        """
        this function finds if date self is equals to date other
        :param other: a date object
        :return: true if self == other
        """
        return self.year == other.year and self.month == other.month and self.day == other.day

    def __lt__(self, other: Date) -> bool:
        """
        this function finds if date self is smaller than date other
        :param other: a date object
        :return: true if self < other
        """
        return self.__gt__(other) is False and self.__eq__(other) is False

    def __ge__(self, other: Date) -> bool:
        """
        this function finds if date self is bigger or equals to date other
        :param other: a date object
        :return: true if self >= other
        """
        return self.__gt__(other) is True or self.__eq__(other) is True

    def __le__(self, other: Date) -> bool:
        """
        this function finds if date self is smaller or equals to date other
        :param other: a date object
        :return: true if self <= other
        """
        return self.__lt__(other) is True or self.__eq__(other) is True

    def __sub__(self, other: Date) -> int:
        """
        this function find the amount of days between two dates
        :param other: a date object
        :return: amount of days between two dates
        """
        smaller_date = Date(self.get_smaller_date(other).__str__())
        bigger_date = Date(self.get_bigger_date(other).__str__())
        days_per_month = bigger_date.get_days_per_month()

        count_days = 0
        while not bigger_date.__eq__(smaller_date) and not bigger_date.__le__(Date.get_smallest_date()):
            bigger_date.day -= 1
            count_days += 1

            if bigger_date.day < 1:
                bigger_date.month -= 1

                if bigger_date.month < 1:
                    bigger_date.year -= 1
                    bigger_date.month = 12
                    days_per_month = bigger_date.get_days_per_month()

                bigger_date.day = days_per_month[bigger_date.month - 1]
        return count_days

    def __add__(self, other: Date | int) -> Date:
        """
        this function add days to a date or date to a date
        :param other: int object or date object
        :return: new date after addition
        """

        date_added_to, difference_in_days = self.find_differance(other)
        days_per_month = date_added_to.get_days_per_month()

        while difference_in_days > 0:
            date_added_to.day += 1
            difference_in_days -= 1

            if date_added_to.day > days_per_month[date_added_to.month - 1]:
                date_added_to.day = 1
                date_added_to.month += 1

            if date_added_to.month > 12:
                date_added_to.month = 1
                date_added_to.year += 1
                days_per_month = date_added_to.get_days_per_month()

        return date_added_to


def main():
    print(Date("1.2.2020") + Date("1.3.2020"))
    print(Date("1.1.2020") + 5)
    print(Date("1.1.2020") - Date("2.2.2020"))


if __name__ == "__main__":
    main()
