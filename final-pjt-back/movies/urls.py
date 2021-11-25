from django.urls import path
from . import views
from . import algo_views
app_name = 'movies'

urlpatterns = [
    path('', views.movie_list, ),
    path('latest/', views.movie_latest, ),
    path('upcoming/', views.movie_upcoming, ),
    path('popular/', views.movie_popular, ),
    path('top_rated/', views.movie_top_rated, ),
    path('recmovie/', algo_views.recmovie, ),
    path('premiumrecmovie/', algo_views.premiumrecmovie, ),
 
    path('casemovie/', views.casemovie, ),
    path('givemovieid/<int:movie_id>/', views.givemovieid, ),
    path('search/<str:what>/<str:searchvalue>/', algo_views.search),

  

    # path('login/', views.login, name='login'),
    # path('logout/', views.logout, name='logout'),
]
