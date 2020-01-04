import redis
import hostEnv from loadInMemory
if hostEnv == 'local':
    redisClient = redis.StrictRedis('localhost', 6379, db=0)
elif hostEnv == 'docker':
    redisClient = redis.StrictRedis('redis', 6379, db=0)
currency = {}
def setBaseCurrency():
    baseCurrency = "356"
    redisClient.set('baseCurrency', baseCurrency)
