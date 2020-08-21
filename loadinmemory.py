import json
import sys
import redis
import requests
import os

import merchantlistinserter

from fpf import fenv
from fpf import flo
from fpf import fjo
from fpf import fmq
from fpf.flo import fortiatelog

filename = 'loadinmemory.py'
microservicename = 'loadinmemory'
microserviceacronym = 'LIM'

flo.setmicroservice(microservicename, microserviceacronym)
fjo.setmicroservice(microservicename, microserviceacronym)
fenv.setmicroservice(microservicename, microserviceacronym)

flo.fortiatelog('Starting ' + microservicename, '700', 'info', filename, '')

fjo.setparameters(percentage=10)



try:
    redis_host = fenv.hostredis
    redis_port = fenv.redisport
    consumersdb = fenv.hostconsumersdb
    merchantsdb = fenv.hostmerchantsdb

    if redis_host == None:
        print("redis_host is not se in load-in-memoryt")
        sys.exit(1)
    if consumerdb == None:
        print("consumer is not set in load-in-memory")
        sys.exit(1)
    if merchantdb == None:
        print("merchants is not set in load-in-memory")
        sys.exit(1)
except Exception as e:
    print(e)
    sys.exit(1)

fileName = 'loadinmemory.py'

consumersdbservice = consumersdb + 'api/consumer'

merchantsdbservice = merchantsdb + 'api/merchant'

print(merchantsdbservice)

print(consumersdbservice)

redisClient = redis.StrictRedis(redis_host, redis_port, db=0)

import baseCurrency
import conversionRate
import dataElementsSymbols
import redisCurrencyCodeDecimalsInserter
import consumerListInserter
import processingCodeImageEnc
import mccImageEnc

redisCurrencyCodeDecimalsInserter.redisInserter(redisClient)
dataElementsSymbols.dataElementInserter(redisClient)
conversionRate.currrencyConversion(redisClient)
baseCurrency.setBaseCurrency(redisClient)
consumerListInserter.consumerList(redisClient, consumersdbservice)
merchantlistinserter.merchantlist(redisClient, merchantsdbservice)
processingCodeImageEnc.processingCodeInserter(redisClient)
mccImageEnc.mccInserter(redisClient)

fortiatelog('loaded in memory successfully', '001', 'info', fileName)
