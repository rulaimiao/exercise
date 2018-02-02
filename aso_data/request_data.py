import requests
import redis
import pymysql

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

url = 'http://www.cainiaodk.com/v2/brush/getMachineUsed?keyword=daikuan-cainiaodk&channel=xiaomi'
insert_sql = 'INSERT INTO `aso_phone_data` (`procmeminfo`, `phoneimsi`, `vivoid`, `locallanguage`, `osversion`, `carrieroperator`, `deviceid`, `androidid`, `vivoversion`, `cupinfo`, `devicerelease`, `arm2`, `devicebrand`, `sdkint`, `arm`, `osversionoppo`, `phonenum`, `idproduct`, `diskspace`, `serialno`, `productprocessorram`, `cupbai`, `buildId`, `deviceserial`, `imei`, `productprocessor`, `devicedensitydpi`, `screenwidth`, `devicefingerprint`, `zonetime`, `xpmdensity`, `timezonev`, `manufacture`, `ypmdensity`, `md5`, `basebandversion`, `screenheight`, `incremental`, `language`, `data_type`,`devicemodel`)VALUES ( "{procmeminfo}", "{phoneimsi}", "{vivoid}", "{locallanguage}", "{osversion}", "{carrieroperator}", {deviceid}, "{androidid}", "{vivoversion}", "{cupinfo}", "{devicerelease}", "{arm2}", "{devicebrand}", "{sdkint}", "{arm}", "{osversionoppo}", "{phonenum}", "{idproduct}", "{diskspace}", "{serialno}", "{productprocessorram}", "{cupbai}", "{buildId}", "{deviceserial}", "{imei}", "{productprocessor}", "{devicedensitydpi}", {screenwidth}, "{devicefingerprint}", "{zonetime}", "{xpmdensity}", "{timezonev}", "{manufacture}","{ypmdensity}", "{md5}", "{basebandversion}", {screenheight}, "{incremental}", "{language}", "{data_type}", "{devicemodel}");'
redis_cli = redis.Redis(host='127.0.0.1',port=6379,db=0)

pycursor = connection.cursor()

while True:
    try:
        r = requests.get(url)
        data_json = r.json()
        # print(data_json)
        data = data_json['data']
        imei = data['imei']
        data['data_type'] = 1
        insert_sql = insert_sql.format_map(data)
        print(insert_sql)
        if redis_cli.get(imei):
            continue
        pycursor.execute(insert_sql)
        redis_cli.set(imei,1)
    except Exception as e:
        connection = pymysql.connect(**config)
        pycursor = connection.cursor()
        redis_cli = redis.Redis(host='127.0.0.1',port=6379,db=0)
    finally:
        
        connection.commit()
        pycursor.close()
        connection.close()
        break