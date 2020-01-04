def setBaseCurrency(redisClient):
    baseCurrency = "356"
    redisClient.set('baseCurrency', baseCurrency)
    print("base currency loaded 356")


