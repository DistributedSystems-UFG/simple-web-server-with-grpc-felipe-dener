from __future__ import print_function
import logging

import grpc
import TemperatureService_pb2
import TemperatureService_pb2_grpc
import datetime
import random
import const

def get_random_date():
    start_date = datetime.datetime(day=1, month=1, year=2022)
    end_date = datetime.datetime(day=31, month=12, year=2022)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = datetime.datetime.strftime((start_date + datetime.timedelta(days=random_number_of_days)), '%d-%m-%Y')

    return random_date

def rand_temperature():
    return random.uniform(15.0, 35.0)

def run():
    with grpc.insecure_channel(const.IP+':'+const.PORT) as channel:
        stub = TemperatureService_pb2_grpc.TemperatureServiceStub(channel)
        for i in range(15):
            response = stub.CreateTemperature(TemperatureService_pb2.TemperatureData(
                date=get_random_date(), location='goiania', temperature=rand_temperature))
            print('Added New Temperature ' + response.status + '\n\n')


if __name__ == '__main__':
    logging.basicConfig()
    run()
