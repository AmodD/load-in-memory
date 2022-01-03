"""
Unit testing module
"""
import unittest


class testpreprocessor(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        Test
        """
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        """
        Test
        """
        print('tearDownClass')

    def setUp(self):
        """
        Test
        """
        print('setUp')
        # self.microservicenamepreprocessor = 'preprocessor'
        # self.nonexistingmicroservicename = 'india'

    def tearDown(self):
        """
        Test
        """
        print('tearDown')

    # def test_fenv_sethostport(self):
    #     # assertion check for file PRESENT
    #     print('test_fenv_sethostport')
    #     hostportreceived = sethostport(self.microservicenamepreprocessor)
    #     print('port' + str(hostportreceived))
    #     hostportexpected = '48315'
    #     self.assertEqual(hostportreceived, hostportexpected)
    #
    # def test_hostenv_when_test_port_is_not_set(self):
    #     with self.assertRaises(SystemExit) as cm:
    #         sethostport(self.nonexistingmicroservicename)
    #     self.assertEqual(cm.exception.code, 1)


if __name__ == '__main__':
    unittest.main()
