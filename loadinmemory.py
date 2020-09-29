import sys
import redis

import basecurrency
import conversionrate
import dataElementsSymbols
import currencycodeinserter
import consumerslistinserter
import merchantlistinserter
import processingcodeinserter
import mcccodeinserter

from fpf import fenv
from fpf import flo
from fpf import fjo
from fpf.flo import fortiatelog

filename = 'loadinmemory.py'
microservicename = 'loadinmemory'
microserviceacronym = 'LIM'

flo.fortiatelog('Starting ' + microservicename, '700', 'info', filename, '')

try:
    flo.setmicroservice(microservicename, microserviceacronym)
    fjo.setmicroservice(microservicename, microserviceacronym)
    fenv.setmicroservice(microservicename, microserviceacronym)
except Exception as e:
    flo.fortiatelog(e, '100', 'error', filename, '')
    sys.exit(1)

fjo.setparameters(percentage=10)

try:
    redis_host = fenv.hostredis
    redis_port = fenv.redisport
    consumersdb = fenv.hostconsumersdb
    merchantsdb = fenv.hostmerchantsdb

    if redis_host is None:
        print("redis_host is not set in fenv")
        sys.exit(1)
    if redis_port is None:
        print("redis_port is not set in fenv")
        sys.exit(1)
    if consumersdb is None:
        print("consumer-dbservice is not set in fenv")
        sys.exit(1)
    if merchantsdb is None:
        print("merchants-dbservice is not set in fenv")
        sys.exit(1)
except Exception as e:
    print(e)
    sys.exit(1)

consumersdbservice = consumersdb + 'api/consumers'

getMerchants = merchantsdb + 'api/merchants'

print(getMerchants)

getTerminals = merchantsdb + 'api/terminals'

print(getTerminals)

redisClient = redis.StrictRedis(redis_host, redis_port)

basecurrency.setbasecurrency(redisClient)
currencycodeinserter.loadcurrencycodes(redisClient)
conversionrate.loadcurrencyconversionrates(redisClient)

consumerslistinserter.loadconsumerslist(redisClient, consumersdbservice)

merchantlistinserter.loadmerchantslist(redisClient, str(getMerchants))

merchantlistinserter.loadterminalslist(redisClient, getTerminals)

dataElementsSymbols.dataElementInserter(redisClient)

processingcodeinserter.processingcodepositioninserter(redisClient)
mcccodeinserter.loadmcccodes(redisClient)

fortiatelog('All tables loaded in memory successfully', '001', 'info', filename, '')
