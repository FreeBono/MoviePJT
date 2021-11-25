from django.urls import path
from . import views

from rest_framework_jwt.views import obtain_jwt_token

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('api-token-auth/', obtain_jwt_token),
    path('userlist/',views.userlist),
    path('userpoint/',views.userpoint),
    path('profile/<str:username>/',views.profile),
    path('follow/',views.follow),
    
]
