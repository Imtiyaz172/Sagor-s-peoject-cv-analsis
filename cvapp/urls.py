from django.urls import path
from . import views 

urlpatterns = [
     
    path('',views.index),
    path('home',views.index2),
    path('cv-create',views.cvcreate),
    path('post',views.postjob),
    path('org-login',views.org_login),
    path('org-logout',views.org_logout),
    path('shortlist/<int:id>', views.shortlist_email),
    path('short-list/',views.shortlist_job),
    path('interview/<int:id>/', views.interviewlist),
    path('interview/',views.interview),
    path('org-reg',views.org_reg),
    path('applicant-login',views.applicant_login),
    path('applicant-logout',views.applicant_logout),
    path('job-list',views.jobpost),
    path('applicant-list/<int:id>/',views.applicationlist),
    path('short-list/<int:id>/',views.shortlist_application),
    path('short-list-mail/<int:id>/',views.interview_email),
    path('job-list/<str:category>/',views.category_post),
    path('job-list/<str:category>/<int:id>/',views.post_details),



]
