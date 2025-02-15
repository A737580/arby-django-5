from django.urls import path
from myapp.views import (
    add_item,
    update_item,
    # delete_item,
    index,
    # ProductListView,
    ProductDeleteView,
    PaymentSuccessView,
    PaymentFailedView,
    ProductDetailView)

app_name = 'myapp'

urlpatterns = [
    path('', index, name='index'),
    # path('', ProductListView.as_view(), name='index'),


    # path('<int:my_id>/', indexItem, name='detail'),
    path('<int:pk>/', ProductDetailView.as_view(), name='detail'),


    path('additem/', add_item, name='add_item'),
    path('updateitem/<int:my_id>/', update_item, name='update_item'),


    # path('deleteitem/<int:my_id>/', delete_item, name='delete_item'),
    path('deleteitem/<int:pk>/', ProductDeleteView.as_view(), name='delete_item'),
    path('success/', PaymentSuccessView.as_view(), name='success'),
    path('failed/', PaymentFailedView.as_view(), name='failed'),
    path('api/checkout-session/<int:id>', update_item, name='api_checkout_session'),

]