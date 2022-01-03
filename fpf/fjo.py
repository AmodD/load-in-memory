"""
This module defines the structure of fortiate json object that is shared between microsrvices
"""
import datetime
import calendar
import time
import pytz
from fpf.flo import fortiatelog

filename = 'fjo.py'

# global microservicename, microserviceacronym
# global parameters, data
# global paramflag, dataflag
# global id, token, datecreated, respstatus, message, respcode
# global client, clientid, businessproblemid, fieldgroupid, action, usecaseid, domainid, csvname, algorithmid,
#        configid, trainingid, percentage, location

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
client = ''
clientid = ''
businessproblemid = ''
fieldgroupid = ''
action = ''
usecaseid = ''
domainid = ''
csvname = ''
algorithmid = ''
configid = ''
trainingid = ''
percentage = ''
location = ''
relationshipid = ''


def createid():
    """
    This function creates a unique id for each json object which is absolute timestamp, which always makes it unique
    :return: returns absolute timestamp value
    """
    method = 'createid'
    ts = calendar.timegm(time.gmtime())
    fortiatelog('Unique id - ' + ts, '101', 'info', filename, method)
    return str(ts)


def setmicroservice(name, acronym):
    """
    This funtion sets the microservice name and its acronym for fortiatelog and other modules to mention in their logs
    :param name: This is the name of the microservice for which environment variables are to be set
    :param acronym: This is the microservice acronym
    """
    method = 'setmicroservice'
    global microservicename, microserviceacronym
    microservicename = name
    microserviceacronym = acronym
    fortiatelog('Microservice name and acronym set - ' + microservicename + ',' + microserviceacronym,
                '102', 'info', filename, method)


def createdatetime():
    """
    This is the function creates a current date and time in specific format to be added in json object
    :return: 
    """
    method = 'createdatetime'
    now = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
    fortiatelog('Date and time -' + now, '103', 'info', filename, method)
    return str(now.strftime('%d')) + '-' + str(now.strftime('%m')) + '-' + str(now.strftime('%y')) + ' ' + str(
        now.strftime('%H')) + ':' + str(now.strftime('%M'))


def setparameters(client='', clientid='', businessproblemid='', fieldgroupid='',
                  action='', usecaseid='', domainid='', csvname='', algorithmid='',
                  configid='', trainingid='', percentage='', location='', relationshipid=''):
    """
    This function sets the parameter value for json object
    :param client: Client refers to the Client Name
    :param clientid: Client refers to the "Client ID" assigned by Fortiate
    :param businessproblemid: This refers to the "business problem ID" assigned by Fortiate
    :param fieldgroupid: This refers to the "Field Group ID" assigned by Fortiate
    :param action: This refers to the action to be taken when the object is received or sent
    :param usecaseid: This refers to the "Usecase ID" assigned by Fortiate
    :param domainid: This refers to the "Domain ID" assigned by Fortiate
    :param csvname: This contains the csv file name imported/uploaded/passed to other microservice
    :param algorithmid: This is the machine learning "Algorithm ID" assigned by Fortiate
    :param configid: This it the machine learning "Configuration ID" specific to the Algorithm, assigned by Fortiate
    :param trainingid: This it the machine learning "Training ID" generated after a training is done
    :param percentage: This is the percentage completion of any process within Fortiate platform
    :param location: This is the location microservices can share between each other as a clue
    """
    method = 'setparameters'
    global parameters, paramflag
    paramflag = True
    parameters = {
        'client': client,
        'clientid': clientid,
        'businessproblemid': businessproblemid,
        'fieldgroupid': fieldgroupid,
        'action': action,
        'usecaseid': usecaseid,
        'domainid': domainid,
        'csvname': csvname,
        'algorithmid': algorithmid,
        'configid': configid,
        'trainingid': trainingid,
        'percentage': percentage,
        'location': location,
        'relationshipid': relationshipid
    }
    fortiatelog('fjo paramters set', '104', 'info', filename, method)


def setdata(dataobj=''):
    """
    This function sets the data object
    :param dataobj:
    """
    method = 'setdata'
    global data, dataflag
    dataflag = True
    data = dataobj
    fortiatelog('fjo data object  set', '105', 'info', filename, method)


def createjson(message, respcode):
    """
    This function creates the json object
    :param message:
    :param respcode:
    :return:
    """
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

    token_local = id + " - " + microservicename

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
        'token': token_local,
        'datecreated': datecreated,
        'respcode': respcode,
        'respstatus': respstatus,
        'microservicename': microservicename,
        'message': message,
        'payload': {'parameters': parameters,
                    'data': data}
    }
    fortiatelog(message, '106', 'info', filename, method)
    return fjo


def parsejson(fjoobj):
    """
    This function parses the fortiate json object
    :param fjoobj:
    """
    method = 'parsejson'
    try:
        global id, token, datecreated, respstatus, message, respcode, microservicename
        global parameters, data
        global client, clientid, businessproblemid, fieldgroupid, action, usecaseid, domainid, csvname, algorithmid, \
            configid, trainingid, percentage, location, relationshipid

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
        businessproblemid = parameters['businessproblemid']
        fieldgroupid = parameters['fieldgroupid']
        action = parameters['action']
        usecaseid = parameters['usecaseid']
        domainid = parameters['domainid']
        csvname = parameters['csvname']
        algorithmid = parameters['algorithmid']
        configid = parameters['configid']
        trainingid = parameters['trainingid']
        percentage = parameters['percentage']
        location = parameters['location']
        relationshipid = parameters['relationshipid']

        fortiatelog('fjo parameters parsed successfully', '107', 'info', filename, method)
    except Exception as e:
        fortiatelog(e, '108', 'error', filename, method)
        fortiatelog(fjoobj, '109', 'info', filename, method)
        raise
