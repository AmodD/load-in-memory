import logging
import datetime
import pytz

logging.basicConfig(filename='app.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')

global microservicename, microserviceacronym

microservicename = ''
microserviceacronym = ''


def setmicroservice(name, acronym):
    global microservicename, microserviceacronym
    microservicename = name
    microserviceacronym = acronym


def dateTime():
    now = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
    return str(now.strftime('%d')) + '-' + str(now.strftime('%m')) + '-' + str(now.strftime('%y')) + ' ' + str(
        now.strftime('%H')) + ':' + str(now.strftime('%M'))


def fortiatelog(msg, code, level, filename, functionname):
    datetimevar = dateTime()

    if level == 'warning':
        alertlevel = 'WN'
    elif level == 'error':
        alertlevel = 'ER'
    elif level == 'debug':
        alertlevel = 'DB'
    else:
        alertlevel = 'IN'

    finalcode = str(alertlevel) + str(microserviceacronym) + str(code)
    finalmsg = str(datetimevar) + "  -  " + str(filename) + " - " + str(functionname) + " [[" + str(microservicename) + "]] {{" + str(level) + "}} ((" + str(finalcode) + ")) [{" + str(
        msg) + "}]"
    print(finalmsg)
    logging.error(finalmsg)
    
    # if level == 'warning':
    #     logging.warning(finalmsg)
    # elif level == 'error':
    #     logging.error(finalmsg)
    # elif level == 'debug':
    #     logging.debug(finalmsg)
    # else:
    #     logging.info(finalmsg)
