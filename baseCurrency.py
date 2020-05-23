from flo import fortiatelog
fileName = 'baseCurrency.py'

def setBaseCurrency(redisClient):
    method = 'setBaseCurrency'
    baseCurrency = "356"
    redisClient.set('baseCurrency', baseCurrency)
    fortiatelog('base currency loaded 356', '007', 'info', fileName, method)

