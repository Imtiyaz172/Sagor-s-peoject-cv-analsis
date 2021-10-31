from django.db.models.expressions import OrderBy
from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from django.db.models import Q,F
from django.http import HttpResponse
from .import models
import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from django.db.models import Q,F
from django.db.models import Sum
from .import models
import datetime
from django.core import serializers
import json
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import random, string, os
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.auth.decorators import login_required
import hashlib, socket



def index(request):

    return render(request,'web/index.html')

def index2(request):
    if not request.session['id']:
        return redirect('/org-login')
    user_post = models.jobpost.objects.filter(user_id = request.session['id'])
    context={
        'user_post':user_post,
    }

    return render(request,'admin_panel/myjoblist.html',context)


def shortlist_job(request):
    if not request.session['id']:
        return redirect('/org-login')
    user_post = models.jobpost.objects.filter(user_id = request.session['id'])
    context={
        'user_post':user_post,
    }

    return render(request,'admin_panel/myjoblist2.html',context)


def interview(request):
    if not request.session['id']:
        return redirect('/org-login')
    user_post = models.jobpost.objects.filter(user_id = request.session['id'])
    context={
        'user_post':user_post,
    }

    return render(request,'admin_panel/myjoblist3.html',context)


def interviewlist(request,id):
    if not request.session['id']:
        return redirect('/org-login')
    applicant = models.user_application.objects.filter(jobpost_id = id, interviewlist = True)
    context={
        'applicant':applicant,
    }
    return render(request,'admin_panel/interviewlist.html',context)


def shortlist_application(request,id):
    if not request.session['id']:
        return redirect('/org-login')
    applicant = models.user_application.objects.filter(jobpost_id = id, shortlist=True,interviewlist = False)
    if request.method == "POST":
        shortlist        = request.POST['shortlist']
        models.user_application.objects.filter(id = id).update(shortlist=True)
    context={
        'applicant':applicant,
    }
    return render(request,'admin_panel/shortlist.html',context)


def applicationlist(request,id):
    if not request.session['id']:
        return redirect('/org-login')
    applicant = models.user_application.objects.filter(jobpost_id = id, shortlist=False)
    if request.method == "POST":
        shortlist        = request.POST['shortlist']
        models.user_application.objects.filter(id = id).update(shortlist=True).order_by("skill_match")
    context={
        'applicant':applicant,
    }
    return render(request,'admin_panel/index2.html',context)



from django.core.mail import send_mail
from django.template.loader import render_to_string

def shortlist_email(request, id):
    models.user_application.objects.filter(id = id).update(shortlist=True)
    email = models.user_application.objects.filter(id = id).first()
    email1 = email.applicant.email
    send_mail(
        'You are in Shortlist',
        "Congrates you are our shortlist. we will contact you next to interview",
        settings.EMAIL_HOST_USER,
        [email1],
        fail_silently=False,
    )
    return redirect('/home')
    

def interview_email(request,id):
    models.user_application.objects.filter(id = id)
    email = models.user_application.objects.filter(id = id).first()
    email1 = email.applicant.email
    
    if request.method == "POST":
        subject        = request.POST['subject']
        message        = request.POST['message']
        subject1 = str(subject)
        message1 = str(message)
        send_mail(
            f'{subject1}',
            f'{message1}',
            settings.EMAIL_HOST_USER,
            [email1],
            fail_silently=False,
        )
        models.user_application.objects.filter(id = id).update(interviewlist=True)
        return redirect('/home')
    return render(request,'web/interview_mail.html')
    

def jobpost(request):
    if request.method == "POST":
        search        = request.POST['post_name']
        jobsearch    = models.jobpost.objects.filter( status=True, post_name__icontains = search)
        if jobsearch:
            return render(request, "web/Job_list.html",{ 'jobsearch' : jobsearch,})
        else:
            messages.warning(request, "No records found.Please try another")
    post = models.jobpost.objects.filter(status=True).order_by("-id")
    paginator = Paginator(post, 10) # Show 6 contacts per page

    page = request.GET.get('page')
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        post = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        post = paginator.page(paginator.num_pages)
    context={
        'post' : post,
    }
    return render(request,'web/Job_list.html',context)

def category_post(request,category):
    category        = category.replace('-', ' ')
    if request.method == "POST":
        search        = request.POST['post_name']
        jobsearch    = models.jobpost.objects.filter( status=True, post_name__icontains = search)
        if jobsearch:
            return render(request, "web/Job_list.html",{ 'jobsearch' : jobsearch,})
        else:
            messages.warning(request, "No records found.Please try another")
    
    post = models.jobpost.objects.filter(category_name_id__category_name = category,status=True).order_by("-id")
    paginator = Paginator(post, 10) # Show 6 contacts per page
    page = request.GET.get('page')
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        post = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        post = paginator.page(paginator.num_pages)
    context={
        'post' : post,
    }
    return render(request,'web/category_list.html',context)

def post_details(request,category,id):
    category        = category.replace('-', ' ')
    post = models.jobpost.objects.filter(category_name_id__category_name = category,id=id,status=True).first()
    
    if request.method == 'POST':
        expected_salary = request.POST.get('expected_salary')
        if not request.session['id']:
            return redirect('/applicant-login')
        if request.session.get('id'):
            models.user_application.objects.create(
                applicant_id = int(request.session['id']),
                jobpost_id = post.id,
                expected_salary = expected_salary,
            )

    context={
        'post' : post,
    }
    return render(request,'web/post_details.html',context)


def org_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = models.Organization.objects.filter(email = email,password = password).first()       
        if not user:
            messages.warning(request, "Wrong Information")
            return render(request,'web/org_login.html')
        request.session['id'] = user.id
        return redirect('/')
    return render(request,'web/org_login.html')


def org_reg(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        models.Organization.objects.create(
        email = email,
        password = password,
        )
        messages.warning(request, "Account Create Successfully")
        return redirect('/org-login')
    return render(request,'web/org_reg.html')

 
def org_logout(request):
    request.session['id'] = False
    return redirect('/')



def cvcreate(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        father_name = request.POST.get('father_name')
        mother_name = request.POST.get('mother_name')
        date_of_birth = request.POST.get('date_of_birth')
        national_id = request.POST.get('national_id')
        pasport_id = request.POST.get('pasport_id')
        birth_reg = request.POST.get('collection_time')
        same_as_present = True if request.POST.get('same_as_present') else False
        email = request.POST.get('email')
        password = request.POST.get('password')
        present_address = request.POST.get('present_address')
        present_district = request.POST.get('present_district')
        present_upazila = request.POST.get('present_upazila')
        present_post = request.POST.get('present_post')
        present_post_code = request.POST.get('present_post_code')
        mobile = request.POST.get('mobile')
        permanent_address = request.POST.get('permanent_address')
        permanent_district = request.POST.get('permanent_district')
        permanent_upazila = request.POST.get('permanent_upazila')
        permanent_post = request.POST.get('permanent_post')
        permanent_post_code = request.POST.get('permanent_post_code')
        ssc_roll = request.POST.get('ssc_roll')
        ssc_result = request.POST.get('ssc_result')
        hsc_result = request.POST.get('hsc_result')
        versity_result = request.POST.get('versity_result')
        ssc_year = request.POST.get('ssc_year')
        hsc_roll = request.POST.get('hsc_roll')
        hsc_year = request.POST.get('hsc_year')
        versity_roll = request.POST.get('versity_roll')
        versity_year = request.POST.get('versity_year')
        versity_duration = request.POST.get('versity_duration')
        company_name1 = request.POST.get('company_name1')
        company_business1 = request.POST.get('company_business1')
        company_designation1 = request.POST.get('company_designation1')
        company_department1 = request.POST.get('company_department1')
        company_responsibility1 = request.POST.get('company_responsibility1')
        company_emp_time1 = request.POST.get('company_emp_time1')
        company_location1 = request.POST.get('company_location1')
        company_experience1 = request.POST.get('company_experience1')
        company_name2 = request.POST.get('company_name2')
        company_business2 = request.POST.get('company_business2')
        company_designation2 = request.POST.get('company_designation2')
        company_department2 = request.POST.get('company_department2')
        company_responsibility2 = request.POST.get('company_responsibility2')
        company_emp_time2 = request.POST.get('company_emp_time2')
        company_location2 = request.POST.get('company_location2')
        company_experience2 = request.POST.get('company_experience2')
        image = ""
        if bool(request.FILES.get('image', False)) == True:
            file = request.FILES['image']
            image = "cv-image/"+file.name
            if not os.path.exists(settings.MEDIA_ROOT+"cv-image/"):
                os.mkdir(settings.MEDIA_ROOT+"cv-image/")
            default_storage.save(settings.MEDIA_ROOT+"cv-image/"+file.name, ContentFile(file.read()))

        gender = int(request.POST[('gender')])
        reletion_status = int(request.POST[('reletion_status')])
        religion = int(request.POST[('religion')])
        nationality = int(request.POST[('nationality')])
        ssc_board = int(request.POST[('ssc_board')])
        ssc_group = int(request.POST[('ssc_group')])
        hsc_board = int(request.POST[('hsc_board')])
        hsc_group = int(request.POST[('hsc_group')])
        versity = int(request.POST[('versity')])
        versity_group = int(request.POST[('versity_group')])

        models.applicant.objects.create(
        first_name = first_name,
        last_name = last_name,
        father_name = father_name,
        mother_name = mother_name,
        date_of_birth = date_of_birth,
        national_id = national_id,
        pasport_id = pasport_id,
        birth_reg = birth_reg,
        same_as_present = same_as_present,
        email = email,
        password = password,
        present_address = present_address,
        present_district = present_district,
        present_upazila = present_upazila,
        present_post = present_post,
        present_post_code = present_post_code,
        mobile = mobile,
        permanent_address = permanent_address,
        permanent_district = permanent_district,
        permanent_upazila = permanent_upazila,
        permanent_post = permanent_post,
        permanent_post_code = permanent_post_code,
        ssc_roll = ssc_roll,
        ssc_result = ssc_result,
        hsc_result = hsc_result,
        versity_result = versity_result,
        ssc_year = ssc_year,
        hsc_roll = hsc_roll,
        hsc_year = hsc_year,
        versity_roll = versity_roll,
        versity_year = versity_year,
        versity_duration = versity_duration,
        company_name1 = company_name1,
        company_business1 = company_business1,
        company_designation1 = company_designation1,
        company_department1 = company_department1,
        company_responsibility1 = company_responsibility1,
        company_emp_time1 = company_emp_time1,
        company_location1 = company_location1,
        company_experience1 = company_experience1,
        company_name2 = company_name2,
        company_business2 = company_business2,
        company_designation2 = company_designation2,
        company_department2 = company_department2,
        company_responsibility2 = company_responsibility2,
        company_emp_time2 = company_emp_time2,
        company_location2 = company_location2,
        company_experience2 = company_experience2,
        gender_id = gender,
        reletion_status_id = reletion_status,
        religion_id = religion,
        nationality_id = nationality,
        ssc_board_id = ssc_board,
        ssc_group_id = ssc_group,
        hsc_board_id = hsc_board,
        hsc_group_id = hsc_group,
        versity_id = versity,
        versity_group_id = versity_group,
        image = image,

            )
    return render(request,'admin_panel/applicant.html')

def postjob(request):
    if request.session['id']:       
        if request.method == 'POST':
            post_name = request.POST.get('post_name')
            company_name = request.POST.get('company_name')
            vacency = request.POST.get('vacency')
            workplace = request.POST.get('workplace')
            job_location = request.POST.get('job_location')
            salary = request.POST.get('salary')
            deadline = request.POST.get('deadline')
            job_context = request.POST.get('job_context')
            education_requirment = request.POST.get('education_requirment')
            experience_requirment = request.POST.get('experience_requirment')
            additional_requirment = request.POST.get('additional_requirment')
            other_benifit_requirment = request.POST.get('other_benifit_requirment')
            email = request.POST.get('email')
            password = request.POST.get('password')
            category_name = int(request.POST[('category_name')])

            models.jobpost.objects.create(
            user_id = int(request.session['id']),
            post_name = post_name,
            category_name_id = category_name,
            company_name = company_name,
            vacency = vacency,
            workplace = workplace,
            job_location = job_location,
            salary = salary,
            deadline = deadline,
            job_context = job_context,
            education_requirment = education_requirment,
            experience_requirment = experience_requirment,
            additional_requirment = additional_requirment,
            other_benifit_requirment = other_benifit_requirment,
            )
            messages.warning(request, "Circuler is Posted")
            return redirect('/home')
    else:
        return redirect('/org-login')
    return render(request,'admin_panel/addpost.html')



def applicant_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = models.applicant.objects.filter(email = email,password = password).first()
        
        if not user:
            messages.warning(request, "Wrong Information")
            return render(request,'web/applicant_login.html')
        request.session['id'] = user.id
        return redirect('/')
    return render(request,'web/applicant_login.html')

 
def applicant_logout(request):
    request.session['id'] = False
    return redirect('/')





