import json

from django.conf import settings
from django.core.cache import cache


def get_values_by_keys(keys):
    body = {}
    for key in keys:
        value = cache.get(key)
        if value:
            body[key] = value
            cache.expire(key, timeout=settings.CACHE_TTL)
        else:
            body[key] = 'Key Not Found'
    return body


def get_data(query_param):
    if query_param:
        keys = query_param.split(',')
    else:
        keys = cache.keys('*')

    response_body = get_values_by_keys(keys)
    return 200 if response_body else 204, response_body


def save_or_update_data(request_body):
    body = json.loads(request_body.decode('utf-8'))
    for key, value in body.items():
        cache.set(key, value, timeout=settings.CACHE_TTL)
    return 200, body


if __name__ == '__main__':
    post_data = {
        "key1": "value 1",
        "key2": "value 2",
        "key3": "value 3",
        "key4": "value 4"
    }

    patch_data = {
        "key1": "value 1.1",
        "key2": 'value 2.1',
        "key3": "value 3.1",
        "key4": "value 4.1"
    }
