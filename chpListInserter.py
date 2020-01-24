import requests
import json
import sys

def chpList(redisClient,chpdbservice):
    try:
        response = requests.get(chpdbservice)
        responseText = json.loads(response.text)
        chplist = responseText['payload']['data']

        # print(chplist)
        # for i in range(len(chplist)):
        #     print('chp' + str(chplist[i]['ch_CIN']))
        # for i in range(len(chplist)):
        #     print(chplist[i])

        for i in range(len(chplist)):
            redisClient.hmset('chp'+str(chplist[i]['ch_CIN']), chplist[i])
            redisClient.rpush('chplist', 'chp'+str(chplist[i]['ch_CIN']))
        print('chp ids loaded into memory successfully')
#        print('printing response')
#        print(response)

    except Exception as e:
        print(e)
        print('chp-dbservice is not responding')
        sys.exit(1)

