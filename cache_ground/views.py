from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .services import get_data, save_or_update_data


class CacheView(View):
    def get(self, request, *args, **kwargs):
        query_param = request.GET.get('keys')
        status_code, response_body = get_data(query_param)

        response = {
            'status_code': status_code,
            'body': response_body
        }
        return JsonResponse(response)

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        request_body = request.body
        if request_body:
            status_code, body = save_or_update_data(request_body)
        else:
            status_code, body = 204, {}

        return JsonResponse({
            'status_code': status_code,
            'body': body
        })

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
