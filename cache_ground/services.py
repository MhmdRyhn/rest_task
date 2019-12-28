from django.conf import settings
from django.core.cache import cache
from redis.exceptions import ConnectionError


def get_invalid_key_error(keys):
    """
    This function checks if all the requested
    keys are present in the storage or not.

    :param keys: Values to be retrieved for
    :return: error if keys not found or {}
    """
    error = {}
    for key in keys:
        if not cache.get(key):
            error[key] = 'Key Not Found'
    return error


def get_values_by_keys(keys):
    body, status_code = {}, 200
    error = {}
    try:
        for key in keys:
            value = cache.get(key)
            if value:
                body[key] = value
                cache.expire(key, timeout=settings.CACHE_TTL)
            else:
                error[key] = 'Key not found in storage'
    except ConnectionError:
        error = 'Service Unavailable'
        status_code = 503
    except Exception as ex:
        error = 'Internal Server Error'
        status_code = 500
    return status_code, body, error


def get_data(query_param):
    if query_param:
        keys = query_param.split(',')
    else:
        keys = cache.keys('*')

    status_code, body, error = get_values_by_keys(keys)
    return status_code if body else 204, body, error


def insert_data(body):
    status_code = 200
    error = {}
    try:
        for key, value in body.items():
            cache.set(key, value, timeout=settings.CACHE_TTL)
    except ConnectionError:
        error = 'Service Unavailable'
        status_code = 503
    except Exception:
        error = 'Internal Server Error'
        status_code = 500
    return status_code, body, error


def update_data(body):
    status_code = 200
    error = {}
    to_be_popped_key = []
    try:
        for key, value in body.items():
            if cache.get(key):
                cache.set(key, value, timeout=settings.CACHE_TTL)
            else:
                to_be_popped_key.append(key)
                error[key] = 'Key not found in storage'

    except ConnectionError:
        error = 'Service Unavailable'
        status_code = 503
    except Exception as ex:
        error = 'Internal Server Error'
        status_code = 500

    for key in to_be_popped_key:
        body.pop(key)

    return status_code, body, error


if __name__ == '__main__':
    post_data = {
        "key1": "v1",
        "key2": "v2",
        "key3": "v3"
    }

    patch_data = {
        "key1": "v1-1",
        "key2": "v2",
        "key3": "v3"
    }
