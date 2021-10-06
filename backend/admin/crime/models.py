from django.db import models
from admin.common.models import DFrameGenerater, Reader, Printer


class CrimeCctvModel():
    generator  = DFrameGenerater()
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
        generator = self.generator
        reader = self.reader
        printer = self.printer
        generator.context = 'admin/crime/data/'
        generator.fname = 'crime_in_Seoul'
        crime_file_name = reader.new_file(generator)
        print(f'파일명:{crime_file_name}')
        crime_model = reader.csv(crime_file_name)
        printer.dframe(crime_model)
        return crime_model