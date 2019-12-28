import json

from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .services import get_data, insert_data, update_data


class CacheView(View):
    def get(self, request, *args, **kwargs):
        query_param = request.GET.get('keys')
        status_code, response_body, error = get_data(query_param)

        response = {
            'status_code': status_code,
            'body': response_body,
            'error': error
        }
        return JsonResponse(response)

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        request_body = request.body
        request_body = json.loads(request_body.decode('utf-8'))
        # if request_body:
        status_code, body, error = insert_data(request_body)
        # else:
        #     status_code, body, error = 204, {}, {}

        response = {
            'status_code': status_code,
            'body': body,
            'error': error
        }
        return JsonResponse(response)

    @csrf_exempt
    def patch(self, request, *args, **kwargs):
        request_body = request.body
        request_body = json.loads(request_body.decode('utf-8'))
        # if request_body:
        status_code, body, error = update_data(request_body)
        # else:
        #     status_code, body = 204, {}
        response = {
            'status_code': status_code,
            'body': body,
            'error': error
        }
        return JsonResponse(response)
