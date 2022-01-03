"""
This module sets the environment variables
"""
import os
import sys
from fpf.flo import fortiatelog

filename = 'fenv.py'

global hostport, preprocessorport, preprocessoruiport, cleanerport, labellerport, separatorport, modellerport, \
    merchantmodellerport, forecasterport, exporterport, hosturl, redisport, setupservicesport, appsetupservices
global hostkafka, hostredis, confluentkafkaconsumer, confluentkafkaproducer
global hostsetupservices, hostmerchantsdb, hostalarm, hostmodellingdb, hostconsumersdb, hosttransactionsdb, \
    hostpropensitydb
global microservicename, microserviceacronym

hostport = ''
confluentkafkaconsumer = ''
confluentkafkaproducer = ''
microservicename = ''
microserviceacronym = ''

try:
    hostredis = os.getenv('REDIS_HOST')
    hostkafka = os.getenv('KAFKA_SERVER')
    hostmerchantsdb = os.getenv('URL_MERCHANTS_DBSERVICE')
    hostconsumersdb = os.getenv('URL_CONSUMERS_DBSERVICE')
    hostmodellingdb = os.getenv('URL_MODELLING_DBSERVICE')
    hosttransactionsdb = os.getenv('URL_TRANSACTIONS_DBSERVICE')
    hostpropensitydb = os.getenv('URL_PROPENSITY_DBSERVICE')
    hosturl = os.getenv('HOST_IP')
    hostalarm = os.getenv('URL_ALARM')
    hostsetupservices = os.getenv('URL_SS')
    
    redisport = os.getenv('REDIS_PORT')

    preprocessorport = os.getenv('PORT_PREPROCESSOR')
    preprocessoruiport = os.getenv('PORT_PREPROCESSOR_UI')
    cleanerport = os.getenv('PORT_CLEANER')
    labellerport = os.getenv('PORT_LABELLER')
    separatorport = os.getenv('PORT_SEPARATOR')
    modellerport = os.getenv('PORT_MODELLER')
    merchantmodellerport = os.getenv('PORT_MERCHANT_MODELLER')
    merchantforecasterport = os.getenv('PORT_MERCHANT_FORECASTER')
    exporterport = os.getenv('PORT_EXPORTER')
    fieldsdbport = os.getenv('PORT_FIELDS_DBSERVICE')
    setupservicesport = os.getenv('PORT_SS')

    appfieldsdbservice = os.getenv('APP_FIELDS_DBSERVICE')
    appsetupservices = os.getenv('APP_SETUP_SERVICES')
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
    if hostmerchantsdb is None:
        fortiatelog('URL_MERCHANTS_DBSERVICE not found  or not set', '004', 'info', filename, '')
        sys.exit(1)
    if hostconsumersdb is None:
        fortiatelog('URL_CONSUMERS_DBSERVICE not found  or not set', '005', 'info', filename, '')
        sys.exit(1)
    if hostmodellingdb is None:
        fortiatelog('URL_MODELLING_DBSERVICE not found  or not set', '006', 'info', filename, '')
        sys.exit(1)
    if hosttransactionsdb is None:
        fortiatelog('URL_TRANSACTIONS_DBSERVICE not found  or not set', '007', 'info', filename, '')
        sys.exit(1)
    if hosturl is None:
        fortiatelog('HOST_IP is not set', '008', 'info', filename, '')
        sys.exit(1)
    if redisport is None:
        fortiatelog('REDIS_PORT is not set', '009', 'info', filename, '')
        sys.exit(1)
    if hostsetupservices is None:
        fortiatelog('URL_SS is not set', '010', 'info', filename, '')
        sys.exit(1)
    if setupservicesport is None:
        fortiatelog('PORT_SS is not set', '011', 'info', filename, '')
        sys.exit(1)
    if appsetupservices is None:
        fortiatelog('APP_SETUP_SERVICES is not set', '012', 'info', filename, '')
        sys.exit(1)
except Exception as e:
    fortiatelog(e, '013', 'error', filename, 'main function')


def sethostport(microservicename1):
    """
    This function sets the port value
    :param microservicename1: 
    :return: 
    """
    method = sethostport
    global hostport
    if microservicename1 == 'preprocessor':
        hostport = preprocessorport
    elif microservicename1 == 'preprocessor-ui':
        hostport = preprocessoruiport
    elif microservicename1 == 'cleaner':
        hostport = cleanerport
    elif microservicename1 == 'labeller':
        hostport = labellerport
    elif microservicename1 == 'separator':
        hostport = separatorport
    elif microservicename1 == 'modeller':
        hostport = modellerport
    elif microservicename1 == 'merchantmodeller':
        hostport = merchantmodellerport
    elif microservicename1 == 'merchantforecaster':
        hostport = merchantforecasterport
    elif microservicename1 == 'exporter':
        hostport = exporterport
    elif microservicename1 == 'fieldsdbservice':
        hostport = fieldsdbport

    if hostport is None:
        fortiatelog('PORT_' + microservicename1.upper() + ' is not set', '014', 'error', filename, method)
        sys.exit(1)
    return hostport


def setmicroservice(name, acronym):
    """
    This funciton sets the microservice name
    :param name:
    :param acronym:
    """
    method = 'setmicroservice'
    global microservicename, microserviceacronym
    microservicename = name
    microserviceacronym = acronym
    sethostport(microservicename)
    fortiatelog('Microservice name and acronym set', '014', 'info', filename, method)
