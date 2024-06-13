from django.shortcuts import render

# Create your views here.
def home(request):
    # Lógica de la vista
    return render(request, 'home.html')