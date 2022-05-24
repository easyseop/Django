
from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('',views.home),
    path('product/',include('product.urls')),
    path('board/',include('board.urls')),
]
    
# 상품 관련 url
    # 127.0.0.1:8000/products/1
    # 127.0.0.1:8000/products/2
    # 127.0.0.1:8000/products/3
    # 127.0.0.1:8000/products/abc


# 구매 후기 url
    # 127.0.0.1:8000/boards/1
    # 127.0.0.1:8000/boards/2
    # 127.0.0.1:8000/boards/3
    # 127.0.0.1:8000/boards/abc






# url을 관리하는 파일 

# www.naver.com 

# 로그인 화면을 나타내는 도메인
# www.naver.com/login 

# 결제 화면을 나타내는 도메인
# www.naver.com/payment

