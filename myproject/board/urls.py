from django.urls import URLPattern, path
from board import views

urlpatterns = [

    path('',views.board),
    path('first/',views.boardfirst),






]