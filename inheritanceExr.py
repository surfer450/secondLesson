from __future__ import annotations
from typing import List


class ValidationError(Exception):
    def __init__(self, error_message):
        self.error_message = error_message

    def __str__(self):
        return self.error_message


class Person:
    def __init__(self, first_name: str, last_name: str, age: int):
        """
        constructor
        :param first_name: first name of a person
        :param last_name: last name of a person
        :param age: age of a person
        """
        try:
            Person.validate_person(first_name, last_name, age)
            self.first_name = first_name
            self.last_name = last_name
            self.age = age

        except ValidationError as ve:
            print(ve.__str__() + "\nyou had a ValidationError. couldn't build the object!")
            exit(0)

    @staticmethod
    def validate_person(first_name: str, last_name: str, age: int):
        """
        this function checks if all input for creating new person is valid(make sense)
        :param first_name: first name of a person
        :param last_name: last name of a person
        :param age: age of a person
        :return: None
        """

        if not first_name.isalpha():
            raise ValidationError("first name contains odd signs!")

        if not Person.is_string_alphabetic(last_name):
            raise ValidationError("last name contains odd signs or have more than 3 words!")

        if not len(first_name) <= 30:
            raise ValidationError("first name was too long! (above 30)!")

        if not len(last_name) <= 30:
            raise ValidationError("last name was too long! (above 30)!")

        if not 0 < age < 150:
            raise ValidationError("age cant be negative, zero or too high!")

    @staticmethod
    def is_string_alphabetic(string: str) -> bool:
        """
        function find if string letters are alphabetic, and have max 3 spaces (for last names with more than one word)
        :param string: string to check
        :return: True if string alphabetic with max 3 spaces, False otherwise
        """

        string_list = string.split()
        count = 0
        for word in string_list:
            if not word.isalpha():
                return False
            count += 1

        if count > 3:
            return False

        return True

    def set_first_name(self, first_name: str):
        """
        set first name of person object
        :param first_name: new first name
        :return: None
        """
        self.first_name = first_name

    def set_last_name(self, last_name: str):
        """
        set last name of person object
        :param last_name: new last name
        :return: None
        """
        self.last_name = last_name

    def set_age(self, age: int):
        """
        set age of person object
        :param age: new age
        :return: None
        """
        self.age = age

    def get_first_name(self) -> str:
        """
        get first name of person object
        :return: the first name of the current person object
        """
        return self.first_name

    def get_last_name(self) -> str:
        """
        get last name of person object
        :return: the last name of the current person object
        """
        return self.last_name

    def get_age(self) -> int:
        """
        get age of person object
        :return: the age of the current person object
        """
        return self.age

    def __str__(self) -> str:
        """
        this function turn the person object into string description
        :return: string that describe the person
        """
        return "first name: " + self.first_name + ", last name: " + self.last_name + ", age: " + str(self.age)


class Talker(Person):
    def __init__(self, first_name: str, last_name: str, age: int):
        """
        constructor
        :param first_name: first name of a person
        :param last_name: last name of a person
        :param age: age of a person
        """

        Person.__init__(self, first_name, last_name, age)

    @staticmethod
    def talk(text: str):
        """
        this function gets a text and print it
        :param text: text to print
        :return: None
        """
        print(text)

    @staticmethod
    def make_them_talk(talker_list: List[Talker], say_what: str):
        """
        this function make every talker object in talker_list that his age is above 10 print the say_what string
        :param talker_list: list of talke object
        :param say_what: string to print
        :return: None
        """
        for talker in talker_list:
            if talker.get_age() > 10:
                print(talker.get_first_name() + " " + talker.get_last_name() + ": ", end="")
                talker.talk(say_what)


class HappyTalker(Talker):
    def __init__(self, first_name: str, last_name: str, age: int):
        """
        constructor
        :param first_name: first name of a person
        :param last_name: last name of a person
        :param age: age of a person
        """

        Talker.__init__(self, first_name, last_name, age)

    @staticmethod
    def talk(text: str):
        """
        this function gets a text and print it with !!! in the end
        :param text: text to print
        :return: None
        """

        Talker.talk(text + "!!!")


class SlowTalker(Talker):
    def __init__(self, first_name: str, last_name: str, age: int):
        """
        constructor
        :param first_name: first name of a person
        :param last_name: last name of a person
        :param age: age of a person
        """

        Talker.__init__(self, first_name, last_name, age)

    @staticmethod
    def talk(text: str):
        """
        this function gets a text and print it with space between characters
        :param text: text to print
        :return: None
        """
        new_text = ""
        for char in text:
            new_text = new_text + char + " "

        Talker.talk(new_text)


class StutterTalker(Talker):
    def __init__(self, first_name: str, last_name: str, age: int):
        """
        constructor
        :param first_name: first name of a person
        :param last_name: last name of a person
        :param age: age of a person
        """

        Talker.__init__(self, first_name, last_name, age)

    @staticmethod
    def talk(text: str):
        """
        this function gets a text and print it with every word first character appearing 3 times
        :param text: text to print
        :return: None
        """

        text_list = text.split()
        new_text = ""
        for word in text_list:
            new_text = new_text + 2 * word[0] + word + " "

        Talker.talk(new_text)


def main():
    Talker.make_them_talk([StutterTalker("sagy", "bar joseph", 9), SlowTalker("ofek", "bar joseph", 18),
                           HappyTalker("lihi", "bar joseph", 18)], "I love cookies")


if __name__ == "__main__":
    main()
