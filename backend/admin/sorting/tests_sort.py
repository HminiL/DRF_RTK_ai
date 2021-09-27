from django.test import TestCase
import unittest
# Create your tests here.
# import sys
# sys.path.append('admin/sorting')
from model_sort import Sorting


class TestSorting(unittest.TestCase):
   def test_bubble_sort(self):
       instance = Sorting()
       instance.random_arr = [9,8,7,6,5,4,3,2,1]
       arr = instance.bubble_sort()
       self.assertEqual([1,2,3,4,5,6,7,8,9],arr)

   def test_merge_sort(self):
       arr = [9,8,7,6,5,4,3,2,1]
       arr = Sorting.merge_sort(arr)
       self.assertEqual([1,2,3,4,5,6,7,8,9],arr)

   def test_quick_sort(self):
       arr = [9,8,7,6,5,4,3,2,1]
       arr = Sorting.quick_sort(arr)
       self.assertEqual([1,2,3,4,5,6,7,8,9],arr)

if __name__ == '__main__':
    unittest.main()