from django.urls import path
from shoppingapp import views
from . import views
app_name='shoppingapp'
urlpatterns=[
       path('',views.AllProductCat,name='AllProductCat'),
       path('<slug:c_slug>/',views.AllProductCat,name='products_by_category'),
       path('<slug:c_slug>/<slug:product_slug>/',views.ProductDetail,name='ProductCatDetail')
]
