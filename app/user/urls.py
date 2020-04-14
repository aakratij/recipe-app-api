from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'user'

urlpatterns = [
    path('create/' , views.CreateUserView.as_view() , name='create'),
    path('token/',views.CreateTokenView.as_view() , name='token'),
]
