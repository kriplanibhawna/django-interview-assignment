from django.contrib.auth import authenticate
from requests import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from .serializers import *
from .models import *
from rest_framework import generics, permissions, status


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


# Register API
class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })


class UserLoginView(APIView):
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            username = serializer.data.get('username')
            password = serializer.data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({"token": token, "msg": "login success"}, status=status.HTTP_200_OK)
            else:
                return Response({'errors': {'non_field_errors': ['email and password are not valid']}},
                                status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListBookAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    """This endpoint list all of the available books from the database"""
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class CreateBookAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    """This endpoint allows for creation of a book"""
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class UpdateBooksAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    """This endpoint allows for updating a specific books by passing in the id of the book to update"""
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class DeleteBookAPIView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    """This endpoint allows for deletion of a specific book from the database"""
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


"""Members Views"""


class ListMemberAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    """This endpoint list all of the available Member from the database"""
    queryset = Members.objects.all()
    serializer_class = MemberSerializer


class CreateMemberAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    """This endpoint allows for creation of a Member"""
    queryset = Members.objects.all()
    serializer_class = MemberSerializer


class UpdateMemberAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    """This endpoint allows for updating a specific Members by passing in the id of the Member to update"""
    queryset = Members.objects.all()
    serializer_class = MemberSerializer


class DeleteMemberAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Member from the database"""
    queryset = Members.objects.all()
    serializer_class = MemberSerializer


