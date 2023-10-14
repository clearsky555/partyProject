from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from apps.users import views as user_views
from apps.party import views as party_views


urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', user_views.CreateUserAPIView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('newparty/', party_views.CreatePartyView.as_view()),
]