import sys
import redis
from flo import fortiatelog
from os import environ
#import configparser
import os
#config = configparser.ConfigParser()
try:
    redis_host = os.getenv('REDIS_HOST')
    redis_port = os.getenv('REDIS_PORT')
    # redis_host = os.getenv('HOST_IP')
    chp = os.getenv('URL_CHP_DBSERVICE')
    if redis_host == None:
        print("redis_host is not se in load-in-memoryt")
        sys.exit(1)
    if chp == None:
        print("chp is not set in load-in-memory")
        sys.exit(1)
except Exception as e:
    print(e)
    sys.exit(1)

alertDomain = 'TM'
fileName = 'loadinmemory.py'

chpdbservice = chp+'api/chp'
redisClient = redis.StrictRedis(redis_host, redis_port, db=0)


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
