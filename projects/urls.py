from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'projects'

urlpatterns = [
    path('homepage/', views.projects_homepage, name='homepage'),
    path('report-project/', views.report_project, name='report_project'),
    path('view-reported-projects/', views.view_reported_projects, name='reported_projects'),
    path('track-project/<int:project_id>/', views.track_project, name='track_project'),
    path('project-details/<int:project_id>/', views.project_details, name='project_details'),
    path('tracked-projects/', views.tracked_projects, name='tracked_projects'),
    path('view-contract/<int:project_id>/', views.view_contract, name='view_contract'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)