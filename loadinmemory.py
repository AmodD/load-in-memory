import sys
import redis
from flo import fortiatelog
alertDomain = 'TM'
fileName = 'loadinmemory.py'

def hostEnv():
    method = 'hostEnv'
    if sys.argv[1] == 'local':
        hostEnv = 'localhost'
        chpdbservice = 'http://localhost:48310/api/chp'
    elif sys.argv[1] == 'docker':
        hostEnv = 'redis'
        chpdbservice = 'http://chp-dbservice/api/chp'
    else:
        hostEnv = 'localhost'
        chpdbservice = 'http://localhost:48310/api/chp'
    return hostEnv,chpdbservice

hostEnv, chpdbservice = hostEnv()
redisClient = redis.StrictRedis(hostEnv, 6379, db=0)


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
