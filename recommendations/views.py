from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from accounts.serializers import UserProfileSerializer

# 추천 요청 + 결과 조회 함수
@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticatedOrReadOnly])
def ask_recommendation(request):
    user = request.user
    if request.method == 'PUT':
        serializer = UserProfileSerializer(user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()    # 새로운 정보 추가해서 저장하기
            # 추천 해주기 - 추천 함수 필요함
            # 사용자 정보 + 목표 설정 상품 정보와 유사도 비교해서 비슷한 거 3개 추천해주는 알고리즘 만들기
            result = 'serializer 넣어서 보여주기'
            return Response({'result': result}, status=status.HTTP_201_CREATED)
