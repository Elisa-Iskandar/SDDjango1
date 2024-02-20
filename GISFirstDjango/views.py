from django.shortcuts import render
from .models import Person

def splash(request):
    name = 'Billy'
    people = Person.objects.all()
    debug_people = list(people)
    my_list = ['You', 'are', 'awesome']
    return render(request, "splash.html", {'name': name,'my_list': my_list})
