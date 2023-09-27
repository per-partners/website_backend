from django.urls import path
from .views import CareersList, CareersDetail

urlpatterns = [
    path('', CareersList.as_view()),
    path('<int:pk>', CareersDetail.as_view())
]
