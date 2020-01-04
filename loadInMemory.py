import sys

if sys.argv[1] == 'local':
    hostEnv = 'localhost'
elif sys.argv[1] == 'docker':
    hostEnv = 'redis'
else:
    hostEnv = 'localhost'


import baseCurrency
import conversionRate
import dataElementsSymbols
import redisCurrencyCodeDecimalsInserter

redisCurrencyCodeDecimalsInserter.redisInserter()
dataElementsSymbols.dataElementInserter()
conversionRate.currrencyConversion()
baseCurrency.setBaseCurrency()
