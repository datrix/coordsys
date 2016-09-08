from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import student

# Create your views here.

def index(request):
    all_students = student.objects.all()
    template = loader.get_template('student/index.html')
    context = {
      'all_students': all_students,
    }
    return HttpResponse(template.render(context, request));
  
def detail(request, zID):
    return HttpResponse("<h2> Details for Student: " + str(zID) + "</h2>")
  
def get_event (request, calendar):
    return calendar.event_set.all()
