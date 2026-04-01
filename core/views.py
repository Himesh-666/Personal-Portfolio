from django.shortcuts import render
from .models import Skill

def home(request):
    skills = Skill.objects.all()
    return render(request, 'home.html', {'skills': skills})