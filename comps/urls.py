from django.urls import path
from .views import comps, result

urlpatterns = [
    path('', comps, name='comps'),
    path('result/', result, name='result'),
]
