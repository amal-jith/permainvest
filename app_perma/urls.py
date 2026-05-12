from django.urls import path
from . import views


app_name = "app_perma"

urlpatterns = [
    path('', views.home, name='home'),
    path('our-firm', views.our_firm, name='our_firm'),
    path('investment-model', views.investment_model, name='investment_model'),
]