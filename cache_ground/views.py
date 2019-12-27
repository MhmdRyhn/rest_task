from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .services import get_data, save_or_update_data
from redis.exceptions import ConnectionError


class CacheView(View):
    def get(self, request, *args, **kwargs):
        try:
            query_param = request.GET.get('keys')
            status_code, response_body = get_data(query_param)

            response = {
                'status_code': status_code,
                'body': response_body
            }
        except ConnectionError:
            response = {
                'status_code': 500,
                'body': 'Database Connection Error'
            }
        except Exception:
            response = {
                'status_code': 500,
                'body': 'Internal Server Error'
            }
        return JsonResponse(response)

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        try:
            request_body = request.body
            if request_body:
                status_code, body = save_or_update_data(request_body)
            else:
                status_code, body = 204, {}

            response = {
                'status_code': status_code,
                'body': body
            }
        except ConnectionError:
            response = {
                'status_code': 500,
                'body': 'Database Connection Error'
            }
        except Exception:
            response = {
                'status_code': 500,
                'body': 'Internal Server Error'
            }
        finally:
            return JsonResponse(response)

    @csrf_exempt
    def patch(self, request, *args, **kwargs):
        request_body = request.body
        if request_body:
            status_code, body = save_or_update_data(request_body)
        else:
            status_code, body = 204, {}

        return JsonResponse({
            'status_code': status_code,
            'body': body
        })
