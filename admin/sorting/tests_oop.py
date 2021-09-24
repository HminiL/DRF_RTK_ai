import unittest

from models_oop import Calculator, Contacts


class TestCalculator(unittest.TestCase):
    def test_calculator(self):
        instance = Calculator()
        instance.num1 = 10
        instance.num2 = 5
        print(instance.add())
        print(instance.subtract())
        print(instance.multiple())
        print(instance.divide())


class TestContact(unittest.TestCase):
   def test_contact(self):
       instance = Contacts('홍길동','010','aa@aa','seoul')
       # instance.name = '홍길동'
       # instance.phone ='010-1234-1234'
       # instance.email = 'aa@naver.com'
       # instance.address = '서울시 강남구'
       ls = []
       ls.append(instance.set_contact())
       print(ls)


if __name__ == '__main__':
    unittest.main