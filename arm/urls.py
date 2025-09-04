from django.urls import path
from .views import login_view, logout_view, signup

#동적 URL 생성을 위한 요소
app_name = "users"

urlpatterns = [
    path("logout/", logout_view, name = "logout"),
    path("signup/", signup, name = "signup"),
    path("login2/", login_view, name = "login")
]
