from django.shortcuts import render, redirect
from .models import LaunchedGovProjects
from django.contrib import messages
from .forms import LaunchedGovProjectForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import LaunchedGovProjects
from django.contrib.auth.models import User


def projects_homepage(request):
    return render(request, 'project/homepage.html')


def report_project(request):
    if request.method == 'POST':
        form = LaunchedGovProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects:homepage')
    else:
        form = LaunchedGovProjectForm()
    return render(request, 'project/report_project.html', {'form': form})

def view_reported_projects(request):
    projects = LaunchedGovProjects.objects.all()
    return render(request, 'project/view_reported_projects.html', {'projects': projects})

@login_required
def track_project(request, project_id):
    project = get_object_or_404(LaunchedGovProjects, id=project_id)
    user = request.user
    
    if project not in user.tracked_projects.all():
        project.tracked_by.add(user)
        messages.success(request, f'Project "{project.project_title}" has been added to your tracked projects.')
    else:
        messages.info(request, f'You are already tracking the project: {project.project_title}')
    
    return redirect('projects:reported_projects')

def project_details(request, project_id):
    project = get_object_or_404(LaunchedGovProjects, id=project_id)
 
    return render(request, 'project/project_detail.html', {'project': project})

@login_required
def tracked_projects(request):
    user = request.user
    tracked_projects = user.tracked_projects.all()
    return render(request, 'project/tracked_projects.html', {'tracked_projects': tracked_projects})


def view_contract(request, project_id):
    project = get_object_or_404(LaunchedGovProjects, id=project_id)
    return render(request, 'project/view_contract.html', {'project': project})
