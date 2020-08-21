from fpf.flo import fortiatelog

fileName = 'processingCodeImageEnc.py'


def processingCodeInserter(redisClient):
    method = 'processingCodeInserter'

    f01003000 = {'000000': [(1, 2), '00ffff'], '010000': [(1, 2), '0000ff'],
                 '090000': [(1, 2), '808080'], '140000': [(1, 2), '00ff00'],
                 '200000': [(1, 2), '000080'], '210000': [(1, 2), 'c0c0c0'],
                 '220000': [(1, 2), 'ffffff'], '260000': [(1, 2), '000000'],
                 '270000': [(1, 2), 'ff00ff'], '280000': [(1, 2), '008000'],
                 '290000': [(1, 2), '800000'], '310000': [(1, 2), '808000'],
                 '320000': [(1, 2), 'ff0000'], '360000': [(1, 2), '008080'],
                 '370000': [(1, 2), 'ffff00'], '400000': [(1, 2), 'FFB000'],
                 '810000': [(1, 2), '480048'], '830000': [(1, 2), '484848'],
                 '900000': [(1, 2), '484800']}

    redisClient.hmset('f01003000', f01003000)

    # print(redisClient.hgetall('f01003000'))

    fortiatelog('color codes loaded in memory for dataElement 003', '002', 'info', fileName, method)
