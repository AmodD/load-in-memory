import requests
import json
import sys
from fpf.flo import fortiatelog
fileName = 'merchantlistinserter.py'


def loadmerchantslist(redisClient, getMerchants):
    method = 'loadmerchantslist'
    try:
        response = requests.get(getMerchants)
        response_text = json.loads(response.text)
        merchantslist = response_text['payload']['data']

        for objects in range(len(merchantslist)):
            redisClient.hmset("merchant" + str(merchantslist[objects]['id']), merchantslist[objects])
            redisClient.sadd('list_of_merchants', str(merchantslist[objects]['id']))

        fortiatelog('merchant ids loaded into memory successfully', '004', 'info', fileName, method)

    except Exception as e:
        fortiatelog(e, '005', 'error', fileName, method)
        sys.exit(1)


def loadterminalslist(redisClient,getTerminals):
    method = 'loadterminalslist'
    try:
        response = requests.get(getTerminals)
        response_text = json.loads(response.text)
        terminalslist = response_text['payload']['data']
        print(terminalslist)

        for objects in range(len(terminalslist)):
            redisClient.hmset("terminal" + str(terminalslist[objects]['id']), terminalslist[objects])
            redisClient.sadd('list_of_terminals', str(terminalslist[objects]['id']))

        fortiatelog('terminal ids loaded into memory successfully', '005', 'info', fileName, method)

    except Exception as e:
        fortiatelog(e, '006', 'error', fileName, method)
        sys.exit(1)