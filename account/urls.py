from django.urls import path
from .views import login_user, logout_user, register_account

urlpatterns = [
    path('register/', register_account, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]
