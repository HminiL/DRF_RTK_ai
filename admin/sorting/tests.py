from django.test import TestCase
import unittest
# Create your tests here.
import sys
sys.path.append('admin/sorting')
from models import MySum

class TestMySum(unittest.TestCase):
    def test_one_to_ten_sum_1(self):
        instance = MySum()
        instance.start_num = 1
        instance.end_num = 11
        res = instance.one_to_ten_sum_2()
        print(f'My Expected Value is {res}')
        self.assertEqual(res, 55)

if __name__ == '__main__':
    unittest.main()