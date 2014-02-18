#!python

import unittest, mock
from mock import Mock, MagicMock

import ascendancy 
from ascendancy.core import Ascendancy
from ascendancy.db_connector import AscendancyDbConnector

class AscendancyTest(unittest.TestCase):

    def setUp(self):
        mock_datastore = MagicMock()
        mock_datastore.get_player = MagicMock(return_value={'player': 12345})
        self.ascendancy = Ascendancy(datastore=mock_datastore)

    def test_get_player(self):
        expected_response_body = u'{"player": {"id": 12345, "first_name": "bob", "surname": "bobington", "ecf_code": "1234AB1", "ecf_member_code": "123456AB"}'
        response_body, keyed_args_dict = self.ascendancy.get_player(12345)

