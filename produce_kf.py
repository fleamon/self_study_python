# -*- encoding: utf-8

import json
import time
import datetime
from confluent_kafka import Consumer, KafkaException, KafkaError, Producer
from multiprocessing import Process
from multiprocessing import Pool
import asyncio

import string 
import random 

#broker = 'dev-ay-kafka.daumkakao.io:9092'
broker = 'prod-ay-kafka.daumkakao.io:9092'
#broker = 'prod-ay-kafka.daumkakao.io:9092'

topic = 'bi-sublog-talk-calendar-app'
#topic = 'bi-sublog-talk-bot'
#dd = '\n'

# See https://github.com/edenhill/librdkafka/blob/master/CONFIGURATION.md
conf = {'bootstrap.servers': broker, 'compression.codec': 'gzip', 'acks': 1}

## 정상 로그
log = {"wooneo":"love!"}
#log = {"type":"express_app_rshlog","k_timestamp":"2021-03-16T09:39:53.615+09:00","kafka_topic":"kemi-talkmsg-express-production","path":"/log/express/release/orion_express_app.11000.rsh.log","_uuid":"talkmsg_express_rsh_production-dkosv3-talkmsg-prod-ay-worker-54-761d106f73bc095c1a4cd17223c6496fc871f554","host":"dkosv3-talkmsg-prod-ay-worker-54","log":"2021-03-16T09:39:53.615\tRSH 5452144 137517100796316 s - 2 0 - - - 0 0 0 - - -","@timestamp":"2021-03-16T00:39:53.615Z","@version":"1","_kemi_tag":"talkmsg_express_rsh_production"}
#log = {"type":"express_app_rshlog","k_timestamp":"2021-03-16T09:39:53.615+09:00","kafka_topic":"kemi-talkmsg-express-production","path":"/log/express/release/orion_express_app.11000.rsh.log","_uuid":"talkmsg_express_rsh_production-dkosv3-talkmsg-prod-ay-worker-54-761d106f73bc095c1a4cd17223c6496fc871f554","host":"dkosv3-talkmsg-prod-ay-worker-54","log":"2021-03-16T09:39:53.615\tRSH 5452144 137517100796316 s - 2 0 - - - 0 0 0 - - -","@timestamp":"2021-03-16T00:39:53.615Z","@version":"1","_kemi_tag":"talkmsg_express_openlink_production"}

def produce_kf(log, name, ty = 'dict'): 
    print("process {}".format(name))
    p = Producer(**conf)
    data = log
    #if ty == 'dict' :
        #log['bi_meta']['log_datetime_id']  = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        #log['log'] = gen_string(1200)
    data = json.dumps(log)

    idx = 0
    start = time.time()
    while True:
        try :
            print("log")
            p.produce(topic, data)
        except BufferError as bfer:
            print('Flush Buffer')
            p.flush()

        idx += 1
        if time.time() - start > 1 :
            start = time.time()
            print('process {}, {} event per sec'.format(name, idx))
            idx = 0
        time.sleep(0.01)

    p.flush()

def gen_string(n):
    _LENGTH = n
    # 10자리 
    string_pool = string.ascii_letters
    # 소문자 
    result = "" 
    for i in range(_LENGTH) :
        result += random.choice(string_pool)
    return result

if __name__ == '__main__':
    print("hello kafka produce start")
    #loop = asyncio.get_event_loop()             # 이벤트 루프를 얻음
    #loop.run_until_complete(print_add(1, 2))
    produce_kf( log, 'log', 'dict')
    #produce_kf( data2_1, 'str')
    #produce_kf( data1_1, 'dict')
    #produce_kf( data2_1, 'str')
    #produce_kf( data1_2, 'dict', 100)
