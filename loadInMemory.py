import redisCurrencyCodeDecimalsInserter, dataElementsSymbols,conversionRate,baseCurrency
import sys
hostEnv = ''
if sys.argv[0] == 'local':
    hostEnv = 'localhost'
elif sys.argv[0] == 'docker':
    hostEnv = 'redis'
redisCurrencyCodeDecimalsInserter.redisInserter()
dataElementsSymbols.dataElementInserter()
conversionRate.currrencyConvrsion()
baseCurrency.setBaseCurrency()
