from django.urls import path
from . import views
from .views import  UserForgotPasswordView, UserPasswordResetConfirmView
urlpatterns = [
    path('auth/', views.auth, name='auth'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.log_out, name='log_out'),
    path('password-reset/', UserForgotPasswordView.as_view(), name='password_reset'),
    path('set-new-password/<uidb64>/<token>/', UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('', views.home, name='home'),
    path('chekmessage/', views.chekmessage, name='chekmessage'),
    path('successmessage/', views.successmessage, name='successmessage'),
    
]