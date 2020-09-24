import requests
import json
import sys
from fpf.flo import fortiatelog
fileName = 'merchantlistinserter.py'


def loadmerchantslist(redisClient,merchantsdbservice):
    method = 'loadmerchantslist'
    try:
        response = requests.get(merchantsdbservice)
        response_text = json.loads(response.text)
        merchantslist = response_text['payload']['data']

        for i in range(len(merchantslist)):
            redisClient.hmset("merchant" + str(merchantslist[i]['id']), merchantslist[i])
            redisClient.sadd('list_of_merchants', str(merchantslist[i]['id']))

        fortiatelog('merchant ids loaded into memory successfully', '004', 'info', fileName, method)

    except Exception as e:
        fortiatelog(e, '005', 'error', fileName, method)
        sys.exit(1)

