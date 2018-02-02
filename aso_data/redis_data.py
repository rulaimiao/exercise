import redis
import pymysql

r = redis.Redis(host='127.0.0.1',port=6379,db=0)

config = {
          'host':'47.96.178.155',
          'port':3306,
          'user':'root',
          'password':'Aso123456',
          'db':'asodatabase',
          'charset':'utf8mb4',
          'cursorclass':pymysql.cursors.DictCursor,
          }

connection = pymysql.connect(**config)

pycursor = connection.cursor()

pycursor.execute('select imei from aso_phone_data ')
while True:
    data_list = pycursor.fetchmany(size=100)
    print(data_list)
    if not data_list:
        break
    for data in data_list:
        r.set(data['imei'], 1)
    # print(data_list)
    