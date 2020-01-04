from redisPython import redisClient

baseCurrency = "356"


def setBaseCurrency():
    redisClient.hset('baseCurrency', baseCurrency)
    print("base currency loaded 356")


if __name__ == '__main__':
    setBaseCurrency()
