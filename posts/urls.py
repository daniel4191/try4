from django.urls import path
from .views import feeds, comment_add, comment_delete, post_add

urlpatterns = [
    path("feeds/", feeds),
    path("comment_add/", comment_add),
    # views에서 comment = Comment.obejcts.get(id = comment_id)
    # 이렇게 받아주기 때문에 comment_id를 사용하는 것이다.
    path("comment_delete/<int:comment_id>/",comment_delete),
    path("post_add/", post_add)
]
