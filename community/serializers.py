from rest_framework import serializers

from django.contrib.auth import get_user_model

from .models import Post, Comment
from accounts.serializers import UserSimpleInfoSerializer

# 게시글 일부 직렬화
class PostListSerializer(serializers.ModelSerializer):

    user = UserSimpleInfoSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'category', )

# 게시글 시리얼라이저
class PostSerializer(serializers.ModelSerializer):
    
    # 댓글
    class CommentDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = '__all__'

    # 작성자
    user = UserSimpleInfoSerializer(many=True, read_only=True)
    # 좋아요
    like_users = UserSimpleInfoSerializer(many=True, read_only=True)
    # 댓글
    comments = CommentDetailSerializer(many=True, read_only=True)    # 읽기 전용, 댓글 개수 0개 이상.
    # 좋아요 개수
    num_of_likes = serializers.SerializerMethodField()
    # 댓글 개수 필드
    num_of_comments = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'

    def get_num_of_comments(self, obj):    
        return obj.num_of_comments    
    
    def get_num_of_likes(self, obj):
        return obj.num_of_likes



# 전체 댓글 시리얼라이저
class CommentSerializer(serializers.ModelSerializer):
    # 게시글 시리얼라이저
    class PostTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Post
            fields = ('id', 'title', )

    # 게시글
    post = PostTitleSerializer(many=True, read_only=True)
    # 작성자
    user = UserSimpleInfoSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'

    