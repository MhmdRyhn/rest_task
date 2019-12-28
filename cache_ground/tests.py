from django.test import TestCase

from .services import insert_data, get_data, update_data, get_values_by_keys


class RestKeyValueTest(TestCase):
    body = {
        'key1': 'v1',
        'key2': 'v2',
        'key3': 'v3'
    }

    def setUp(self):
        insert_data(self.body)

    # def tearDown(self):
    #     from django_redis import get_redis_connection
    #     con = get_redis_connection('default').flushall()

    def test_get_value_from_key_list(self):
        query_for = ['key1', 'key3']
        result = (200, {'key1': 'v1', 'key3': 'v3'}, {})
        response = get_values_by_keys(query_for)
        self.assertEqual(response, result)

    def test_get_value_from_key_list_2(self):
        query_for = ['key1', 'key3', 'key5']
        result = (200, {'key1': 'v1', 'key3': 'v3'}, {'key5': 'Key not found in storage'})
        response = get_values_by_keys(query_for)
        self.assertEqual(response, result)

    def test_get_value_from_query_param(self):
        query_param = 'key1,key2'
        result = (200, {'key1': 'v1', 'key2': 'v2'}, {})
        response = get_data(query_param)
        self.assertEqual(response, result)

    def test_get_value_from_empty_query_param(self):
        query_param = None
        result = (200, {'key1': 'v1', 'key2': 'v2', 'key3': 'v3'}, {})
        response = get_data(query_param)
        self.assertEqual(response, result)

    def test_get_value_after_update(self):
        update_data({'key1': 'v1-1'})
        query_for = ['key1', 'key2']
        result = (200, {'key1': 'v1-1', 'key2': 'v2'}, {})
        response = get_values_by_keys(query_for)
        self.assertEqual(response, result)

    def test_get_value_after_update_2(self):
        update_data({'key1': 'v1-1'})
        query_for = ['key5']
        result = (200, {}, {'key5': 'Key not found in storage'})
        response = get_values_by_keys(query_for)
        self.assertEqual(response, result)

    def test_get_all_value_after_update(self):
        update_data({'key1': 'v1-1'})
        query_param = None
        result = (200, {'key1': 'v1-1', 'key2': 'v2', 'key3': 'v3'}, {})
        response = get_data(query_param)
        self.assertEqual(response, result)
