"""
This module loads the conversion rates into cache memory
"""
from fpf.flo import fortiatelog
fileName = 'coversionrate.py'


def loadcurrencyconversionrates(redisClient):
    """
    This funciton loads the currency conversion rates into cache
    @param redisClient:
    """
    method = 'loadcurrencyconversionrate'
    converionrate_356 = {"356": 1.0000, "840": 70.9086, "978": 78.5764, "826": 93.3888, "036": 48.3025, "784": 19.3117,
                         "144": 0.390901}
    converionrate_840 = {"356": 0.0141027, "840": 70.9086, "978": 1.12097, "826": 1.32238, "036": 0.700104,
                         "784": 0.272294,
                         "144": 0.00550932}

    redisClient.hmset('currency_converion_356', converionrate_356)
    redisClient.hmset('currency_converion_840', converionrate_840)
    fortiatelog('Conversion rates are loaded into memory', '003', 'info', fileName, method)
