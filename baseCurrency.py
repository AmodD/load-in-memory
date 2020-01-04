from loadInMemory import redisClient

currency = {}


def setBaseCurrency():
    baseCurrency = "356"
    redisClient.set('baseCurrency', baseCurrency)
    print("base currency loaded 356")

