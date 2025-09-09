from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def students(request):
    students = [
        {
            'id': 1,
            'name': 'John Doe',
            'age': 20,
            'major': 'Computer Science'
        },
        {
            'id': 2,
            'name': 'Jane Smith',
            'age': 22,
            'major': 'Mathematics'
        }]
    return HttpResponse(students)