from django.db import models
from django.conf import settings

# 게시글 모델
class Post(models.Model):
    # 작성자
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 좋아요 누른 사용자들
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    # 제목
    title = models.CharField(max_length=200)
    # 내용
    content = models.TextField()
    # 카테고리
    category = models.CharField(max_length=10)
    # 생성 날짜
    created_at = models.DateTimeField(auto_now_add=True)
    # 수정 날짜
    updated_at = models.DateTimeField(auto_now=True)


# 댓글 모델
class Comment(models.Model):
    # 작성자
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 게시글
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # 내용
    content = models.TextField()
    # 생성 날짜
    created_at = models.DateTimeField(auto_now_add=True)
    # 수정 날짜
    updated_at = models.DateTimeField(auto_now=True)