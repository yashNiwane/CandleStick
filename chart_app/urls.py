from django.urls import path
from . import views

urlpatterns = [
    path('', views.candlestick_chart, name='candlestick_chart'),
]