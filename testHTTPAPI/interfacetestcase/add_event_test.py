import unittest
import requests
import os
import sys
from db_fixture import test_data

#  添加搜索路径
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)


class AddEventTest(unittest.TestCase):
    """
    添加发布会测试类
    """
    def setUp(self):
        self.base_url = 'http://127.0.0.1/api/add_event/'

    def tearDown(self):
        print(self.result)

    def test_add_event_all_null(self):
        """
        所有参数为空的情况
        """
        payload = {'eid': '', 'name': '', 'limit': '', 'address': '', 'start_time': ''}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10021)
        self.assertEqual(self.result['message'], 'parameter error')

    def test_add_event_eid_exists(self):
        """
        eid已经存在
        """
        payload = {'eid': 1, 'name': '苹果发布会', 'limit': '2000', 'address': '火星', 'start_time': '2000-12-12 12:23:12'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10023)
        self.assertEqual(self.result['message'], 'event id already exists')

    def test_add_event_name_exists(self):
        """
        名称已经存在
        """
        payload = {'eid': 2, 'name': '小米发布会', 'limit': '2000', 'address': '火星', 'start_time': '2000-12-12 12:23:12'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10023)
        self.assertEqual(self.result['message'], '')

    def test_add_event_time_format_error(self):
        """
        发布会日期格式错误
        """
        payload = {'eid': 2, 'name': '小米发布会', 'limit': '2000', 'address': '火星', 'start_time': '2000-12-12'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10024)
        self.assertEqual(self.result['message'], '')

    def test_add_event_success(self):
        """
        发布会添加成功
        """
        payload = {'eid': 3, 'name': '红米发布会', 'limit': '2000', 'address': '火星', 'start_time': '2000-12-12 12:23:12'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], 'add event success')

    if __name__ == '__main__':
        test_data.init_data()  # 初始化接口测试数据
        unittest.main()
