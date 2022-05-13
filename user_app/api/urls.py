from django.urls import path, include

from rest_framework.authtoken.views import obtain_auth_token

from .views import Logout

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('logout/', Logout.as_view() , name='logout'),
]
