from dataclasses import dataclass


@dataclass
class Calculator(object):

    num1 : int
    num2 : int

    @property
    def num1(self) -> int: return self._num1
    @num1.setter
    def num1(self,num1): self._num1 = num1

    @property
    def num2(self) -> int:return self._num2
    @num2.setter
    def num2(self, num2):self._num2 = num2

    # def __init__(self, num1, num2):
    #     self.num1 = num1
    #     self.num2 = num2

    def add(self) :
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiple(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2


@dataclass
class Contacts(object):

    @property
    def name(self) -> str :return self._name
    @name.setter
    def name(self, name): self._name = name

    @property
    def phone(self) -> str: return self._phone
    @phone.setter
    def phone(self, phone):self._phone = phone

    @property
    def email(self) -> str: return self._email
    @email.setter
    def email(self,email): self._email = email

    @property
    def address(self) -> str: return self._address
    @address.setter
    def address(self, address): self._address = address

    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def to_string(self):
        return f'{self.name}, {self.phone}, {self.email}, {self.address}'

    @staticmethod
    def set_contact(name, phone, email, address) -> object:
        return Contacts(name, phone, email, address)

    @staticmethod
    def get_contact(ls):
        for i in ls:
            i.to_string()
        return ls

    @staticmethod
    def del_contact(ls ,name):
        for i, j in enumerate(ls):
            if name == j.name:
                del ls[i]
        return ls


class Grade(object):

    @property
    def kor(self) -> int: return self._kor
    @kor.setter
    def kor(self , kor): self._kor = kor

    @property
    def eng(self) -> int: return self._eng
    @eng.setter
    def eng(self, eng): self._eng = eng

    @property
    def math(self) -> int: return self._math
    @math.setter
    def math(self, math): self._math = math

    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

    def sum(self):
        return self.kor + self.eng + self.math

    def avg(self):
        return round((self.sum() / 3), 2)

    def grade(self):
        avg=self.avg()
        if avg >= 90:
            return 'A'
        elif avg >= int('80'):
            return 'B'
        elif avg >= int('70'):
            return 'C'
        elif avg >= int('60'):
            return 'D'
        else:
            return 'F'

class GradeWithName(object):

    @property
    def name(self) -> str: return self._name
    @name.setter
    def name(self, name): self._name = name

    def __init__(self, name):
        self.name = name
        self.scores = []

    def addScores(self, score):
        self.scores.append(score)

    def avg(self):
        return sum(self.scores) / len(self.scores)

    def grade(self):
        grade = Grade(self.name)
        for i in ['Korean', 'English', 'Math']:
            grade.addScores(int(input(f'{i} : ')))
        avg = self.avg()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'