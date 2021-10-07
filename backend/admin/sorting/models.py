from dataclasses import dataclass

# from django.db import models
# Create your models here.




@dataclass
class MySum(object):

    start_number : int
    end_number : int

    @property
    def start_number(self) -> int: return self._start_number

    @start_number.setter
    def start_number(self, start_number): self._start_number = start_number

    @property
    def end_number(self) -> int: return self._end_number

    @end_number.setter
    def end_number(self, end_number): self._end_number = end_number

    def one_to_ten_sum_1(self):
        sum = 0
        for i in range(self.start_number, self.end_number):
            sum += i
        return sum

    def one_to_ten_sum_2(self):
        return sum(i for i in range(self.start_number, self.end_number))

    def one_to_ten_sum_3(self):
        return sum(range(self.start_number, self.end_number))
