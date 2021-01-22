import requests
import json
import sys
from fpf.flo import fortiatelog
fileName = 'merchantlistinserter.py'


def loadmerchantslist(redisClient, getMerchants):
    method = 'loadmerchantslist'
    try:
        response = requests.get(getMerchants,verify=False,timeout=None)
        response_text = json.loads(response.text)
        merchantslist = response_text['payload']['data']
        print(len(merchantslist))
        for objects in range(len(merchantslist)):
            redisClient.hmset("merchant" + str(merchantslist[objects]['id']), merchantslist[objects])
            redisClient.sadd('list_of_merchants', str(merchantslist[objects]['id']))

        fortiatelog('merchant ids loaded into memory successfully', '004', 'info', fileName, method)

    except Exception as e:
        fortiatelog(e, '005', 'error', fileName, method)
        sys.exit(1)


def loadacceptorslist(redisClient,getAcceptors):
    method = 'loadacceptorslist'
    try:
        response = requests.get(getAcceptors,verify=False,timeout=None)
        response_text = json.loads(response.text)
        acceptorslist = response_text['payload']['data']
        print(acceptorslist)

        for objects in range(len(acceptorslist)):
            redisClient.hmset("acceptor" + str(acceptorslist[objects]['id']), acceptorslist[objects])
            redisClient.sadd('list_of_acceptors', str(acceptorslist[objects]['id']))

        fortiatelog('acceptor ids loaded into memory successfully', '005', 'info', fileName, method)

    except Exception as e:
        fortiatelog(e, '006', 'error', fileName, method)
        sys.exit(1)