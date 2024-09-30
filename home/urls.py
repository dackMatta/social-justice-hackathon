from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name='home'

urlpatterns=[
    path('',views.home, name='home'),
    path('report/',views.submit_case_form, name='report'),
    path('raised_cases/',views.raised_cases, name='raised_cases'),  
    path('case_detail/<int:case_id>/',views.case_detail, name='case_detail'),
    path('lawyers/',views.lawyers, name='lawyers'),
    path('assign_case/<int:case_id>/',views.assign_case, name='assign_case'),
    path('login/',views.user_login, name='login'),
    path('register/',views.register, name='register'),
    path('logout/',views.user_logout, name='logout'),
    path('profile/',views.profile, name='profile'),
    path('track_case/<int:case_id>/',views.track_case, name='track_case'),
    path('tracked_cases/',views.tracked_cases, name='tracked_cases'),
    path('lawyer_chat/<int:lawyer_id>/',views.send_message, name='lawyer_chat'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
