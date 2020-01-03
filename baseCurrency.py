import redis

redisClient = redis.StrictRedis(host='localhost', port=6379, db=0)
currency = {}
def setBaseCurrency():
    baseCurrency = "356"
    redisClient.set('baseCurrency', baseCurrency)