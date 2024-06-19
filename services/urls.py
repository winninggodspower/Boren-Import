from django.urls import path
from . import views

urlpatterns = [
    path('air_shipping', views.air_shipping, name='air_shipping'),
    path('fx_payment', views.fx_payment, name='fx_payment'),
    path('goods_procurement', views.goods_procurement, name='goods_procurement'),
    path('product_consultation', views.product_consultation, name='product_consultation'),
    path('product_sourcing', views.product_sourcing, name='product_sourcing'),
    path('sea_shipping', views.sea_shipping, name='sea_shipping'),
]
