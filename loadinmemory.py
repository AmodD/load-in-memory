import sys
import redis
import logging

logging.basicConfig(filename='load-in-memory.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

if sys.argv[1] == 'local':
    hostEnv = 'localhost'
    chpdbservice = 'http://localhost:48310/api/chp'
elif sys.argv[1] == 'docker':
    hostEnv = 'redis'
    chpdbservice = 'http://chp-dbservice/api/chp'
else:
    hostEnv = 'localhost'
    chpdbservice = 'http://localhost:48310/api/chp'

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
logging.warning('loaded in memory successfully')
