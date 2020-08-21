import requests
import json
import sys
from fpf.flo import fortiatelog
fileName = 'consumerListInserter.py'

def consumersList(redisClient,consumersdbservice):
    method = consumerList
    try:
        response = requests.get(consumersdbservice)
        responseText = json.loads(response.text)
        consumerslist = responseText['payload']['data']

        for i in range(len(consumerslist)):
            redisClient.hmset("consumer"+str(consumerslist[i]['pan']), consumerslist[i])
            redisClient.rpush('list_of_consumer_id', str(consumerslist[i]['pan']))

        fortiatelog('consumer ids loaded into memory successfully', '004', 'info', fileName, method)

    except Exception as e:
        fortiatelog(e, '005', 'error', fileName, method)
        fortiatelog('consumers-dbservice is not responding', '006', 'error', fileName, method)
        sys.exit(1)

