from django.urls import path
from . import views

app_name = 'finatic'

urlpatterns = [
    path('', views.LustView.as_view(), name="list"),
    path('<slug:slug>/', views.LustDetail.as_view(), name="detail")
]

