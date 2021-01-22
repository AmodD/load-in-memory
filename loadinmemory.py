import sys
import redis

import basecurrency
import conversionrate
import dataElementsSymbols
import currencycodeinserter
# import consumerslistinserter
import merchantlistinserter
import processingcodeinserter
import mcccodeinserter
from bidashboardinserter import loadpayment, loadactiveaccounts, loadtransaction, loaddispute, loadlistinstruments, \
    loadlistinstrumentclassifierupi, loadlistinstrumentclassifiercredit, loadlistinstrumentclassifierdebit, \
    loadlistinstrumentclassifierneft, loaddailyaverageriskscore, loaddailyavergaecompliancescore, loadpayments, \
    loadtransactions, loadlistproducts, loadproductclassifierlist, loadlistdatacashbackissued, loadlistdatacashbackused, \
    loadlistdatapremiumissued, loadlistdatapremiumused, loadlistdatastandardissued, loadlistdatastandardused

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

# consumersdbservice = consumersdb + 'api/consumers'

getMerchants = merchantsdb + 'api/merchants'

print(getMerchants)

getAcceptors = merchantsdb + 'api/acceptors'

print(getAcceptors)

redisClient = redis.StrictRedis(redis_host, redis_port)

basecurrency.setbasecurrency(redisClient)
currencycodeinserter.loadcurrencycodes(redisClient)
conversionrate.loadcurrencyconversionrates(redisClient)

# consumerslistinserter.loadconsumerslist(redisClient, consumersdbservice)
loadpayment(redisClient)
loadactiveaccounts(redisClient)
loadtransaction(redisClient)
loaddispute(redisClient)
loadlistinstruments(redisClient)
loadlistinstrumentclassifierupi(redisClient)
loadlistinstrumentclassifiercredit(redisClient)
loadlistinstrumentclassifierdebit(redisClient)
loadlistinstrumentclassifierneft(redisClient)
loaddailyaverageriskscore(redisClient)
loaddailyavergaecompliancescore(redisClient)
loadpayments(redisClient)
loadtransactions(redisClient)
loadlistproducts(redisClient)
loadproductclassifierlist(redisClient)
loadlistdatacashbackissued(redisClient)
loadlistdatacashbackused(redisClient)
loadlistdatapremiumissued(redisClient)
loadlistdatapremiumused(redisClient)
loadlistdatastandardissued(redisClient)
loadlistdatastandardused(redisClient)

merchantlistinserter.loadmerchantslist(redisClient, getMerchants)

merchantlistinserter.loadacceptorslist(redisClient, getAcceptors)

dataElementsSymbols.dataElementInserter(redisClient)

processingcodeinserter.processingcodepositioninserter(redisClient)
mcccodeinserter.loadmcccodes(redisClient)

fortiatelog('All tables loaded in memory successfully', '001', 'info', filename, '')
