import requests
import json
import sys
from flo import fortiatelog
alertDomain = 'SF'
fileName = 'merchantlistinserter.py'


def merchantlist(redisClient,merchantdbservice):
    method = 'merchantlist'
    try:
        response = requests.get(merchantdbservice)
        responseText = json.loads(response.text)
        merchantlist = responseText['payload']['data']
        print(len(merchantlist))

        for i in range(len(merchantlist)):
            redisClient.hmset("merchant" + str(merchantlist[i]['MHTID']), merchantlist[i])
            redisClient.rpush('list_of_merchant_id', str(merchantlist[i]['MHTID']))

        fortiatelog(alertDomain, 'merchant ids loaded into memory successfully', '004', 'info', fileName, method)

    except Exception as e:
        fortiatelog(alertDomain, e, '005', 'error', fileName, method)
        fortiatelog(alertDomain, 'merchant-dbservice is not responding', '006', 'error', fileName, method)
        sys.exit(1)

