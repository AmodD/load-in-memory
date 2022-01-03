"""
This is a unit test module
"""
import unittest


# import requests
# from unittest.mock import patch


class testpreprocessor(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        Setup class
        """
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        """
        Tear down class
        """
        print('tearDownClass')

    def setUp(self):
        """
        Setup override
        """
        print('setUp')
        self.inputpath = '~/.fortiate/48990/23/imported/merchant_transaction1.csv'
        self.inputpath1 = '~/.fortiate/48990/23/imported/cardholder_transaction1.csv'
        self.csvname = 'merchant_transaction1.csv'
        self.csvname1 = 'merchant_transaction1.xlsx'
        self.csvname2 = 'regular1.txt'
        self.emptycsvwithheaders = '~/.fortiate/48990/23/imported/merchant_transaction1-empty-but-with-headers.csv'
        self.emptycsvwithoutheaders = '~/.fortiate/48990/23/imported/merchant_transaction1-empty-missing-headers.csv'
        self.nonemptycsv = '~/.fortiate/48990/23/imported/merchant_transaction1.csv'

    def tearDown(self):
        """
        Tear down override
        """
        print('tearDown')


if __name__ == '__main__':
    unittest.main()
