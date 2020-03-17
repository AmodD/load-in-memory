import logging
logging.basicConfig(filename='basecurrency.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

def setBaseCurrency(redisClient):
    baseCurrency = "356"
    redisClient.set('baseCurrency', baseCurrency)
    print("base currency loaded 356")
    logging.warning('base currency loaded 356')


