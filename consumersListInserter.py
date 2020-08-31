import requests
import json
import sys
from fpf.flo import fortiatelog
fileName = 'consumersListInserter.py'

def consumersList(redisClient,consumersdbservice):
    method = consumersList
    try:
        response = requests.get(consumersdbservice)
        responseText = json.loads(response.text)
        consumerslist = responseText['payload']['data']

        for i in range(len(consumerslist)):
            print(len(consumerslist))
            redisClient.hmset("consumer"+str(consumerslist[i]['id']), consumerslist[i])
            redisClient.sadd('list_of_consumers_id', *str(consumerslist[i]['id']))

        #print(redisClient.scard(list_of_consumers_id))
        #print(redisClient.smembers(list_of_consumers_id))
        fortiatelog('consumer ids loaded into memory successfully', '004', 'info', fileName, method)

    except Exception as e:
        fortiatelog(e, '005', 'error', fileName, method)
        fortiatelog('consumers-dbservice is not responding', '006', 'error', fileName, method)
        sys.exit(1)

