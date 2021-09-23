import dataclasses
from builtins import object

from django.db import models

# Create your models here.

class MergeSort(object):
    pass

class QuickSort(object):
    pass

@dataclasses
class MySum(object):
    start_num = 0
    end_num = 0

    @property
    def start_number(self) -> int:return  self._start_number


    @property
    def start_number(self) -> int:return  self._start_number


    def one_to_ten_sum_1(start_num, end_num):
        sum = 0
        for i in range(start_num, end_num):
            sum += i
        print(sum)

    def one_to_ten_sum_2(start_num, end_num):
        print(sum(i for i in range(start_num, end_num)))

    def one_to_ten_sum_3(start_num, end_num):
        print(sum(range(start_num, end_num)))