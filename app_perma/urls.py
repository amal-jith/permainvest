from django.urls import path
from . import views


app_name = "app_perma"

urlpatterns = [
    path('', views.home, name='home'),
    path('our-firm', views.our_firm, name='our_firm'),
    path('investment-model', views.investment_model, name='investment_model'),
    path('investment-values', views.investment_values, name='investment_values'),
    path('ethical-investing', views.ethical_investing, name='ethical_investing'),
    path('technology-and-innovation-commitment', views.technology_innovation, name='technology_innovation'),
]
