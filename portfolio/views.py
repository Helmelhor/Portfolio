from django.shortcuts import render
from .dados import habilidade

# Create your views here.
def home(request):
    return render(request, "home.html", {"habilidade": habilidade})
