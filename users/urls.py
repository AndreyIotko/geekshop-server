from django.urls import path
from users.views import RegistrationView, LoginUserView, ProfileUserView, UserLogoutView, verify

app_name = 'users'

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('profile/<int:pk>/', ProfileUserView.as_view(), name='profile'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('verify/<str:email>/<str:activation_key>/', verify, name='verify'),
]
