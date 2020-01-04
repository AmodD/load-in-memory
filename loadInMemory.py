import redisCurrencyCodeDecimalsInserter, dataElementsSymbols
import sys
hostEnv = ''
if sys.argv[0] == 'local':
    hostEnv = 'localhost'
elif sys.argv[0] == 'docker':
    hostEnv = 'redis'
redisCurrencyCodeDecimalsInserter.redisInserter()
dataElementsSymbols.dataElementInserter()
