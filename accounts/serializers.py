from rest_framework import serializers

from django.contrib.auth import get_user_model, authenticate


# 회원 가입을 위한 시리얼라이저
class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'
        
    def create(self, validated_data):
        username = validated_data.get('username')
        email = validated_data.get('email')
        nickname = validated_data.get('nickname')
        password = validated_data.get('password')
        age = validated_data.get('age')
    

# 로그인을 위한 시리얼라이저
class UserLoginSerializer(serializers.Serializer):

    username = serializers.CharField(required=True)    # 이메일, 유저네임 둘다 받게 하자
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        # 사용자 인증
        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError('아이디 (또는 이메일) 또는 비밀번호가 올바르지 않습니다.')
        
        if not user.is_acitve:
            raise serializers.ValidationError("비활성화된 계정입니다.")
        
        data['user'] = user

        return data



# 프로필 시리얼라이저
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'


# 유저 시리얼라이저 >> 커뮤니티 전용
class UserSimpleInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'nickname', )