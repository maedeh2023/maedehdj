from django.urls import path,re_path
from . import views

app_name='home'
urlpatterns=[
    path('',views.home,name='home'),
    path('product/', views.all_product, name='product'),
    path('detail/<int:id>/', views.product_detail, name='detail'),
    path('category/<slug>/<int:id>/', views.all_product, name='category'),
]