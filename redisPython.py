import redis
from loadInMemory import hostEnv

redisClient = ''

if hostEnv == 'localhost':
    redisClient = redis.StrictRedis('localhost', 6379, db=0)
else:
    redisClient = redis.StrictRedis('redis', 6379, db=0)

