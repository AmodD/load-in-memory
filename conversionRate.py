from redisPython import redisClient

converionRate_356 = {"356": 1.0000, "840": 70.9086, "978": 78.5764, "826": 93.3888, "036": 48.3025, "784": 19.3117,
                     "144": 0.390901}
converionRate_840 = {"356": 0.0141027, "840": 70.9086, "978": 1.12097, "826": 1.32238, "036": 0.700104, "784": 0.272294,
                     "144": 0.00550932}


def currrencyConversion():
    redisClient.hmset('currencyConverion_356', converionRate_356)
    redisClient.hmset('currencyConverion_840', converionRate_840)
    print("Conversion rates are loaded into memory")


if __name__ == '__main__':
    currrencyConversion()
