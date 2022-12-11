from concurrent import futures
import logging

import grpc
import TemperatureService_pb2
import TemperatureService_pb2_grpc

tempDB=[
 {
 'date': '25-02-2022',
 'location':'Goias',
 'temperature':27.6
 },
 {
 'date': '26-02-2022',
 'location':'Sao Paulo',
 'temperature':24.5
 }
 ]

class TemperatureServer(TemperatureService_pb2_grpc.TemperatureServiceServicer):

  def CreateTemperature(self, request, context):
    dat = {
    'date':request.date,
    'location':request.location,
    'temperature':request.temperature
    }
    tempDB.append(dat)
    return TemperatureService_pb2.StatusReply(status='OK')

  def GetTemperatureByDate(self, request, context):
    list = TemperatureService_pb2.TemperatureDataList()
    for temp in tempDB:
      if temp['date'] == request.date:
        temp_data = TemperatureService_pb2.TemperatureData(date=temp['date'], location=temp['location'], temperature=temp['temperature'])
        list.temperature_data.append(temp_data)
    return list

  def GetTemperatureByLocation(self, request, context):
    list = TemperatureService_pb2.TemperatureDataList()
    for temp in tempDB:
      if temp['location'] == request.location:
        temp_data = TemperatureService_pb2.TemperatureData(date=temp['date'], location=temp['location'], temperature=temp['temperature'])
        list.temperature_data.append(temp_data)
    return list
    
  def ListAllTemperatures(self, request, context):
    list = TemperatureService_pb2.TemperatureDataList()
    for temp in tempDB:
      temp_data = TemperatureService_pb2.TemperatureData(date=temp['date'], location=temp['location'], temperature=temp['temperature']) 
      list.temperature_data.append(temp_data)
    return list

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    TemperatureService_pb2_grpc.add_TemperatureServiceServicer_to_server(TemperatureServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()

       
