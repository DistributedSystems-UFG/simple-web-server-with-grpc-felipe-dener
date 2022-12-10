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
        print ('Temperature\'s data: ' + str(response))

        # Query Temperature by Location
        response = stub.GetTemperatureByLocation(TemperatureService_pb2.TemperatureLocation(location='Sao Paulo'))
        print ('Temperature\'s data: ' + str(response))

        # Add New Temperature
        response = stub.CreateTemperature(TemperatureService_pb2.TemperatureData(date='12-03-2022', location='Rio de Janeiro', temperature=29.3))
        print ('Added New Temperature ' + response.status)

        # List all Temperature
        response = stub.ListAllTemperatures(TemperatureService_pb2.EmptyMessage())
        print ('All temperature: ' + str(response))

if __name__ == '__main__':
    logging.basicConfig()
    run()
