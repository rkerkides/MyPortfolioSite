from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Project

def projects(request):
    # Default sorting is by date created in descending order
    sort_by = request.GET.get('sort', 'date_created')
    order = request.GET.get('order', 'desc')

    # Mapping sort options to model fields
    sort_options = {
        'date_created': 'date_created',
        'last_updated': 'last_updated',
        'technologies': 'technology',
    }

    # Adjusting sort field based on the provided order
    sort_field = sort_options.get(sort_by, 'date_created')
    if order == 'asc':
        projects_list = Project.objects.order_by(sort_field)
    else:  # Default to descending
        projects_list = Project.objects.order_by(f'-{sort_field}')
    
    # Setup paginator
    paginator = Paginator(projects_list, 6)  # 6 projects per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Pass the page_obj to the template, instead of projects_list
    return render(request, 'projects/projects.html', {'page_obj': page_obj})
