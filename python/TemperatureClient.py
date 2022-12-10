from __future__ import print_function
import logging

import grpc
import TemperatureService_pb2
import TemperatureService_pb2_grpc

import const

def run():
    with grpc.insecure_channel(const.IP+':'+const.PORT) as channel:
        stub = TemperatureService_pb2_grpc.TemperatureServiceStub(channel)

        # Query Temperature by Date
        response = stub.GetTemperatureByDate(TemperatureService_pb2.TemperatureDate(date='25-02-2022'))
        print ('Result of Query By Date:\n' + str(response) + '\n\n')

        # Query Temperature by Location
        response = stub.GetTemperatureByLocation(TemperatureService_pb2.TemperatureLocation(location='Sao Paulo'))
        print ('Restult of Query By Location:\n' + str(response) + '\n\n')

        # Add New Temperature
        response = stub.CreateTemperature(TemperatureService_pb2.TemperatureData(date='12-03-2022', location='Rio de Janeiro', temperature=29.3))
        print ('Added New Temperature ' + response.status + '\n\n')

        # List all Temperature
        response = stub.ListAllTemperatures(TemperatureService_pb2.EmptyMessage())
        print ('List All temperature:\n' + str(response) + '\n\n')

if __name__ == '__main__':
    logging.basicConfig()
    run()
