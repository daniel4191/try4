from django.db import models

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(
        "arm.User", # users가 아니라 arm일 수도 있을것 같다. 어디의 users일까? models안의 파라미터일까?
        # 앱.그 앱의 models에 정의 되어있는 클래스
        verbose_name= "작성자",
        on_delete=models.CASCADE,
    )
    content = models.TextField("내용")
    created = models.DateTimeField("생성일시", auto_now_add=True)
    
    def __str__(self):
        return self.content[:20]
    
class PostImage(models.Model):
    post = models.ForeignKey(
        Post,
        verbose_name="포스트",
        on_delete=models.CASCADE
    )    
    photo = models.ImageField("사진", upload_to="post")

class Comment(models.Model):
    user = models.ForeignKey(
        "arm.User",
        verbose_name="작성자",
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(Post, verbose_name="포스트", on_delete=models.CASCADE)
    content = models.TextField("내용")
    created = models.DateTimeField("생성일시",auto_now_add=True)
    