from django.shortcuts import render
from django.http import HttpResponse
from pets_for_students.models import Student
from pets_for_students.models import Cat


def index(request):
    students_list = Student.objects.order_by('last_name', 'first_name')
    cats_list = Cat.objects.order_by('name')


    context_dict = {}
    context_dict['boldmessage'] = 'bold!'
    context_dict['students'] = students_list
    context_dict['cats'] = cats_list
 

    

    return render(request, 'pets_for_students/index.html', context=context_dict)

def pets(request):
    cats_list = Cat.objects.order_by('name')

    context_dict={}
    context_dict['cats'] = cats_list
    return render(request, 'pets_for_students/pets.html', context=context_dict)




# Create your views here.
