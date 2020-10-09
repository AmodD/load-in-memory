from fpf.flo import fortiatelog
import json

fileName = 'processingcodeinserter.py'


def processingcodepositioninserter(redisClient):
    method = 'processingCodeInserter'

    f100001003000_position = {'000000': (1,2), '010000': (1,2),
                 '090000': (1, 2), '140000': (1, 2),
                 '200000': (1, 2), '210000': (1, 2),
                 '220000': (1, 2), '260000': (1, 2),
                 '270000': (1, 2), '280000': (1, 2),
                 '290000': (1, 2),  '310000': (1, 2),
                 '320000': (1, 2),  '360000': (1, 2),
                 '370000': (1, 2),  '400000': (1, 2),
                 '810000': (1, 2),  '830000': (1, 2),
                 '900000': (1, 2)}

    f100001003000list = ['000000', '010000',
                     '090000', '140000',
                     '200000', '210000',
                     '220000', '260000',
                     '270000', '280000',
                     '290000', '310000',
                     '320000', '360000',
                     '370000', '400000',
                     '810000', '830000',
                     '900000']

    f100001003001list = ['00', '01',
                         '09', '14',
                         '20', '21',
                         '22', '26',
                         '27', '28',
                         '29', '31',
                         '32', '36',
                         '37', '40',
                         '81', '83',
                         '90']

    f100001003002list = ['00', '10',
                         '20', '30']

    f100001003003list = ['00', '10',
                         '20', '30']

    redisClient.sadd('f100001003000_position', str(f100001003000_position))
    redisClient.sadd('100001003000', str(f100001003000list))
    redisClient.sadd('100001003001', str(f100001003001list))
    redisClient.sadd('100001003002', str(f100001003002list))
    redisClient.sadd('100001003003', str(f100001003003list))

    fortiatelog('Processing code compliance values loaded in memory', '002', 'info', fileName, method)
