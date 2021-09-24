from dataclasses import dataclass


@dataclass
class Calculator(object):

    num1 = int
    num2 = int

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
    # name = str
    # phone = str
    # email = str
    # address = str
    #
    #
    # @property
    # def name(self) -> str :return self._name
    # @name.setter
    # def name(self, name): self._name = name
    #
    # @property
    # def phone(self) -> str: return self._phone
    # @phone.setter
    # def phone(self, phone):self._phone = phone
    #
    # @property
    # def email(self) -> str: return self._email
    # @email.setter
    # def email(self,email): self._email = email
    #
    # @property
    # def address(self) -> str: return self._address
    # @address.setter
    # def address(self, address): self._address = address

    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def to_string(self):
        print(f'{self.name}, {self.phone}, {self.email}, {self.address}')

    def set_contact(self) -> object:
        return Contacts(self.name, self.phone, self.email, self.address)

    def get_contact(self):
        ls = self.set_contact()
        for i in ls:
            i.to_string()

    def del_contact(self, name):
        ls = self.set_contact()
        for i, j in enumerate(ls):
            if name == j.name:
                del ls[i]
