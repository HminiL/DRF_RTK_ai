import pandas as pd
from django.db import models
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

    def create_crime_model(self):
        vo = self.vo
        reader = self.reader
        printer = self.printer
        vo.context = 'admin/crime/data/'
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
        #crime.to_csv(self.vo.context + 'new_data/police_position.csv')

    def create_cctv_model(self):
        vo = self.vo
        reader = self.reader
        printer = self.printer
        vo.context = 'admin/crime/data/'
        vo.fname = 'CCTV_in_Seoul'
        cctv_file_name = reader.new_file(vo)
        cctv_model = reader.csv(cctv_file_name)
        cctv_model.rename(columns={'기관명': '구별'}, inplace=True)
        # cctv_model.rename(columns={cctv_model.columns[0]: '구별'}, inplace=True)
        cctv_model.to_csv(vo.context + 'new_data/cctv_in_seoul.csv')
        printer.dframe(cctv_model)
        return cctv_model


    def create_population_model(self):
        vo = self.vo
        reader = self.reader
        printer = self.printer
        vo.context = 'admin/crime/data/'
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
        # population.drop([26],inplace=True) 마지막 줄에 있던 공백 제거
        printer.dframe(population)
        return population

    def merge_cctv_pop(self):
        cctv = self.create_cctv_model()
        pop = self.create_population_model()
        cctv_pop = pd.merge(left=cctv, right=pop, on='구별', how='left')
        cctv_pop.to_csv(self.vo.context + 'new_data/cctv_pop.csv')
        return cctv_pop