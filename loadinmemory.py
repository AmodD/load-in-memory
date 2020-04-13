import json
import sys
import redis
import requests
from flo import fortiatelog
import os

try:
    redis_host = os.getenv('REDIS_HOST')
    redis_port = os.getenv('REDIS_PORT')
    chp = os.getenv('URL_CHP_DBSERVICE')

    alarm = os.getenv('APP_ALARM')
    merchants = os.getenv('URL_MERCHANTS_DBSERVICE')
    if redis_host is None:
        print("redis_host is not se in load-in-memoryt")
        sys.exit(1)
    if chp is None:
        print("chp is not set in load-in-memory")
        sys.exit(1)
    if alarm is None:
        print("alarm is not set in load-in-memory")
        sys.exit(1)
    if merchants is None:
        print("merchants is not set in load-in-memory")
        sys.exit(1)
except Exception as e:
    print(e)
    sys.exit(1)

alertDomain = 'TM'
fileName = 'loadinmemory.py'

chpdbservice = chp+'api/chp'
redisClient = redis.StrictRedis(redis_host, redis_port, db=0)
client_url = alarm+'api/clients'
try:
    response = requests.get(client_url)
    client_json = json.loads(response.text)
    clients = client_json['payload']['data']
except Exception as e:
    clients = ''
    fortiatelog(alertDomain, e, '003', 'error', fileName)
    fortiatelog(alertDomain, 'alarm is not responding', '004', 'error', fileName)
    sys.exit(1)

fortiatelog(alertDomain, clients, '005', 'info', fileName)

# for client in clients:
#     mid = merchants+'api/'+client
#     fortiatelog(alertDomain, mid, '002', 'info', fileName)


import baseCurrency
import conversionRate
import dataElementsSymbols
import redisCurrencyCodeDecimalsInserter
import chpListInserter

redisCurrencyCodeDecimalsInserter.redisInserter(redisClient)
dataElementsSymbols.dataElementInserter(redisClient)
conversionRate.currrencyConversion(redisClient)
baseCurrency.setBaseCurrency(redisClient)
chpListInserter.chpList(redisClient,chpdbservice)
fortiatelog(alertDomain, 'loaded in memory successfully', '001', 'info', fileName)
