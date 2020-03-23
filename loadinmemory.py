import sys
import redis
from flo import fortiatelog
from os import environ
import configparser

config = configparser.ConfigParser()

env = environ.get('FORTIATE_ENV')
if env == 'localhost':
    config.read('../.env.localhost')
    redis = config['DEFAULT']['REDIS_HOST']
    chp = config['DEFAULT']['APP_CHP']
    
elif env == 'localdocker':
    config.read('../.env.localdocker')
    redis = config['DEFAULT']['REDIS_HOST']
    chp = config['DEFAULT']['APP_CHP']

alertDomain = 'TM'
fileName = 'loadinmemory.py'

hostEnv, chpdbservice = redis, str(chp) + 'api/chp'
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
