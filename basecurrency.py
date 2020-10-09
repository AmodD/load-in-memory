from fpf.flo import fortiatelog
fileName = 'basecurrency.py'


def setbasecurrency(redisClient):
    method = 'setcasecurrency'
    basecurrency = "356"
    redisClient.set('basecurrency', basecurrency)
    fortiatelog('Base currency loaded as INR or 356', '007', 'info', fileName, method)

