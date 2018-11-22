import unittest

from SMWinservice import SMWinservice

class SMWinserviceImplTest(unittest.TestCase):
    def setUp(self):
        self.service = SMWinservice()


    def startTest(self):
        self.service.start()
        self.assertTrue(self.service.isrunning)

if __name__ == '__main__':
    unittest.main()