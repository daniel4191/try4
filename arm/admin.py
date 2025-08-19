from django.contrib import admin
# 이 클래스는 어드민 창에서 유저관리를 하기 편리지는 것이다.
from django.contrib.auth.admin import UserAdmin

from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {
            "fields": (
                "username", "password"
            ),
        }),
        ("개인정보", {"fields": ("last_name","first_name",  "email")}),
        ("추가필드", {"fields": ("profile_image", "short_description")}),
        ("권한",{"fields": ("is_active", "is_staff", "is_superuser")}),
        ("중요한 일정", {"fields":("last_login", "date_joined")}),
    )
    