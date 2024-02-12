from django.shortcuts import render
from .models import Project

def projects(request):
    # Default sorting is by date created in descending order
    sort_by = request.GET.get('sort', 'date_created')
    order = request.GET.get('order', 'desc')  # Get the order from the query parameters

    # A dictionary mapping sort options to model fields
    sort_options = {
        'date_created': 'date_created',
        'last_updated': 'last_updated',
        'technologies': 'technology',
    }
    
    sort_field = sort_options.get(sort_by, 'date_created')
    if order == 'asc':
        projects_list = Project.objects.order_by(sort_field)
    else:  # Default to descending if anything other than 'asc' is specified
        projects_list = Project.objects.order_by(f'-{sort_field}')
    
    return render(request, 'projects/projects.html', {'projects': projects_list})
