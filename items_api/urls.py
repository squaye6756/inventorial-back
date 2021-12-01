from django.urls import path
from . import views

urlpatterns = [
    path('api/items', views.ItemList.as_view(), name='item_list'),
    path('api/items/<int:pk>', views.ItemDetail.as_view(), name='item_detail')
]
