#!python

import unittest
from mock import Mock, MagicMock

import ascendancy 
from ascendancy.core import Ascendancy

class AscendancyTest(unittest.TestCase):

    def setUp(self):
        mock_datastore = MagicMock()
        self.ascendancy = Ascendancy(datastore=mock_datastore)

