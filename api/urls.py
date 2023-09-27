from django.urls import path
from .views import PostDetail, PostList
from .models import MyCVS

urlpatterns = [
    path('posts/', PostList.as_view()),
    path('<int:pk>', PostDetail.as_view()),
    path('mycareers/', MyCVS.as_view()),
]
