import numpy as np
from django.db import models
import pandas as pd
from icecream import ic
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from admin.common.models import ValueObject


class HousingService(object):
    def __init__(self):
        self.vo  = ValueObject()
        self.vo.fname  = 'admin/housing/data/housing.csv'
        self.model = self.vo.create_model()


    def housing_info(self):
        self.vo.model_info(self.model)

    def housing_hist(self):
        self.model.hist(bins=50, figsize=(20,15))
        # self.model.dframe.hist(bins=50, figsize=(20,15))
        plt.savefig('admin/housing/image/housing-hist.png')

    def split_model(self) -> []:
        train_set, test_set = train_test_split(self.model, test_size=0.2, random_state=42)
        return [train_set, test_set]

    def income_cat_hist(self):
        h = self.model
        h['income_cat'] = pd.cut(h['median_income'],
                             bins = [0.,1.5,3.0,4.5,6.,np.inf], #np.inf is NaN(Not a Number)
                             labels=[1,2,3,4,5]
                             )
        h['income_cat'].hist()
        plt.savefig('admin/housing/image/income-cat.png')

    def split_model_by_income_cat(self) -> []:
        h = self.model
        h['income_cat'] = pd.cut(h['median_income'],
                                 bins=[0., 1.5, 3.0, 4.5, 6., np.inf],  # np.inf is NaN(Not a Number)
                                 labels=[1, 2, 3, 4, 5]
                                 )
        split = StratifiedShuffleSplit(n_split=1, test=0.2, random_state=42)
        for train_idx, test_idx in split.split(h, h['income_cat']):
            temp_train_set = h.loc[train_idx]
            temp_test_set = h.loc[test_idx]
        ic(temp_test_set['income_cat'].value_counts() / len(temp_test_set))

        # 사이킷런  위 함수 밑 생성자 위는 랜덤 아래는 기준으로 나눔

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


'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 20640 entries, 0 to 20639
Data columns (total 10 columns):
 #   Column              Non-Null Count  Dtype
---  ------              --------------  -----
 0   longitude           20640 non-null  float64
 1   latitude            20640 non-null  float64
 2   housing_median_age  20640 non-null  float64
 3   total_rooms         20640 non-null  float64
 4   total_bedrooms      20433 non-null  float64
 5   population          20640 non-null  float64
 6   households          20640 non-null  float64
 7   median_income       20640 non-null  float64
 8   median_house_value  20640 non-null  float64
 9   ocean_proximity     20640 non-null  object
dtypes: float64(9), object(1)
memory usage: 1.6+ MB
'''

