from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # 나중에 티어나 프로필 이미지가 필요하면 여기에 필드를 추가하면 됩니다.
    # 지금은 일단 비워두고 상속만 받아도 충분합니다.
    pass