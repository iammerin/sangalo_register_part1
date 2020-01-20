from django.urls import path
from . import views


urlpatterns = [
    # path('suburbs/', views.SuburbNameList.as_view()),
    path('new/', views.NewStateList.as_view()),
    path('postal/', views.PostalCode.as_view()),
    path('', views.InformationList.as_view()),
    path('state/', views.StateList.as_view()),
]