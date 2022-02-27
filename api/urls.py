from django.urls import path
from . import views

urlpatterns = [
    path('', views.MachineListView.as_view()),
    path('<int:pk>/', views.MachineDetailView.as_view()),
]
