from django.urls import path
from .views import feeds, comment_add, comment_delete, post_add

#동적URL -> 복잡해질 수록 URL관리가 안되기에 제작
app_name = "posts"

urlpatterns = [
    path("feeds/", feeds, name = "feeds"),
    path("comment_add/", comment_add, name = "comment_add"),
    # views에서 comment = Comment.obejcts.get(id = comment_id)
    # 이렇게 받아주기 때문에 comment_id를 사용하는 것이다.
    path("comment_delete/<int:comment_id>/",comment_delete, name = "comment_delete"),
    path("post_add/", post_add, name = "post_add")
]
