# 이 임포트는 admin단에서 썸네일 보여주기 위해서 필요
import admin_thumbnails

from django.contrib import admin
from django.db.models import ManyToManyField
from django.forms import CheckboxSelectMultiple

from .models import Post, PostImage, Comment, HashTag

# Register your models here.
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

@admin_thumbnails.thumbnail('photo')
class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1
    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "id", 
        "content"
    ]
    inlines = [
        CommentInline,
        PostImageInline
        ]
    
    # Post 변경 화면에서 ManyToManyField를 Checkbox로 출력
    formfield_overrides = {
        ManyToManyField: {"widget": CheckboxSelectMultiple}
    }
    
@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "post",
        "photo"
    ]
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "post",
        "content"
    ]

@admin.register(HashTag)
class HashTagAdmin(admin.ModelAdmin):
    pass