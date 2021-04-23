from django.shortcuts import render

def home(request):
    return render(request, 'myapp/home.html', {'hometext': 'Home Pag'})

# Create your views here.
