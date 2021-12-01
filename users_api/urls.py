from django.views.decorators.csrf import csrf_exempt
from . import views
from django.urls import path

urlpatterns = [
    path('api/users', views.UserList.as_view(), name='user_list'),
    path('api/users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('api/users/login', csrf_exempt(views.check_login), name="check_login")
]
