"""
This module inserts the list of consumers into cache memory
"""
import requests
import json
import sys
from fpf.flo import fortiatelog
fileName = 'consumerslistinserter.py'


def loadconsumerslist(redisClient, consumersdbservice):
    """
This function loads the consumer IDs and PAN numbers in redis
Requires following parameters as input
    @param redisClient:
    @param consumersdbservice:
    """
    method = 'consumerslist'
    try:
        response = requests.get(consumersdbservice, verify=False, timeout=120)
        response_text = json.loads(response.text)
        consumers_list = response_text['payload']['data']

        for key in range(len(consumers_list)):
            redisClient.hmset("consumer"+str(consumers_list[key]['id']), consumers_list[key])
            redisClient.sadd('list_of_consumers', str(consumers_list[key]['id']))

        fortiatelog('consumer ids loaded into memory successfully', '004', 'info', fileName, method)

    except Exception as e:
        fortiatelog(e, '005', 'error', fileName, method)
        fortiatelog('consumers-dbservice is not responding', '006', 'error', fileName, method)
        sys.exit(1)
