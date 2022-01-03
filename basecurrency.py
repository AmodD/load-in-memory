"""
This module sets the base currency for the entire setup
"""
from fpf.flo import fortiatelog
fileName = 'basecurrency.py'


def setbasecurrency(redisClient):
    """
    This function sets the base currency for the product. Currently it is INR.
    @param redisClient:
    """
    method = 'setcbasecurrency'
    basecurrency = "356"
    redisClient.set('basecurrency', basecurrency)
    fortiatelog('Base currency loaded as INR or 356', '007', 'info', fileName, method)
