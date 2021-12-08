from django.urls import path
from . import views

urlpatterns = [
    path('api/stores', views.StoreList.as_view(), name='store_list'),
    path('api/stores/<int:pk>', views.StoreDetail.as_view(), name='store_detail')
]
