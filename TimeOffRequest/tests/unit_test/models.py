from datetime import datetime, timedelta
import unittest
from TimeOffRequest import models


class ModelTest(unittest.TestCase):
    def setUp(self):
        self.models = models("John", "Smith", datetime.now(),datetime.now()+ timedelta(3) )
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
