import unittest

from models_oop import Calculator, Contacts, Grade, GradeWithName


class TestCalculator(unittest.TestCase):
    def test_add(self):
        instance = Calculator()
        instance.num1 = 10
        instance.num2 = 5
        self.assertEqual(15, instance.add())

    def test_subtract(self):
        instance = Calculator()
        instance.num1 = 10
        instance.num2 = 5
        self.assertEqual(5, instance.subtract())

    def test_multiple(self):
        instance = Calculator()
        instance.num1 = 10
        instance.num2 = 5
        self.assertEqual(50, instance.multiple())

    def test_divide(self):
        instance = Calculator()
        instance.num1 = 10
        instance.num2 = 5
        self.assertEqual(2.0,instance.divide())

class TestContact(unittest.TestCase):
   def test_contact(self):
       ls = []
       ls.append(Contacts.set_contact('홍길동', '010', 'aa@aa', 'seoul'))
       ls = Contacts.get_contact(ls)
       print(ls[0])

   def test_get_contact(self):
       ls = []
       ls.append(Contacts.set_contact('Tom', '010-1234', 'tom@test.com', 'Seoul'))
       ls.append(Contacts.set_contact('Jane', '010-3334', 'jane@test.com', 'Incheon'))
       ls.append(Contacts.set_contact('Kim', '010-7734', 'kim@test.com', 'Busan'))
       ls = Contacts.get_contact(ls)
       self.assertEqual(ls[0].name, 'Tom')


   def test_del_contact(self):
       ls = []
       ls.append(Contacts.set_contact('Tom', '010-1234', 'tom@test.com', 'Seoul'))
       ls.append(Contacts.set_contact('Jane', '010-3334', 'jane@test.com', 'Incheon'))
       ls.append(Contacts.set_contact('Kim', '010-7734', 'kim@test.com', 'Busan'))
       ls = Contacts.del_contact(ls, 'Tom')
       print([i.to_string() for i in ls])
       self.assertEqual(len(ls),2)

class TestGrade(unittest.TestCase):
    def test_grade(self):
        instance = Grade('홍길동',100,80,90)
        # print(instance.sum())
        self.assertEqual(270,instance.sum())
        self.assertEqual(90,instance.avg())
        self.assertEqual('A',instance.grade())

class TestGradeWithName(unittest.TestCase):
    def test_grade_with_name(self):
        instance = Grade('홍길동',100,80,90)
        self.assertEqual('A',instance.grade())

if __name__ == '__main__':
    unittest.main