from django.shortcuts import render, get_object_or_404
from django.contrib.auth import logout, login
from rest_framework import views, response
from rest_framework.status import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from .models import *
from .serializers import *
from main.serializers import *

# Create your views here.

class SignUpView(views.APIView):
    serializer_class = SignUpSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': '회원가입 성공', 'data': serializer.data}, status=HTTP_201_CREATED)
        return Response({'message': '회원가입 실패', 'data': serializer.errors}, status=HTTP_400_BAD_REQUEST)

class LoginView(views.APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            return Response({'message': "로그인 성공", 'data': serializer.validated_data}, status=HTTP_200_OK)
        return Response({'message': "로그인 실패", 'data': serializer.errors}, status=HTTP_400_BAD_REQUEST)

class ProfileView(views.APIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    # def get(self, request, format=None):
    #     serializer = ProfileSerializer(request.user)
    #     return Response({'message': '프로필 가져오기 성공', 'data': serializer.data}, status=HTTP_200_OK)

    # def put(self, request, format=None):
    #     serializer = ProfileSerializer(data=request.user)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'message': '프로필 가져오기 성공', 'data': serializer.data}, status=HTTP_200_OK)
    #     return Response(serializer.errors)

    def get(self, request, format=None):
        serializer = self.serializer_class(request.user)  # Assuming the profile is related to the user
        return Response({'message': '프로필 가져오기 성공', 'data': serializer.data}, status=HTTP_200_OK)

    def put(self, request, format=None):
        serializer = self.serializer_class(request.user, data=request.data, partial=True)  # Using request data to update the profile
        if serializer.is_valid():
            serializer.save()
            return Response({'message': '프로필 업데이트 성공', 'data': serializer.data}, status=HTTP_200_OK)
        return Response({'message': '프로필 업데이트 실패', 'data': serializer.errors}, status=HTTP_400_BAD_REQUEST)



class MyScrapedView(views.APIView):
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return user.scraped_posts.all()

    def get(self, request):
        scraped_posts = self.get_queryset()
        serializer = PostSerializer(scraped_posts, many=True)
        if scraped_posts.exists():
            serializer = PostSerializer(scraped_posts, many=True)
            return response.Response({'message': '내가 스크랩 한 포스트 조회 성공', 'data': serializer.data}, status=HTTP_200_OK)
        else:
            return response.Response({'message': '내가 스크랩 한 포스트가 없습니다.'}, status=HTTP_204_NO_CONTENT)
        
class MyPostedView(views.APIView):
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author=user)  # 사용자가 작성한 포스트만 필터링하여 반환

    def get(self, request):
        user_posts = self.get_queryset()
        if user_posts.exists():
            serializer = PostSerializer(user_posts, many=True)  # 댓글 시리얼라이저를 import하세요.
            return response.Response({'message': '내가 작성한 게시물 조회 성공', 'data': serializer.data}, status=HTTP_200_OK)
        else:
            return response.Response({'message': '내가 작성한 게시물이 없습니다.'}, status=HTTP_204_NO_CONTENT)

class MyCommentView(views.APIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Comment.objects.filter(author=user)  # 사용자가 작성한 댓글만 필터링하여 반환

    def get(self, request):
        user_comments = self.get_queryset()
        if user_comments.exists():
            serializer = CommentSerializer(user_comments, many=True)  # 댓글 시리얼라이저를 import하세요.
            return response.Response({'message': '내가 작성한 댓글 조회 성공', 'data': serializer.data}, status=HTTP_200_OK)
        else:
            return response.Response({'message': '내가 작성한 댓글이 없습니다.'}, status=HTTP_204_NO_CONTENT)

class MyRecommentView(views.APIView):
    serializer_class = RecommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Recomment.objects.filter(author=user)  # 사용자가 작성한 댓글만 필터링하여 반환

    def get(self, request):
        user_recomments = self.get_queryset()
        if user_recomments.exists():
            serializer = RecommentSerializer(user_recomments, many=True)  # 댓글 시리얼라이저를 import하세요.
            return response.Response({'message': '내가 작성한 대댓글 조회 성공', 'data': serializer.data}, status=HTTP_200_OK)
        else:
            return response.Response({'message': '내가 작성한 대댓글이 없습니다.'}, status=HTTP_204_NO_CONTENT)