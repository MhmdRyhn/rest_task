import json

from django.core.cache import cache
from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings


class CacheView(View):
    def get(self, request, *args, **kwargs):
        # cache.set()
        response = {
            'status_code': 200,
            'status': 'success',
            'request_type': 'get',
            'ttl': settings.CACHE_TTL
        }
        if request.GET.get('keys'):
            response['query_params'] = request.GET.get('keys')
        return JsonResponse(response)

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body.decode('utf-8'))
        print(data, type(data))
        return JsonResponse({
            'status_code': 200,
            'status': 'success',
            'request_type': 'post'
        })


    @csrf_exempt
    def patch(self, request, *args, **kwargs):
        return JsonResponse({
            'status_code': 200,
            'status': 'success',
            'request_type': 'patch'
        })

