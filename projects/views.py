from django.shortcuts import render
from .models import Project
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})

# Create your views here.
