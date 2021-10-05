import numpy as np
from django.db import models
import pandas as pd
from icecream import ic
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

from admin.common.models import Dataset


class HousingService(object):

    dataset = Dataset()

    def new_model(self) -> object :
        return pd.read_csv(f'admin/housing/data/housing.csv')

    def split_model(self) -> []:
        train_set, test_set = train_test_split(self.new_model(), test_size=0.2, random_state=42)
        return [train_set, test_set]

    def income_cat_hist(self):
        h = self.new_model()
        h['income_cat'] = pd.cut(h['median_income'],
                                 bins = [0.,1.5,3.0,4.5,6.,np.inf], #np.inf is NaN(Not a Number)
                                 labels=[1,2,3,4,5]
                                 )
        h['income_cat'].hist()
        plt.savefig('admin/housing/image/income-cat.png')

    def split_model_by_income_cat(self) -> []:
        h = self.new_model()
        split = StratifiedShuffleSplit(n_split=1, test=0.2, random_state=42)
        for train_idx, test_idx in split.split(h, h['income_cat']):
            temp_train_set = h.loc[train_idx]
            temp_test_set = h.loc[test_idx]
        ic(temp_test_set['income_cat'].value_counts() / len(temp_test_set))


#  위 함수 밑 생성자 위는 랜덤 아래는 기준으로 나눔

if __name__ == '__main__':
    h = HousingService()
    ic(h.new_model())


class Housing(models.Model):

    # use_in_migrations = True
    id = models.AutoField(primary_key=True)
    longitude = models.FloatField()
    latitude = models.FloatField()
    housing_median_age = models.FloatField()
    total_rooms = models.FloatField()
    total_bedrooms = models.FloatField()
    population = models.FloatField()
    households = models.FloatField()
    median_income = models.FloatField()
    median_house_value = models.FloatField()
    ocean_proximity = models.TextField()

    class Meta:

        db_table = "housing"

    def __str__(self):

        return f'[{self.pk}] : {self.id}'

