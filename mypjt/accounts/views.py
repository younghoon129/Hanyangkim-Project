# accounts/views.py
from django.shortcuts import render

from allauth.socialaccount.providers.kakao import views as kakao_view
from allauth.socialaccount.providers.google import views as google_view
from allauth.socialaccount.providers.naver import views as naver_view
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView

class KakaoLogin(SocialLoginView):
    adapter_class = kakao_view.KakaoOAuth2Adapter
    client_class = OAuth2Client
    callback_url = 'http://localhost:8080/login/callback/' # 프론트엔드 콜백 주소와 반드시 일치

# 구글 로그인 뷰
class GoogleLogin(SocialLoginView):
    adapter_class = google_view.GoogleOAuth2Adapter
    client_class = OAuth2Client
    callback_url = 'http://localhost:8080/login/callback/'

# 네이버 로그인 뷰
class NaverLogin(SocialLoginView):
    adapter_class = naver_view.NaverOAuth2Adapter
    client_class = OAuth2Client
    callback_url = 'http://localhost:8080/login/callback/'

# Django 테스트 용
# Create your views here.
def index(request):
    return render(request, 'accounts/index.html')

