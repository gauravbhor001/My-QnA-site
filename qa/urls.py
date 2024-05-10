from django.urls import path
from . import views
from .views import home_redirect_view

urlpatterns = [
    path('', views.question_list, name='question_list'),
    path('<int:question_id>/', views.question_detail, name='question_detail'),
    path('create/', views.question_create, name='question_create'),
    path('register/', views.register, name='register'),  # Path for user registration.
    path('user/<int:user_id>/', views.user_question_list, name='user_question_list'),  # Questions by a specific user
    path('delete_question/<int:question_id>/', views.delete_question, name='delete_question'),  # Delete question path


]
