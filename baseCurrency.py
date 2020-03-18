from flo import fortiatelog
alertDomain = 'SF'
fileName = 'baseCurrency.py'

def setBaseCurrency(redisClient):
    method = 'setBaseCurrency'
    baseCurrency = "356"
    redisClient.set('baseCurrency', baseCurrency)
    fortiatelog(alertDomain, 'base currency loaded 356', '007', 'info', fileName, method)

