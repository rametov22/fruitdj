from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path(' ', ShopView.as_view(), name='shop'),
    path('cart/', view_cart, name='view_cart'),
    path('update_quantity/', update_quantity, name='update_quantity'),
    path('remove_from_cart/', remove_from_cart, name='remove_from_cart'),
    path('add/<str:product_type>/<int:product_id>/', AddToCartView.as_view(), name='add_to_cart'),
    path('checkout/', checkout, name='checkout'),
]
