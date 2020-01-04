import redis
import hostEnv from loadInMemory
if hostEnv == 'local':
    redisClient = redis.StrictRedis('localhost', 6379, db=0)
elif hostEnv == 'docker':
    redisClient = redis.StrictRedis('redis', 6379, db=0)


de000 = {'0100': '!', '0110': '\"', '0120': '#', '0121': '$', '0130': '%', '0200': '&', '0210': '\'', '0220': '('}
de003se1 = {'00': '!', '01': '\"', '09': '#', '10': '$', '14': '%', '20': '&', '21': '\'', '22': '(', '26': ')',
            '27': '*', '28': '+', '31': ',', '36': '-', '37': '.', '40': '/', '81': '0', '83': '1', '90': '2'}
de003se2 = {'00': '!', '10': '\"', '20': '#', '30': '$'}
de003se3 = {'00': '!', '10': '\"', '20': '#', '30': '$'}
de018 = {'0742': '!', '0763': '\"', '0780': '#', '1520': '$', '1711': '%', '1731': '&', '2741': '\'', '3003': '(',
         '3020': ')', '3389': '*', '3504': '+', '3509': ',', '4829': '-', '4784': '.', '4900': '/', '5251': '0',
         '5411': '1', '5732': '2', '8931': '3', '9222': '4', '9311': '5', '6010': '6', '6011': '7', '6012': '8'}
de019 = {'356': '!', '840': '\"', '276': '#', '784': '$', '036': '%', '826': '&', '124': '\'', '050': '(', '144': ')',
         '702': '*', '704':'+', '368':','}
de022se1 = {'00': '!', '01': '\"', '02': '#', '03': '$', '04': '%', '05': '&', '06': '\'', '07': '(', '08': ')',
            '09': '*', '10': '+', '80': ',', '81': '-', '90': '.', '91': '/', '95': '0', '99': '1'}
de022se2 = {'0': '!', '1': '\"', '2': '#', '6': '$', '8': '%', '9': '&'}
de025 = {'00': '!', '01': '\"', '02': '#', '03': '$', '05': '%', '07': '&', '08': '\'', '51': '(', '59': ')', '71': '*'}
de049 = {'356': '!', '840': '\"', '978': '#', '784': '$', '036': '%', '826': '&', '124': '\'', '050': '(', '144': ')',
         '702': '*', '704':'+', '368':','}


def dataElementInserter():
    redisClient.hmset('de000', de000)
    redisClient.hmset('de003se1', de003se1)
    redisClient.hmset('de003se2', de003se2)
    redisClient.hmset('de003se3', de003se3)
    redisClient.hmset('de018', de018)
    redisClient.hmset('de019', de019)
    redisClient.hmset('de022se1', de022se1)
    redisClient.hmset('de022se2', de022se2)
    redisClient.hmset('de025', de025)
    redisClient.hmset('de049', de049)
    # print(redisClient.hgetall('de000'))
    # print(redisClient.hgetall('de003se1'))
    # print(redisClient.hgetall('de003se2'))
    # print(redisClient.hgetall('de003se3'))
    # print(redisClient.hgetall('de018'))
    # print(redisClient.hgetall('de019'))
    # print(redisClient.hgetall('de022se1'))
    # print(redisClient.hgetall('de022se2'))
    # print(redisClient.hgetall('de025'))
    # print(redisClient.hgetall('de049'))
    print('ASCII codes loaded in memory for dataElements 000, 003, 018, 019, 022, 025, 049')

if __name__ == '__main__':
    dataElementInserter()
