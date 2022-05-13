from django.urls import path, include
from .views import MessageCreate

urlpatterns = [
    path('create/', MessageCreate.as_view() , name='post-message'),
]
