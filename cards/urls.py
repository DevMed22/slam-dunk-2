from django.urls import  path
from .views import CreateCardView,ListCardView


urlpatterns = [
    path('create/',CreateCardView.as_view(),name='create_card'), 
    path('',ListCardView.as_view(),name='list_card'),
]