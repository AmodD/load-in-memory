import redis

redisClient = redis.StrictRedis(host='localhost', port=6379, db=0)
currency = {}
def basecurrency():
    baseCurrency = "356"
    currency["baseCurrency"] = baseCurrency
    redisClient.hmset('baseCurrency', currency)