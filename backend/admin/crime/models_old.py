import pandas as pd
from django.db import models
from icecream import ic

from admin.common.models import ValueObject, Reader, Printer


class CrimeCctvModel():
    vo  = ValueObject()
    reader = Reader()
    printer = Printer()

    def __init__(self):
        '''
        Raw Data 의 feature를 가져온다.
        살인 발생,살인 검거,강도 발생,강도 검거,강간 발생,강간 검거,절도 발생,절도 검거,폭력 발생,폭력 검거
        '''
        self.crime_columns = ['살인 발생', '강도 발생','강간 발생', '절도 발생', '폭력 발생'] # Nominal (발생건수)
        self.arrest_columns = ['살인 검거', '강도 검거', '강간 검거', '절도 검거', '폭력 검거'] # Nominal (검거건수)
        self.arrest_crime_rate_columns = ['살인 검거율', '강도 검거율', '강간 검거율', '절도 검거율', '폭력 검거율'] # Nominal
        self.vo.context = 'admin/crime/data/'

    def create_crime_model(self):
        vo = self.vo
        reader = self.reader
        printer = self.printer
        vo.fname = 'crime_in_Seoul'
        crime_file_name = reader.new_file(vo)
        print(f'파일명:{crime_file_name}')
        crime_model = reader.csv(crime_file_name)
        printer.dframe(crime_model)
        '''
                RangeIndex: 31 entries, 0 to 30
        Data columns (total 11 columns):
         #   Column  Non-Null Count  Dtype
        ---  ------  --------------  -----
         0   관서명     31 non-null     object
         1   살인 발생   31 non-null     int64
         2   살인 검거   31 non-null     int64
         3   강도 발생   31 non-null     int64
         4   강도 검거   31 non-null     int64
         5   강간 발생   31 non-null     int64
         6   강간 검거   31 non-null     int64
         7   절도 발생   31 non-null     int64
         8   절도 검거   31 non-null     int64
         9   폭력 발생   31 non-null     int64
         10  폭력 검거   31 non-null     int64
        '''
        return crime_model

    def create_police_position(self):
        crime = self.create_crime_model()
        reader = self.reader
        station_names = []
        # for name in crime['관서명']:
        #     station_names.append('서울'+str(name[:-1]+'경찰서'))
        [station_names.append('서울'+str(name[:-1]+'경찰서')) for name in crime['관서명']]
        station_addrs = []
        station_lats = []
        station_lngs = []
        gmaps = reader.gmaps()
        for name in station_names:
            temp = gmaps.geocode(name, language='ko')
            station_addrs.append(temp[0].get('formatted_address'))
            temp_loc = temp[0].get('geometry')
            station_lats.append(temp_loc['location']['lat'])
            station_lngs.append(temp_loc['location']['lng'])
            print(f'name : {temp[0].get("formatted_address")}')
        gu_names = []
        for name in station_addrs:
            temp = name.split()
            gu_name = [gu for gu in temp if gu[-1] == '구'][0]
            gu_names.append(gu_name)
        crime['구별'] = gu_names
        # 구와 경찰서의 위치가 다른 경우 수작업
        # crime.loc[crime['관서명'] == '혜화서', ['구별']] = '종로구'
        # crime.loc[crime['관서명'] == '서부서', ['구별']] = '은평구'
        # crime.loc[crime['관서명'] == '강서서', ['구별']] = '양천구'
        # crime.loc[crime['관서명'] == '종암서', ['구별']] = '성북구'
        # crime.loc[crime['관서명'] == '방배서', ['구별']] = '서초구'
        # crime.loc[crime['관서명'] == '수서서', ['구별']] = '강남구'
        # 금천경찰서는 관악구에 있어서 금천구로 변경
        print('==================================================')
        print(f"샘플 중 혜화서 정보 : {crime[crime['관서명'] == '혜화서']}")
        print(f"샘플 중 금천서 정보 : {crime[crime['관서명'] == '금천서']}")
        crime.to_csv(self.vo.context + 'new_data/police_position.csv')

    def create_cctv_model(self) -> object:
        vo = self.vo
        reader = self.reader
        printer = self.printer
        vo.fname = 'CCTV_in_Seoul'
        cctv_file_name = reader.new_file(vo)
        cctv_model = reader.csv(cctv_file_name)
        cctv_model.rename(columns={'기관명': '구별'}, inplace=True)
        cctv_model.rename(columns={cctv_model.columns[0]: '구별'}, inplace=True)
        cctv_model.to_csv(vo.context + 'new_data/cctv_in_seoul.csv')
        printer.dframe(cctv_model)
        return cctv_model


    def create_population_model(self) -> object:
        vo = self.vo
        reader = self.reader
        printer = self.printer
        vo.fname = 'population_in_Seoul'
        population_file_name = reader.new_file(vo)
        population = reader.xls(population_file_name, 2, ('B,D,G,J,N') )
        # header와 columns의 원하는 열을 위치로 호출한다. list로 호출도 가능
        # 예) usecols : ('B,D,G,J,N')혹은 [2,4,7,10,14] 가능
        '''
        print(population.columns)
        Index(['자치구', '계', '계.1', '계.2', '65세이상고령자'], dtype='object')
        따라서 하나만 변경할때는 .rename을 이용하여 columns={'기관명': '구별'}을 사용
        모두 변경할때는 .columns = ['구별','인구수','한국인','외국인','고령자']를 이용하여 모두 변경
        '''
        population.columns = ['구별','인구수','한국인','외국인','고령자']
        population.to_csv(vo.context + 'new_data/new_population.csv')
        population.drop([26],inplace=True) #마지막 줄에 있던 공백 제거
        printer.dframe(population)
        return population

    def merge_cctv_pop(self):
        printer = self.printer
        cctv = self.create_cctv_model()
        pop = self.create_population_model()
        cctv_pop = pd.merge(cctv,pop) #(left=cctv, right=pop, on='구별', how='left')
        '''
        r이 -1.0과 -0.7 사이이면, 강한 음적 선형관계,
        r이 -0.7과 -0.3 사이이면, 뚜렷한 음적 선형관계,
        r이 -0.3과 -0.1 사이이면, 약한 음적 선형관계,
        r이 -0.1과 +0.1 사이이면, 거의 무시될 수 있는 선형관계,
        r이 +0.1과 +0.3 사이이면, 약한 양적 선형관계,
        r이 +0.3과 +0.7 사이이면, 뚜렷한 양적 선형관계,
        r이 +0.7과 +1.0 사이이면, 강한 양적 선형관계
        '''
        ic(cctv_pop.corr())
        '''
                       CCTV 소계  2013년도 이전  2014년    2015년     2016년    인구수     한국인     외국인     고령자
          소계           1.000000   0.862756  0.450062  0.624402  0.593398  0.306342  0.304287 -0.023786  0.255196
          2013년도 이전   0.862756   1.000000  0.121888  0.257748  0.355482  0.168177  0.163142  0.048973  0.105379
          2014년         0.450062   0.121888  1.000000  0.312842  0.415387  0.027040  0.025005  0.027325  0.010233
          2015년         0.624402   0.257748  0.312842  1.000000  0.513767  0.368912  0.363796  0.013301  0.372789
          2016년         0.593398   0.355482  0.415387  0.513767  1.000000  0.144959  0.145966 -0.042688  0.065784
          인구수          0.306342   0.168177  0.027040  0.368912  0.144959  1.000000  0.998061 -0.153371  0.932667
          한국인          0.304287   0.163142  0.025005  0.363796  0.145966  0.998061  1.000000 -0.214576  0.931636
          외국인         -0.023786   0.048973  0.027325  0.013301 -0.042688 -0.153371 -0.214576  1.000000 -0.155381
          고령자          0.255196   0.105379  0.010233  0.372789  0.065784  0.932667  0.931636 -0.155381  1.000000

        '''
        # printer.dframe(cctv_pop)
        cctv_pop.to_csv(self.vo.context + 'new_data/cctv_pop.csv')

    def sum_crime(self):
        crime = pd.read_csv(self.vo.context + 'new_data/police_position.csv')
        crime['발생'] = crime.loc[:,self.crime_columns].sum(axis=1)
        crime['검거'] = crime.loc[:,self.arrest_columns].sum(axis=1)
        grouped = crime.groupby('구별')
        crime_filter = grouped['발생','검거'].sum()
        self.printer.dframe(crime_filter)
        crime_filter.to_csv(self.vo.context+'new_data/new_crime_arrest.csv')

    def merge_cctv_crime(self):
        cctv = self.create_cctv_model()
        # vo = self.vo
        # reader = self.reader
        # vo.fname = 'new_data/new_crime_arrest'
        # reader.new_file(vo)
        # crime = reader.csv(vo)
        # self.printer.dframe(crime)
        crime = pd.read_csv('admin/crime/data/new_data/new_crime_arrest.csv', encoding='UTF-8', thousands=',')
        cctv_crime = pd.merge(cctv, crime)
        ic(cctv_crime.corr())
        cctv_crime.to_csv(self.vo.context + 'new_data/cctv_crime.csv')
        '''
                      소계     2013년도 이전  2014년    2015년    2016년     발생       검거
       소계           1.000000   0.862608  0.484229  0.625006  0.595623  0.474269  0.520321
       2013년도 이전   0.862608   1.000000  0.165281  0.256443  0.314722  0.450751  0.514952
       2014년         0.484229   0.165281  1.000000  0.325710  0.526610  0.241809  0.203891
       2015년         0.625006   0.256443  0.325710  1.000000  0.536419  0.163454  0.157643
       2016년         0.595623   0.314722  0.526610  0.536419  1.000000  0.449323  0.438884
       발생           0.474269   0.450751  0.241809  0.163454  0.449323  1.000000  0.979473
       검거           0.520321   0.514952  0.203891  0.157643  0.438884  0.979473  1.000000
        '''


'''
vo = self.vo
reader = self.reader
printer = self.printer
vo.fname = 'population_in_Seoul'
population_file_name = reader.new_file(vo)
'''


