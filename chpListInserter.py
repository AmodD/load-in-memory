import requests
import json
import sys
from fpf.flo import fortiatelog
fileName = 'chpListInserter.py'


def chpList(redisClient,chpdbservice):
    method = chpList
    try:
        response = requests.get(chpdbservice)
        responseText = json.loads(response.text)
        chplist = responseText['payload']['data']

        for i in range(len(chplist)):
            redisClient.hmset("chp"+str(chplist[i]['ch_CIN']), chplist[i])
            redisClient.rpush('list_of_chp_id', str(chplist[i]['ch_CIN']))

        fortiatelog('chp ids loaded into memory successfully', '004', 'info', fileName, method)

    except Exception as e:
        fortiatelog(e, '005', 'error', fileName, method)
        fortiatelog('chp-dbservice is not responding', '006', 'error', fileName, method)
        sys.exit(1)

