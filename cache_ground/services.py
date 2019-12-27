import json

from django.conf import settings
from django.core.cache import cache


def get_data(query_param):
    def get_value_by_key(keys):
        body = {}
        for key in keys:
            value = cache.get(key)
            if value:
                body[key] = value
                cache.expire(key, timeout=settings.CACHE_TTL)
            else:
                body[key] = 'Key Not Found'
        return 200 if body else 204, body

    if query_param:
        keys = query_param.split(',')
    else:
        keys = cache.keys('*')

    status_code, response_body = get_value_by_key(keys)
    return status_code, response_body


def save_or_update_data(request_body):
    body = json.loads(request_body.decode('utf-8'))
    for key, value in body.items():
        cache.set(key, value, timeout=settings.CACHE_TTL)
    return 200, body
