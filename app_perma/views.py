from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "home.html",)

def our_firm(request):
    return render(request, "our-firm.html",)

def investment_model(request):
    return render(request, "investment-model.html",)
