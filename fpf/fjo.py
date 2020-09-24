import datetime
import calendar
import time
import pytz
from fpf.flo import fortiatelog

filename = 'fjo.py'

global microservicename, microserviceacronym
global parameters, data
global paramflag, dataflag
global id, token, datecreated, respstatus, message, respcode, respstatus
global client, clientid, action, usecase, domain, csvname, overwrite, algorithmid, algoname, algotype, configid, trainingid, percentage, location

microservicename = ''
microserviceacronym = ''
parameters = ''
paramflag = False
dataflag = False
id = ''
token = ''
datecreated = ''
respstatus = ''
message = ''
respcode = ''
respstatus = ''
client = ''
clientid = ''
action = ''
usecase = ''
domain = ''
csvname = ''
overwrite = ''
algorithmid = ''
algoname = ''
algotype = ''
configid = ''
trainingid = ''
percentage = ''
location = ''


def createid():
    method = 'createid'
    ts = calendar.timegm(time.gmtime())
    return str(ts)


def setmicroservice(name, acronym):
    method = 'setmicroservice'
    global microservicename, microserviceacronym
    microservicename = name
    microserviceacronym = acronym


def createdatetime():
    method = 'createdatetime'
    now = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
    return str(now.strftime('%d')) + '-' + str(now.strftime('%m')) + '-' + str(now.strftime('%y')) + ' ' + str(
        now.strftime('%H')) + ':' + str(now.strftime('%M'))


def setparameters(client='', clientid='', action='', usecase='', domain='', csvname='', overwrite='',algorithmid='',
                  algoname='', algotype='', configid='', trainingid='', percentage='', location=''):
    method = 'setparameters'
    global parameters, paramflag
    paramflag = True
    parameters = {
        'client': client,
        'clientid': clientid,
        'action': action,
        'usecase': usecase,
        'domain': domain,
        'csvname': csvname,
        'overwrite': overwrite,
        'algorithmid': algorithmid,
        'algoname': algoname,
        'algotype': algotype,
        'configid': configid,
        'trainingid': trainingid,
        'percentage': percentage,
        'location': location
    }


def setdata(dataobj=''):
    method = 'setdata'
    global data, dataflag
    dataflag = True
    data = dataobj


def createjson(message, respcode):
    method = 'createjson'
    global paramflag, dataflag, id, datecreated, respstatus

    if paramflag is False:
        setparameters()
    if dataflag is False:
        setdata()

    paramflag = False
    dataflag = False

    # Setting Header field values

    id = createid()

    token = id + " - " + microservicename

    datecreated = createdatetime()

    if respcode != '':
        if int(respcode) < 400:
            respstatus = 'success'
        elif int(respcode) >= 400 or int(respcode) < 600:
            respstatus = 'failure'
        else:
            respstatus = 'unknown'

    fjo = {
        'id': id,
        'token': token,
        'datecreated': datecreated,
        'respcode': respcode,
        'respstatus': respstatus,
        'microservicename': microservicename,
        'message': message,
        'payload': {'parameters': parameters,
                    'data': data}
    }
    return fjo


def parsejson(fjoobj):
    method = 'parsejson'
    try:
        global id, token, datecreated, respstatus, message, respcode, microservicename
        global parameters, data
        global client, clientid, action, usecase, domain, csvname, overwrite, algorithmid, algoname, algotype, configid, trainingid, percentage, location

        id = fjoobj['id']
        token = fjoobj['token']
        datecreated = fjoobj['datecreated']
        respcode = fjoobj['respcode']
        respstatus = fjoobj['respstatus']
        microservicename = fjoobj['microservicename']
        message = fjoobj['message']

        parameters = fjoobj['payload']['parameters']

        data = fjoobj['payload']['data']

        client = parameters['client']
        clientid = parameters['clientid']
        action = parameters['action']
        usecase = parameters['usecase']
        domain = parameters['domain']
        csvname = parameters['csvname']
        overwrite = parameters['overwrite']
        algorithmid = parameters['algorithmid']
        algoname = parameters['algoname']
        algotype = parameters['algotype']
        configid = parameters['configid']
        trainingid = parameters['trainingid']
        percentage = parameters['percentage']
        location = parameters['location']

    except Exception as e:
        fortiatelog(e, '101', 'error', filename, method)
        fortiatelog(fjoobj, '102', 'info', filename, method)
        raise
