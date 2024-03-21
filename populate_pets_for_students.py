import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_cats.settings')

import django
django.setup()
from pets_for_students.models import Student, Cat

# For an explanation of what is going on here, please refer to the TwD book.

def populate():
    
    students_and_their_pets = [
        {'first_name': 'Alyssa', 'last_name': 'Croft', 'cats': ['Alex', 'Luna', 'Mittens']}, 
        {'first_name': 'John', 'last_name': 'Doe', 'cats': ['Muffins']}, 
        {'first_name': 'Azam', 'last_name': 'Khan', 'cats': ['Jill', 'Joe']} ]
    
    for person in students_and_their_pets:
        st = add_student(person['first_name'], person['last_name'])
        for each_cat in person['cats']:
            add_cat(st, each_cat)


def add_cat(student, name):
    c = Cat.objects.get_or_create(students=student, name=name)[0]
    c.save()
    return c

def add_student(first_name, last_name):
    s = Student.objects.get_or_create(first_name=first_name, last_name=last_name)[0]
    s.save()
    return s

# Start execution here!
if __name__ == '__main__':
    print('Starting Pets for Students population script...')
    populate()