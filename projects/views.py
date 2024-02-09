from django.shortcuts import render
from .models import Project

def projects(request):
    projects_list = Project.objects.order_by('-date_created')
    return render(request, 'projects/projects.html', {'projects': projects_list})