from django.urls import path
from . import views

app_name = 'finatic'

urlpatterns = [
    path('', views.LustView.as_view(), name="list"),
    path('lustr/add', views.CreateLust.as_view(), name="create"),
    path('<slug:slug>/', views.LustDetail.as_view(), name="detail"),
    path('lustr/<slug:slug>/', views.UpdateLust.as_view(), name="update"),
    path('lustr/<slug:slug>/delete/', views.DeleteLust.as_view(), name="delete"),
]



