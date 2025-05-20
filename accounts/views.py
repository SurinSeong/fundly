import urllib.parse

from django.conf import settings
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer
from .utils import get_access_token, get_user_info, generate_jwt_for_user, get_or_create_social_user

GOOGLE_CLIENT_ID = settings.GOOGLE_CLIENT_ID

# 회원가입하기 - 일반 이메일 가입
@api_view(['POST'])
def signup(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)


# 기본 로그인
@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            auth_login(request, serializer.data)
            return Response(status=status.HTTP_202_ACCEPTED)
    return Response(status=status.HTTP_406_NOT_ACCEPTABLE)


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
    

# 콜백 함수
@api_view(['GET'])
def callback(request, provider):
    code = request.GET.get('code')
    if not code:
        return Response({'error': 'No code provided'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        # 소셜 로그인 토큰 요청
        access_token = get_access_token(code)
        # 사용자 정보 요청
        email, social_id = get_user_info(access_token)
        # 생성하거나 존재하는 정보 가져오거나
        user = get_or_create_social_user(provider, social_id, email)
        # JWT 토큰 생성
        tokens = generate_jwt_for_user(user)

        return Response(tokens, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)