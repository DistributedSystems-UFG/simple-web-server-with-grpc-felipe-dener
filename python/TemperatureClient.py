from __future__ import print_function
import logging

import grpc
import TemperatureService_pb2
import TemperatureService_pb2_grpc

import const

def run():
    with grpc.insecure_channel(const.IP+':'+const.PORT) as channel:
        print('services available: create, getByDate, getByLocation, listAll')
        print('type break as service to exit or type ctrl+c to interupt')
        stub = TemperatureService_pb2_grpc.TemperatureServiceStub(channel)
        while True:
            service = input('choose a service: ')
            # Query Temperature by Date
            if service.strip() == "getByDate":
                print('date format: dd-mm-yyyy')
                date = input('searching date: ')
                response = stub.GetTemperatureByDate(TemperatureService_pb2.TemperatureDate(date=date))
                print('Result of Query By Date:\n' + str(response) + '\n\n')

            # Query Temperature by Location
            if service.strip() == "getByLocation":
                location = input('searching location: ')
                response = stub.GetTemperatureByLocation(TemperatureService_pb2.TemperatureLocation(location=location))
                print('Restult of Query By Location:\n' + str(response) + '\n\n')

            # Add New Temperature
            if service.strip() == "create":
                print('date format: dd-mm-yyyy')
                date = input('date: ')
                location = input('location: ')
                temp = float(input('temperature: '))
                response = stub.CreateTemperature(TemperatureService_pb2.TemperatureData(date=date, location=location, temperature=temp))
                print('Added New Temperature ' + response.status + '\n\n')

            # List all Temperature
            if service.strip() == 'listAll':
                response = stub.ListAllTemperatures(TemperatureService_pb2.EmptyMessage())
                print('List All temperature:\n' + str(response) + '\n\n')

            if service.strip() == 'break':
                break

if __name__ == '__main__':
    logging.basicConfig()
    run()
