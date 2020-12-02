import suds

from suds.client import Client

url = "http://60.205.206.111:805/WebServiceCC.asmx?wsdl"
client = suds.client.Client(url)

#getHealthyHeBei是webService提供的方法
result = client.service.getHealthyHeBei(18210409689)

#打印出结果
print(result)