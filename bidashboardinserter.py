"""
This module does the work of loading the BI dashboard  into cache memory
"""
import requests
import json
import sys
from fpf.flo import fortiatelog
import random

fileName = 'bidashboardinserter.py'


def loadactiveaccounts(redisClient):
    """
    This function loads the count of active accounts into cache memory
    @param redisClient:
    """
    method = 'loadactiveaccounts'
    try:
        res = [random.randrange(1, 5, 1) for _ in range(365)]
        res = [str(x) for x in res]

        for objects in range(len(res)):
            redisClient.rpush('activeaccounts', str(res[objects]))

        fortiatelog('activeaccounts loaded into memory successfully', '013', 'info', fileName, method)

    except Exception as e:
        fortiatelog(e, '014', 'error', fileName, method)
        sys.exit(1)


def loadtransaction(redisClient):
    """
    This function loads the transactions into cache memory
    @param redisClient:
    """
    method = 'loadtransaction'
    try:
        res = [random.randrange(1, 99999, 1) for _ in range(365)]
        res = [str(x) for x in res]

        for objects in range(len(res)):
            redisClient.rpush('transaction', str(res[objects]))

        fortiatelog('transaction loaded into memory successfully', '015', 'info', fileName, method)

    except Exception as e:
        fortiatelog(e, '016', 'error', fileName, method)
        sys.exit(1)


def loaddispute(redisClient):
    """
    This function loads the disputes  into cache memory
    @param redisClient:
    """
    method = 'loaddispute'
    try:
        res = [random.randrange(1, 99999, 1) for _ in range(365)]
        res = [str(x) for x in res]

        for objects in range(len(res)):
            redisClient.rpush('dispute', str(res[objects]))

        fortiatelog('dispute loaded into memory successfully', '017', 'info', fileName, method)

    except Exception as e:
        fortiatelog(e, '018', 'error', fileName, method)
        sys.exit(1)


def loadlistinstruments(redisClient):
    """
    This function loads the instruments i.e. cards, mobiles into cache memory
    @param redisClient:
    """
    method = 'loadlistinstruments'
    try:
        res = ["upi", "credit", "debit", "neft"]

        for objects in range(len(res)):
            redisClient.rpush('list_instruments', str(res[objects]))

        fortiatelog('list_instruments loaded into memory successfully', '019', 'info', fileName, method)

    except Exception as e:
        fortiatelog(e, '020', 'error', fileName, method)
        sys.exit(1)


def loadlistinstrumentclassifierupi(redisClient):
    """
    This function loads the instrument classifier - UPI  into cache memory
    @param redisClient:
    """
    method = 'loadlistinstrumentclassifierupi'
    try:
        res = [random.randrange(1, 99, 1) for _ in range(365)]
        res = [str(x) for x in res]

        for objects in range(len(res)):
            redisClient.rpush('list_instrument_classifier_upi', str(res[objects]))

        fortiatelog('list_instrument_classifier_upi loaded into memory successfully', '021', 'info', fileName, method)

    except Exception as e:
        fortiatelog(e, '022', 'error', fileName, method)
        sys.exit(1)


def loadlistinstrumentclassifiercredit(redisClient):
    """
    This funciton loads the instrument classifier - Credit cards  into cache memory
    @param redisClient:
    """
    method = 'loadlistinstrumentclassifiercredit'
    try:
        res = [random.randrange(1, 99, 1) for _ in range(365)]
        res = [str(x) for x in res]

        for objects in range(len(res)):
            redisClient.rpush('list_instrument_classifier_credit', str(res[objects]))

        fortiatelog('list_instrument_classifier_credit loaded into memory successfully', '023', 'info', fileName,
                    method)

    except Exception as e:
        fortiatelog(e, '024', 'error', fileName, method)
        sys.exit(1)


def loadlistinstrumentclassifierdebit(redisClient):
    """
    This function classifies the instrument classifier - Debit cards into cache memory
    @param redisClient:
    """
    method = 'loadlistinstrumentclassifierdebit'
    try:
        res = [random.randrange(1, 99, 1) for _ in range(365)]
        res = [str(x) for x in res]

        for objects in range(len(res)):
            redisClient.rpush('list_instrument_classifier_debit', str(res[objects]))

        fortiatelog('list_instrument_classifier_debit loaded into memory successfully', '025', 'info', fileName, method)

    except Exception as e:
        fortiatelog(e, '026', 'error', fileName, method)
        sys.exit(1)


def loadlistinstrumentclassifierneft(redisClient):
    """
    This function loads the instrument classifier - NEFT into cache memory
    @param redisClient:
    """
    method = 'loadlistinstrumentclassifierneft'
    try:
        res = [random.randrange(1, 99, 1) for _ in range(365)]
        res = [str(x) for x in res]

        for objects in range(len(res)):
            redisClient.rpush('list_instrument_classifier_neft', str(res[objects]))

        fortiatelog('list_instrument_classifier_neft loaded into memory successfully', '027', 'info', fileName, method)

    except Exception as e:
        fortiatelog(e, '028', 'error', fileName, method)
        sys.exit(1)


def loaddailyaverageriskscore(redisClient):
    """
    This function loads the daily avg risk score into cache memory
    @param redisClient:
    """
    method = 'loaddailyaverageriskscore'
    try:
        res = [random.randrange(1, 99, 1) for _ in range(365)]
        res = [str(x) for x in res]

        for objects in range(len(res)):
            redisClient.rpush('daily_average_risk_score', str(res[objects]))

        fortiatelog('daily_average_risk_score loaded into memory successfully', '029', 'info', fileName, method)

    except Exception as e:
        fortiatelog(e, '030', 'error', fileName, method)
        sys.exit(1)


def loaddailyavergaecompliancescore(redisClient):
    """
    This function loads the avg compliance score into cache memory
    @param redisClient:
    """
    method = 'loaddailyavergaecompliancescore'
    try:
        res = [random.randrange(1, 99, 1) for _ in range(365)]
        res = [str(x) for x in res]

        for objects in range(len(res)):
            redisClient.rpush('daily_avergae_compliance_score', str(res[objects]))

        fortiatelog('daily_avergae_compliance_score loaded into memory successfully', '031', 'info', fileName, method)

    except Exception as e:
        fortiatelog(e, '032', 'error', fileName, method)
        sys.exit(1)


def loadpayments(redisClient):
    """
    This function loads the payments into cache memory
    @param redisClient:
    """
    method = 'loadpayments'
    try:
        res = [random.randrange(1, 9999, 1) for _ in range(365)]
        res = [str(x) for x in res]

        for objects in range(len(res)):
            redisClient.rpush('payments', str(res[objects]))

        fortiatelog('payments loaded into memory successfully', '033', 'info', fileName, method)

    except Exception as e:
        fortiatelog(e, '034', 'error', fileName, method)
        sys.exit(1)


def loadtransactions(redisClient):
    """
    This function loads the transactions into cache memory
    @param redisClient:
    """
    method = 'loadtransactions'
    try:
        res = [random.randrange(1, 99999, 1) for _ in range(365)]
        res = [str(x) for x in res]

        for objects in range(len(res)):
            redisClient.rpush('transactions', str(res[objects]))

        fortiatelog('transactions loaded into memory successfully', '035', 'info', fileName, method)

    except Exception as e:
        fortiatelog(e, '036', 'error', fileName, method)
        sys.exit(1)


def loadlistproducts(redisClient):
    """
    This function loads the list of products in cache memory
    @param redisClient:
    """
    method = 'loadlistproducts'
    try:
        res = ["standard", "premium", "cashback"]

        for objects in range(len(res)):
            redisClient.rpush('list_products', str(res[objects]))

        fortiatelog('list_products loaded into memory successfully', '037', 'info', fileName, method)

    except Exception as e:
        fortiatelog(e, '038', 'error', fileName, method)
        sys.exit(1)


def loadproductclassifierlist(redisClient):
    """
    This function loads the product classifier  in cache memory
    @param redisClient:
    """
    method = 'loadproductclassifierlist'
    try:
        res = ["issued", "used"]

        for objects in range(len(res)):
            redisClient.rpush('product_classifier_list', str(res[objects]))

        fortiatelog('product_classifier_list loaded into memory successfully', '039', 'info', fileName, method)

    except Exception as e:
        fortiatelog(e, '040', 'error', fileName, method)
        sys.exit(1)


def loadlistdatacashbackissued(redisClient):
    """
    This funciton loads the cashback related data in cache memory
    @param redisClient:
    """
    method = 'loadlistdatacashbackissued'
    try:
        res = [random.randrange(1, 9999, 1) for _ in range(365)]
        res = [str(x) for x in res]

        for objects in range(len(res)):
            redisClient.rpush('list_data_cashback_issued', str(res[objects]))

        fortiatelog('list_data_cashback_issued loaded into memory successfully', '041', 'info', fileName, method)

    except Exception as e:
        fortiatelog(e, '042', 'error', fileName, method)
        sys.exit(1)


def loadlistdatacashbackused(redisClient):
    """
    This function loads the cashbacks used data in cache memory
    @param redisClient:
    """
    method = 'loadlistdatacashbackused'
    try:
        res = [random.randrange(1, 9999, 1) for _ in range(365)]
        res = [str(x) for x in res]

        for objects in range(len(res)):
            redisClient.rpush('list_data_cashback_used', str(res[objects]))

        fortiatelog('list_data_cashback_used loaded into memory successfully', '043', 'info', fileName, method)

    except Exception as e:
        fortiatelog(e, '044', 'error', fileName, method)
        sys.exit(1)


def loadlistdatapremiumissued(redisClient):
    """
    This funciton loads the list of premium cards issued in cache memory
    @param redisClient:
    """
    method = 'loadlistdatapremiumissued'
    try:
        res = [random.randrange(1, 9999, 1) for _ in range(365)]
        res = [str(x) for x in res]

        for objects in range(len(res)):
            redisClient.rpush('list_data_premium_issued', str(res[objects]))

        fortiatelog('list_data_premium_issued loaded into memory successfully', '045', 'info', fileName, method)

    except Exception as e:
        fortiatelog(e, '046', 'error', fileName, method)
        sys.exit(1)


def loadlistdatapremiumused(redisClient):
    """
    This function loads the premium cards usage in cache memory
    @param redisClient:
    """
    method = 'loadlistdatapremiumused'
    try:
        res = [random.randrange(1, 9999, 1) for _ in range(365)]
        res = [str(x) for x in res]

        for objects in range(len(res)):
            redisClient.rpush('list_data_premium_used', str(res[objects]))

        fortiatelog('list_data_premium_used loaded into memory successfully', '047', 'info', fileName, method)

    except Exception as e:
        fortiatelog(e, '048', 'error', fileName, method)
        sys.exit(1)


def loadlistdatastandardissued(redisClient):
    """
    This function loads the standard cards issued in cache memory
    @param redisClient:
    """
    method = 'loadlistdatastandardissued'
    try:
        res = [random.randrange(1, 9999, 1) for _ in range(365)]
        res = [str(x) for x in res]

        for objects in range(len(res)):
            redisClient.rpush('list_data_standard_issued', str(res[objects]))

        fortiatelog('list_data_standard_issued loaded into memory successfully', '049', 'info', fileName, method)

    except Exception as e:
        fortiatelog(e, '050', 'error', fileName, method)
        sys.exit(1)


def loadlistdatastandardused(redisClient):
    """
    This function loads the standard card usage in cache memory
    @param redisClient:
    """
    method = 'loadlistdatastandardused'
    try:
        res = [random.randrange(1, 9999, 1) for _ in range(365)]
        res = [str(x) for x in res]

        for objects in range(len(res)):
            redisClient.rpush('list_data_standard_used', str(res[objects]))

        fortiatelog('list_data_standard_used loaded into memory successfully', '051', 'info', fileName, method)

    except Exception as e:
        fortiatelog(e, '052', 'error', fileName, method)
        sys.exit(1)

# def loadpayment(redisClient):
#     """
#     This function loads the payments into cache memory
#     @param redisClient:
#     """
#     method = 'loadpayment'
#     try:
#         res = [random.randrange(1, 9999, 1) for i in range(365)]
#         res = [str(x) for x in res]
#
#         for objects in range(len(res)):
#             redisClient.rpush('payment', str(res[objects]))
#
#         fortiatelog('payment loaded into memory successfully', '011', 'info', fileName, method)
#
#     except Exception as e:
#         fortiatelog(e, '012', 'error', fileName, method)
#         sys.exit(1)
