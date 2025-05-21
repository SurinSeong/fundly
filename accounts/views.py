import urllib.parse

from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


from .serializers import UserSignupSerializer, UserLoginSerializer, UserProfileSerializer
from .utils import get_access_token, get_user_info, generate_jwt_for_user, get_or_create_social_user

GOOGLE_CLIENT_ID = settings.GOOGLE_CLIENT_ID
KAKAO_CLIENT_ID = settings.KAKAO_CLIENT_ID

# 회원가입하기 - 일반 이메일 가입
@api_view(['POST'])
def signup(request):
    if request.method == 'POST':
        serializer = UserSignupSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)


# 기본 로그인
@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            auth_login(request, user)
            return Response(status=status.HTTP_202_ACCEPTED)
        
    return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

# 로그아웃
def logout(request):
    auth_logout(request)
    return Response(status=status.HTTP_200_OK)


# 소셜 로그인
@api_view(['GET'])
def social_login(request, provider):
    redirect_uri = f'http://127.0.0.1:8000/api/auth/{provider}/callback/'

    if provider == 'google':
        client_id = GOOGLE_CLIENT_ID    # 클라이언트 ID 받기
        scope = 'openid email profile'
        response_type = 'code'    # 인가 코드 응답 요청

        google_auth_url = (
            'https://accounts.google.com/o/oauth2/v2/auth?' + 
            urllib.parse.urlencode({
                'client_id': client_id,
                'redirect_uri': redirect_uri,
                'response_type': response_type,
                'scope': scope,
                'prompt': 'select_account',
            })
        )

        return redirect(google_auth_url)
    
    if provider == 'kakao':
        client_id = KAKAO_CLIENT_ID
        response_type = 'code'
        scope = 'openid'

        kakao_auth_url = (
            'https://kauth.kakao.com/oauth/authorize?' + 
            urllib.parse.urlencode({
                'response_type': response_type,
                'client_id': client_id,
                'redirect_uri': redirect_uri,
                'scope': scope,
                'prompt': 'select_account',
            })
        )

        return redirect(kakao_auth_url)


# # 소셜 로그아웃
# @api_view(['POST'])
# def social_logout(request, provider):
#     url = 'https://kapi.kakao.com/v1/user/logout'

#     get_access_token()

# 콜백 함수
@api_view(['GET', 'POST'])
def callback(request, provider):
    code = request.data.get('code') or request.GET.get('code')
    if not code:
        return Response({'error': 'No code provided'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        # 소셜 로그인 토큰 요청
        access_token = get_access_token(code, provider)
        # 사용자 정보 요청
        email, social_id = get_user_info(access_token, provider)
        # 생성하거나 존재하는 정보 가져오거나
        user = get_or_create_social_user(provider, social_id, email)
        # JWT 토큰 생성
        tokens = generate_jwt_for_user(user)

        return Response(tokens, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)