import requests
import json


def chpList(redisClient):
    try:
        response = requests.get("http://localhost:48310/api/chp")
        responseText = json.loads(response.text)
        chplist = responseText['payload']['data']
        # print(chplist)
        # for i in range(len(chplist)):
        #     print('chp' + str(chplist[i]['ch_CIN']))
        # for i in range(len(chplist)):
        #     print(chplist[i])
        for i in range(len(chplist)):
            redisClient.hmset('chp'+str(chplist[i]['ch_CIN']), chplist[i])
        print('chp ids loaded into memory successfully')

    except Exception as e:
        print(e)
        print('chp-dbservice is not responding')

