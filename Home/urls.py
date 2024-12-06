from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('equipment/',views.equipment, name='equipment'),
    path('equipment/<int:product_id>/', views.product_page, name='product_page'),  # For individual product pages
]
