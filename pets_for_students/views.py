from django.shortcuts import render
from django.http import HttpResponse
from pets_for_students.models import Student


def index(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'pets_for_students/index.html', context=context_dict)

def pets(request):
    return render(request, 'pets_for_students/pets.html')



# Create your views here.
