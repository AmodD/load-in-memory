"""
This module provides the logging functionality for all the python microservices in fortiate platform
"""
import logging
import datetime
import pytz

logging.basicConfig(filename='app.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')

# global microservicename, microserviceacronym

microservicename = ''
microserviceacronym = ''


def setmicroservice(name, acronym):
    """
    This function sets the microservice name and its acronym
    :param name:
    :param acronym:
    """
    global microservicename, microserviceacronym
    microservicename = name
    microserviceacronym = acronym


def dateTime():
    """
    This function sets the date and time for logging
    :return:
    """
    now = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
    return str(now.strftime('%d')) + '-' + str(now.strftime('%m')) + '-' + str(now.strftime('%y')) + ' ' + str(
        now.strftime('%H')) + ':' + str(now.strftime('%M'))


def fortiatelog(msg, code, level, filename, functionname):
    """
    This function sets the variables in the log - log level, program function that inserted the log entry, module name,
    the message for the debugger and a 3 digit unique code for quickly identifying the error location in the program
    :param msg:
    :param code:
    :param level:
    :param filename:
    :param functionname:
    """
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
    finalmsg = str(datetimevar) + "  -  " + str(filename) + " - " + str(functionname) + " [[" + str(microservicename) \
        + "]] {{" + str(level) + "}} ((" + str(finalcode) + ")) [{" + str(msg) + "}]"
    print(finalmsg)
    logging.error(finalmsg)

