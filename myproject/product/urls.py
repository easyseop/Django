from django.urls import URLPattern, path
from product import views

urlpatterns = [
    path('',views.product),
    path('first/',views.productfirst),
]