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

        print(merchantslist)

        i = 1
        while i < len(merchantslist):
            print("inside for loop")
            print(i)
            print(merchantslist[i])
            redisClient.hmset("merchant" + str(merchantslist[i]['id']), merchantslist[i])
            redisClient.sadd('list_of_merchants', str(merchantslist[i]['id']))
            i += 1

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

        i = 0
        while i < len(terminalslist):
            redisClient.hmset("terminal" + str(terminalslist[i]['id']), terminalslist[i])
            redisClient.sadd('list_of_terminals', str(terminalslist[i]['id']))
            i += 1

        fortiatelog('terminal ids loaded into memory successfully', '005', 'info', fileName, method)

    except Exception as e:
        fortiatelog(e, '006', 'error', fileName, method)
        sys.exit(1)
