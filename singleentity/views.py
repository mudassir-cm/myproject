from django.shortcuts import render, redirect

from singleentity.form import PersonForm
from singleentity.models import Person

def home(request):
    return render(request, 'singleentity/home.html', {'pagetext': 'single crud Home Page'})

def peronshow(request):
    list = Person.objects.all()
    return render(request, 'singleentity/personshow.html', {'list': list})

def personadd(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        form.save()
        return redirect('/singleentity/person/show')
    else:
        form = PersonForm
        return render(request, 'singleentity/personadd.html', {'form': form})

def personupdate(request, id):
    if request.method == 'POST':
        p = Person.objects.get(id=id)
        person = PersonForm(request.POST, instance=p)
        person.save()
        return redirect('/singleentity/person/show')
    else:
        person = Person.objects.get(id=id)
        return render(request, 'singleentity/personupdate.html', {'person': person})

def persondelete(request, id):
    p = Person.objects.get(id = id)
    p.delete()
    return redirect('/singleentity/person/show')

def personview(request, id):
    person = Person.objects.get(id = id)
    return render(request, 'singleentity/personview.html', {'person': person})






# Create your views here.
