from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "home.html",)

def our_firm(request):
    return render(request, "our-firm.html",)

def investment_model(request):
    return render(request, "investment-model.html",)

def investment_values(request):
    return render(request, "investment-values.html",)

def ethical_investing(request):
    return render(request, "ethical-investing.html",)

def technology_innovation(request):
    return render(request, "technology_and_innovation.html",)
