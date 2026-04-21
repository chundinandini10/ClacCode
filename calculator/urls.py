from django.urls import path
from .views import CalculateView, HomeView, CalculatorGUIView

urlpatterns = [
    path('', CalculatorGUIView.as_view(), name='gui'),
    path('info/', HomeView.as_view(), name='home'),
    path('calculate/', CalculateView.as_view(), name='calculate'),
]
