from rest_framework import serializers

from django.contrib.auth import get_user_model

from .utils import generate_jwt_for_user

User = get_user_model()

# 회원 가입을 위한 시리얼라이저
class UserSignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'nickname', 'email', 'password', )
        extra_kwargs = {
            'password': {
            'style': {
                'input_type': 'password'
                },
            }
        }
        
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
        

# 로그인을 위한 시리얼라이저
class UserLoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'password', )
        extra_kwargs = {
            'email': {
                'validators': [],    # 유효성 검사 제거하기
                'style': {
                    'input_type': 'email',
                }
            },
            'password': {
                'style': {
                    'input_type': 'password',
                }
            }
        }

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)

            if not user.check_password(password):
                raise serializers.ValidationError('잘못된 비밀번호 입니다.')
        
        else:
            raise serializers.ValidationError("존재하지 않는 사용자 입니다.")
        
        jwt = generate_jwt_for_user(user)
        refresh = jwt.get('refresh')
        access = jwt.get('access')

        data = {
            'user': user,
            'refresh': refresh,
            'access': access,
        }

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