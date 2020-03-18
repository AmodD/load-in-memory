from flo import fortiatelog
alertDomain = 'SF'
fileName = 'dataElementsSymbols.py'

def dataElementInserter(redisClient):
    method = 'dataElementInserter'
    f01001000 = {'0100': '!', '0110': '\"', '0120': '#', '0121': '$', '0130': '%', '0200': '&', '0210': '\'', '0220': '('}
    f01003001 = {'00': '!', '01': '\"', '09': '#', '10': '$', '14': '%', '20': '&', '21': '\'', '22': '(', '26': ')',
                '27': '*', '28': '+', '31': ',', '36': '-', '37': '.', '40': '/', '81': '0', '83': '1', '90': '2'}
    f01003002 = {'00': '!', '10': '\"', '20': '#', '30': '$'}
    f01003003 = {'00': '!', '10': '\"', '20': '#', '30': '$'}
    f01018000 = {'0742': '!', '0763': '\"', '0780': '#', '1520': '$', '1711': '%', '1731': '&', '2741': '\'', '3003': '(',
             '3020': ')', '3389': '*', '3504': '+', '3509': ',', '4829': '-', '4784': '.', '4900': '/', '5251': '0',
             '5411': '1', '5732': '2', '8931': '3', '9222': '4', '9311': '5', '6010': '6', '6011': '7', '6012': '8'}
    f01019000 = {'356': '!', '840': '\"', '276': '#', '784': '$', '036': '%', '826': '&', '124': '\'', '050': '(', '144': ')',
             '702': '*', '704':'+', '368':','}
    f01022001 = {'00': '!', '01': '\"', '02': '#', '03': '$', '04': '%', '05': '&', '06': '\'', '07': '(', '08': ')',
                '09': '*', '10': '+', '80': ',', '81': '-', '90': '.', '91': '/', '95': '0', '99': '1'}
    f01022002 = {'0': '!', '1': '\"', '2': '#', '6': '$', '8': '%', '9': '&'}
    f01025000 = {'00': '!', '01': '\"', '02': '#', '03': '$', '05': '%', '07': '&', '08': '\'', '51': '(', '59': ')', '71': '*'}
    f01049000 = {'356': '!', '840': '\"', '978': '#', '784': '$', '036': '%', '826': '&', '124': '\'', '050': '(', '144': ')',
             '702': '*', '704':'+', '368':','}

    redisClient.hmset('f01001000', f01001000)
    redisClient.hmset('f01003001', f01003001)
    redisClient.hmset('f01003002', f01003002)
    redisClient.hmset('f01003003', f01003003)
    redisClient.hmset('f01018000', f01018000)
    redisClient.hmset('f01019000', f01019000)
    redisClient.hmset('f01022001', f01022001)
    redisClient.hmset('f01022002', f01022002)
    redisClient.hmset('f01025000', f01025000)
    redisClient.hmset('f01049000', f01049000)
    # print(redisClient.hgetall('f01001000'))
    # print(redisClient.hgetall('f01003001'))
    # print(redisClient.hgetall('f01003002'))
    # print(redisClient.hgetall('f01003003'))
    # print(redisClient.hgetall('f01018000'))
    # print(redisClient.hgetall('f01019000'))
    # print(redisClient.hgetall('f01022001'))
    # print(redisClient.hgetall('f01022002'))
    # print(redisClient.hgetall('f01025000'))
    # print(redisClient.hgetall('f01049000'))

    fortiatelog(alertDomain, 'ASCII codes loaded in memory for dataElemnets 000, 003, 018, 019, 022, 025, 049', '002', 'info', fileName, method)
