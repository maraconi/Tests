import unittest
from create_folder import create_folder

class TestCreateFolder(unittest.TestCase):

    def setUp(self):
        print('Вызов setUp')

    def test_request_code_1(self):
        self.assertEqual(201, create_folder('TestCase'), msg="Ошибка!!!")

    def test_request_code_2(self):
        self.assertEqual(409, create_folder('TestCase'))

    def tearDown(self):
        print('Вызов tearDown')

if __name__ == '__main__':
    unittest.main()