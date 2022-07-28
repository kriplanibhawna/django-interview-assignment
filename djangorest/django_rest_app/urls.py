from . import views
from django.urls import path
from .views import *

urlpatterns = [
    path("view/", views.ListBookAPIView.as_view(), name="books_list"),
    path("create/", views.CreateBookAPIView.as_view(), name="books_create"),
    path("update/<int:pk>/", views.UpdateBooksAPIView.as_view(), name="update_books"),
    path("delete/<int:pk>/", views.DeleteBookAPIView.as_view(), name="delete_books"),
    path("view_member/", views.ListMemberAPIView.as_view(), name="members_list"),
    path("create_member/", views.CreateMemberAPIView.as_view(), name="members_create"),
    path("update_member/<int:pk>/", views.UpdateMemberAPIView.as_view(), name="update_members"),
    path("delete_member/<int:pk>/", views.DeleteMemberAPIView.as_view(), name="delete_members"),
    path('api/register', RegisterApi.as_view()),
    path('login/', UserLoginView.as_view(), name='login'),

]
