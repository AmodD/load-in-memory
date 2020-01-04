import sys
import redis

if sys.argv[1] == 'local':
    hostEnv = 'localhost'
elif sys.argv[1] == 'docker':
    hostEnv = 'redis'
else:
    hostEnv = 'localhost'

if hostEnv == 'localhost':
    redisClient = redis.StrictRedis('localhost', 6379, db=0)
else:
    redisClient = redis.StrictRedis('redis', 6379, db=0)


import baseCurrency
import conversionRate
import dataElementsSymbols
import redisCurrencyCodeDecimalsInserter

redisCurrencyCodeDecimalsInserter.redisInserter(redisClient)
dataElementsSymbols.dataElementInserter(redisClient)
conversionRate.currrencyConversion(redisClient)
baseCurrency.setBaseCurrency(redisClient)
