import logging

logging.basicConfig(filename='app.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')

module = 'metl'
appName = 'load-in-memory'
# alertLevel = ''
appAcr = 'LIM'


def fortiatelog(alertDomain, msg, code='000', level='info', fileName='', method=''):
    method = method
    if level == 'warning':
        alertLevel = 'WN'
    elif level == 'error':
        alertLevel = 'ER'
    elif level == 'debug':
        alertLevel = 'DB'
    else:
        alertLevel = 'IN'

    finalCode = alertLevel + appAcr + alertDomain + code
    finalMsg = str(fileName) + " - " + str(method) + " {(" + str(module) + ")} {[" + str(alertDomain) + "]} [[" + \
               str(appName) + "]] {{" + str(level) + "}} ((" + str(finalCode) + ")) [{" + str(msg) + "}]"
    print(finalMsg)

    if level == 'warning':
        logging.warning(finalMsg)
    elif level == 'error':
        logging.error(finalMsg)
    elif level == 'debug':
        logging.debug(finalMsg)
    else:
        logging.info(finalMsg)
