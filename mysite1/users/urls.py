from django.urls import path
from .views import register, profile, logout_view,seller_profile
from django.contrib.auth.views import LoginView, LogoutView


app_name = 'users'

urlpatterns = [
    #http://127.0.0.1:8000/myapp/
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile, name='profile'),
    path('sellerprofile/<int:id>/', seller_profile, name='sellerprofile'),

]