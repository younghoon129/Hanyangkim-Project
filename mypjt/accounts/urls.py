from django.urls import path
from . import views
from .views import KakaoLogin, GoogleLogin, NaverLogin

urlpatterns = [
    # 프론트엔드에서 axios.post('.../kakao/') 로 요청을 보냅니다.
    path('kakao/login/', KakaoLogin.as_view(), name='kakao_login_api'),
    path('google/login/', GoogleLogin.as_view(), name='google_login_api'),
    path('naver/login/', NaverLogin.as_view(), name='naver_login_api'),
]