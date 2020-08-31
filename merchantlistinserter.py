import requests
import json
import sys
from fpf.flo import fortiatelog
fileName = 'merchantlistinserter.py'


def Listmerchants(redisClient,merchantsdbservice):
    method = 'merchantlist'
    try:
        print(merchantsdbservice)
        response = requests.get(merchantsdbservice)
        responseText = json.loads(response.text)
        merchantslist = responseText['payload']['data']
        #print(merchantslist)
        print(len(merchantslist))

        for i in range(len(merchantslist)):
            redisClient.hmset("merchant" + str(merchantslist[i]['mid']), merchantslist[i])
            redisClient.rpush('list_of_merchant_id', str(merchantslist[i]['mid']))

        fortiatelog('merchant ids loaded into memory successfully', '004', 'info', fileName, method)

    except Exception as e:
        fortiatelog(e, '005', 'error', fileName, method)
        sys.exit(1)

