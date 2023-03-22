from django.shortcuts import render

# Create your views here.
context = {}

def index(request):
    return render(request, 'index.html', context)
