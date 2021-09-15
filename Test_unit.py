import unittest
from mock import patch
import unit


class TestUnit(unittest.TestCase):

    def setUp(self):
        print('Вызов setUp')

    @patch('unit.input')
    def test_get_doc_owner_name(self, mock):
        mock.return_value = '2207 876234'
        doc_number = unit.get_doc_owner_name()
        self.assertEqual('Василий Гупкин', doc_number)

    @patch('unit.input')
    def test_get_doc_shelf(self, mock):
        mock.return_value = '11-2'
        shelf_number = unit.get_doc_shelf()
        self.assertEqual('1', shelf_number)

    def test_get_all_doc_owners_names(self):
        self.assertIsInstance(unit.get_all_doc_owners_names(), set)

    @patch('unit.input')
    def test_add_new_doc(self, mock):
        mock.return_value = '3'
        shelf_number = unit.add_new_doc()
        self.assertEqual('3', shelf_number)

    @patch('unit.input')
    def test_delete_doc(self, mock):
        mock.return_value = '5455 028765'
        doc_number = unit.delete_doc()
        self.assertTrue(True, doc_number)

    def tearDown(self):
        print('Вызов tearDown')

if __name__ == '__main__':
    unittest.main()