import requests
import redis
import pymysql
import logging
import json
import time

fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'
log_dict = {
    "filename" : 'data.log',
    "filemode" : 'a',
    "level" :logging.INFO,
    'datefmt' : '%Y-%m-%d %H:%M:%S'
}
logging.basicConfig(**log_dict)

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
insert_sql = 'INSERT INTO `aso_phone_data` (`procmeminfo`, `phoneimsi`, `vivoid`, `locallanguage`, `osversion`, `carrieroperator`, `deviceid`, `androidid`, `vivoversion`, `cupinfo`, `devicerelease`, `arm2`, `devicebrand`, `sdkint`, `arm`, `osversionoppo`, `phonenum`, `idproduct`, `diskspace`, `serialno`, `productprocessorram`, `cupbai`, `buildId`, `deviceserial`, `imei`, `productprocessor`, `devicedensitydpi`, `screenwidth`, `devicefingerprint`, `zonetime`, `xpmdensity`, `timezonev`, `manufacture`, `ypmdensity`, `md5`, `basebandversion`, `screenheight`, `incremental`, `language`, `data_type`,`devicemodel`)VALUES ( "{procmeminfo}", "{phoneimsi}", "{vivoid}", "{locallanguage}", "{osversion}", "{carrieroperator}", {deviceid}, "{androidid}", "{vivoversion}", "{cupinfo}", "{devicerelease}", "{arm2}", "{devicebrand}", "{sdkint}", "{arm}", "{osversionoppo}", "{phonenum}", "{idproduct}", "{diskspace}", "{serialno}", "{productprocessorram}", "{cupbai}", "{buildId}", "{deviceserial}", "{imei}", "{productprocessor}", "{devicedensitydpi}", {screenwidth}, "{devicefingerprint}", "{zonetime}", "{xpmdensity}", "{timezonev}", "{manufacture}","{ypmdensity}", "{md5}", "{basebandversion}", {screenheight}, "{incremental}", "{language}", "{data_type}", "{devicemodel}");'

url = 'http://www.cainiaodk.com/v2/brush/getMachineUsed?keyword=daikuan-cainiaodk&channel=xiaomi'
redis_cli = redis.Redis(host='127.0.0.1',port=6379,db=0)

pycursor = connection.cursor()

try:
    while True:
        time.sleep(1)
        r = requests.get(url)
        data_json = r.json()
        # print(data_json)
        data = data_json['data']
        imei = data['imei']
        data['data_type'] = 1
        insert_sql_true = insert_sql.format_map(data)
        
        if redis_cli.get(imei):
            continue
        logging.info(insert_sql_true)
        pycursor.execute(insert_sql_true)
        connection.commit()        
        redis_cli.set(imei,1)
except Exception as e:
    logging.error(e)
    connection = pymysql.connect(**config)
    pycursor = connection.cursor()
    redis_cli = redis.Redis(host='127.0.0.1',port=6379,db=0)
finally:
        
    
    pycursor.close()
    connection.close()
        
    