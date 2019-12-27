from django.urls import path

from .views import CacheView

urlpatterns = [
    path('', CacheView.as_view(), name='values'),
]
