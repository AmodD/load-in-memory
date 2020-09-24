import os
import sys
from fpf.flo import fortiatelog

filename = 'fenv.py'
#dummy change
global hostport, preprocessorport, cleanerport, labellerport, separatorport, modellerport, merchantmodellerport, forecasterport, exporterport, hosturl, redisport
global hostkafka, hostredis, confluentkafkaconsumer, confluentkafkaproducer
global hostfieldsdbservice, hostmerchantsdb, hostalarm, hostmodellingdb, hostconsumersdb
global microservicename, microserviceacronym

hostport = ''
confluentkafkaconsumer = ''
confluentkafkaproducer = ''
microservicename = ''
microserviceacronym = ''

try:
    hostredis = os.getenv('REDIS_HOST')
    hostkafka = os.getenv('KAFKA_SERVER')
    hostfieldsdbservice = os.getenv('URL_FIELDS_DBSERVICE')
    hostmerchantsdb = os.getenv('URL_MERCHANTS_DBSERVICE')
    hostconsumersdb = os.getenv('URL_CONSUMERS_DBSERVICE')
    hostmodellingdb = os.getenv('URL_MODELLING_DBSERVICE')
    hosturl = os.getenv('HOST_IP')
    hostalarm = os.getenv('URL_ALARM')
    
    redisport = os.getenv('REDIS_PORT')

    preprocessorport = os.getenv('PORT_PREPROCESSOR')
    cleanerport = os.getenv('PORT_CLEANER')
    labellerport = os.getenv('PORT_LABELLER')
    separatorport = os.getenv('PORT_SEPARATOR')
    modellerport = os.getenv('PORT_MODELLER')
    merchantmodellerport = os.getenv('PORT_MERCHANT_MODELLER')
    merchantforecasterport = os.getenv('PORT_MERCHANT_FORECASTER')
    exporterport = os.getenv('PORT_EXPORTER')
    fieldsdbport = os.getenv('PORT_FIELDS_DBSERVICE')

    appfieldsdbservice = os.getenv('APP_FIELDS_DBSERVICE')
    appconsumersdbservice = os.getenv('APP_CONSUMERS_DBSERVICE')

except Exception as e:
    fortiatelog(e, '001', 'error', filename, '')

try:
    if hostredis is None:
        fortiatelog('REDIS_HOST is not found or not set', '002', 'info', filename, '')
        sys.exit(1)
    if hostkafka is None:
        fortiatelog('KAFKA_SERVER is not found or not set', '003', 'info', filename, '')
        sys.exit(1)
    if hostfieldsdbservice is None:
        fortiatelog('URL_FIELDS_DBSERVICE not found  or not set', '004', 'info', filename, '')
        sys.exit(1)
    if hostmerchantsdb is None:
        fortiatelog('URL_MERCHANTS_DBSERVICE not found  or not set', '005', 'info', filename, '')
        sys.exit(1)
    if hostconsumersdb is None:
        fortiatelog('URL_CONSUMERS_DBSERVICE not found  or not set', '006', 'info', filename, '')
        sys.exit(1)
    if hostmodellingdb is None:
        fortiatelog('URL_MODELLING_DBSERVICE not found  or not set', '007', 'info', filename, '')
        sys.exit(1)
    if hosturl is None:
        fortiatelog('HOST_IP is not set', '008', 'info', filename, '')
        sys.exit(1)
    if redisport is None:
        fortiatelog('REDIS_PORT is not set', '011', 'info', filename, '')
        sys.exit(1)
except Exception as e:
    fortiatelog(e, '009', 'error', filename, '')


def sethostport(microservicename):
    global hostport
    if microservicename == 'preprocessor':
        hostport = preprocessorport
    elif microservicename == 'cleaner':
        hostport = cleanerport
    elif microservicename == 'labeller':
        hostport = labellerport
    elif microservicename == 'separator':
        hostport = separatorport
    elif microservicename == 'modeller':
        hostport = modellerport
    elif microservicename == 'merchantmodeller':
        hostport = merchantmodellerport
    elif microservicename == 'merchantforecaster':
        hostport = merchantforecasterport
    elif microservicename == 'exporter':
        hostport = exporterport
    elif microservicename == 'fieldsdbservice':
        hostport = fieldsdbport

    if hostport is None:
        fortiatelog('PORT_' + microservicename.upper() + ' is not set', '010', 'error', filename, 'sethostport')
        sys.exit(1)
    return hostport


def setmicroservice(name, acronym):
    method = 'setmicroservice'
    global microservicename, microserviceacronym
    microservicename = name
    microserviceacronym = acronym
    sethostport(microservicename)
