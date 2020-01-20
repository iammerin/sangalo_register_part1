from django.urls import path
from . import views


urlpatterns = [
    path('', views.InformationList.as_view()),
    # path('okay/', views.InformationList1.as_view()),
]