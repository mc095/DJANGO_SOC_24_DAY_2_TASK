from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from courses.models import Course

def courses_details(request):
    template = loader.get_template('courses.html')
    
    courses_list = Course.objects.all().values()
    context = {
        'courses_list' : courses_list,
    }
    
    return HttpResponse(template.render(context, request))