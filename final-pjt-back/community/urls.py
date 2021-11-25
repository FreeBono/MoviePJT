from django.urls import path
from . import views



app_name = 'community'

urlpatterns = [
    path('review/', views.review, name='review'),
    path('review/<int:review_id>/comment/', views.comment, ),
    path('review/<int:review_id>/', views.reviewrevise, ),
    path('comment/<int:comment_id>/', views.commentrevise, ),
    path('like/', views.like, ),
    path('reviewking/', views.reviewking)
  
    
    # ${SERVER_URL}/community/reviewall/`

  
    # path('logout/', views.logout, name='logout'),
]
# url: `${SERVER_URL}/community/comment/${commentId}`,