from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.safestring import mark_safe 
import os

# Create your models here.

class DistrictEntry(models.Model):
    district_name_bangla  = models.CharField(max_length=230)
    district_name_english  = models.CharField(max_length=230)
    ordering       = models.IntegerField(default=0)
    add_date    = models.DateTimeField(auto_now_add = True)
    status         = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.district_name_bangla)

class UpazillaEntry(models.Model):
    district_name  = models.ForeignKey(DistrictEntry, on_delete=models.CASCADE)
    upazilla_name_bangla   = models.CharField(max_length=230)
    upazilla_name_english  = models.CharField(max_length=230)
    add_date       = models.DateTimeField(auto_now_add = True)
    status         = models.BooleanField(default=1)

    def __str__(self):
        return str(self.upazilla_name_bangla)


class Gender(models.Model):
    gender  = models.CharField(max_length=30)
    status         = models.BooleanField(default=1)

    def __str__(self):
        return str(self.gender)

class Status(models.Model):
    reletion_status  = models.CharField(max_length=30)
    status         = models.BooleanField(default=1)

    def __str__(self):
        return str(self.reletion_status)

class Religion(models.Model):
    religion  = models.CharField(max_length=30)
    status         = models.BooleanField(default=1)

    def __str__(self):
        return str(self.religion)

class Nationality(models.Model):
    nationality  = models.CharField(max_length=30)
    status         = models.BooleanField(default=1)

    def __str__(self):
        return str(self.nationality)

class sscBoard(models.Model):
    board_name  = models.CharField(max_length=30)
    status         = models.BooleanField(default=1)

    def __str__(self):
        return str(self.board_name)

class ssc_group(models.Model):
    group_name  = models.CharField(max_length=30)
    status         = models.BooleanField(default=1)

    def __str__(self):
        return str(self.group_name)

class hsc_group(models.Model):
    group_name  = models.CharField(max_length=30)
    status         = models.BooleanField(default=1)

    def __str__(self):
        return str(self.group_name)

class hscBoard(models.Model):
    board_name  = models.CharField(max_length=30)
    status         = models.BooleanField(default=1)

    def __str__(self):
        return str(self.board_name)

class Versity(models.Model):
    versity_name  = models.CharField(max_length=30)
    status         = models.BooleanField(default=1)

    def __str__(self):
        return str(self.versity_name)

class VersitySubject(models.Model):
    department  = models.CharField(max_length=30)
    status         = models.BooleanField(default=1)

    def __str__(self):
        return str(self.department)

class VersityDuration(models.Model):
    duration  = models.CharField(max_length=30)
    status         = models.BooleanField(default=1)

    def __str__(self):
        return str(self.duration)


class applicant(models.Model):
    gender  = models.ForeignKey(Gender, on_delete=models.CASCADE,blank=True,null=True)
    reletion_status  = models.ForeignKey(Status, on_delete=models.CASCADE,blank=True,null=True)
    religion  = models.ForeignKey(Religion, on_delete=models.CASCADE,blank=True,null=True)
    nationality  = models.ForeignKey(Nationality, on_delete=models.CASCADE,blank=True,null=True)
    image         = models.FileField(upload_to="cv-image/",blank= True)
    first_name   = models.CharField(max_length=230,blank=True,null=True)
    last_name   = models.CharField(max_length=230,blank=True,null=True)
    father_name   = models.CharField(max_length=230,blank=True,null=True)
    mother_name   = models.CharField(max_length=230,blank=True,null=True)
    date_of_birth  = models.CharField(max_length=230,blank=True,null=True)
    national_id  = models.CharField(max_length=230,blank=True,null=True)
    pasport_id  = models.CharField(max_length=230,blank=True,null=True)
    birth_reg  = models.CharField(max_length=230,blank=True,null=True)
    email  = models.CharField(max_length=230,blank=True,null=True)
    password  = models.CharField(max_length=230,blank=True,null=True)
    present_address  = models.CharField(max_length=230,blank=True,null=True)
    present_district  = models.CharField(max_length=230,blank=True,null=True)
    present_upazila  = models.CharField(max_length=230,blank=True,null=True)
    present_post  = models.CharField(max_length=230,blank=True,null=True)
    present_post_code  = models.CharField(max_length=230,blank=True,null=True)
    mobile  = models.CharField(max_length=230,blank=True,null=True)
    permanent_address  = models.CharField(max_length=230,blank=True,null=True)
    permanent_district  = models.CharField(max_length=230,blank=True,null=True)
    permanent_upazila  = models.CharField(max_length=230,blank=True,null=True)
    permanent_post  = models.CharField(max_length=230,blank=True,null=True)
    permanent_post_code  = models.CharField(max_length=230,blank=True,null=True)
    ssc_board  = models.ForeignKey(sscBoard, on_delete=models.CASCADE,blank=True,null=True)
    ssc_roll  = models.CharField(max_length=230,blank=True,null=True)
    ssc_year  = models.CharField(max_length=230,blank=True,null=True)
    ssc_result  = models.CharField(max_length=230,blank=True,null=True)
    ssc_group  = models.ForeignKey(ssc_group, on_delete=models.CASCADE,blank=True,null=True)
    hsc_board  = models.ForeignKey(hscBoard, on_delete=models.CASCADE,blank=True,null=True)
    hsc_roll  = models.CharField(max_length=230,blank=True,null=True)
    hsc_result  = models.CharField(max_length=230,blank=True,null=True)
    hsc_year  = models.CharField(max_length=230,blank=True,null=True)
    hsc_group  = models.ForeignKey(hsc_group, on_delete=models.CASCADE,blank=True,null=True)
    versity  = models.ForeignKey(Versity, on_delete=models.CASCADE,blank=True,null=True)
    versity_roll  = models.CharField(max_length=230,blank=True,null=True)
    versity_result  = models.CharField(max_length=230,blank=True,null=True)
    versity_year  = models.CharField(max_length=230,blank=True,null=True)
    versity_duration  = models.CharField(max_length=230,blank=True,null=True)
    versity_group  = models.ForeignKey(VersitySubject, on_delete=models.CASCADE,blank=True,null=True)
    company_name1  = models.CharField(max_length=230,blank=True,null=True)
    company_business1  = models.CharField(max_length=230,blank=True,null=True)
    company_designation1  = models.CharField(max_length=230,blank=True,null=True)
    company_department1  = models.CharField(max_length=230,blank=True,null=True)
    company_responsibility1  = models.CharField(max_length=230,blank=True,null=True)
    company_emp_time1  = models.CharField(max_length=230,blank=True,null=True)
    company_location1  = models.CharField(max_length=230,blank=True,null=True)
    company_experience1  = models.CharField(max_length=230,blank=True,null=True)
    company_name2  = models.CharField(max_length=230,blank=True,null=True)
    company_business2  = models.CharField(max_length=230,blank=True,null=True)
    company_designation2  = models.CharField(max_length=230,blank=True,null=True)
    company_department2  = models.CharField(max_length=230,blank=True,null=True)
    company_responsibility2  = models.CharField(max_length=230,blank=True,null=True)
    company_emp_time2  = models.CharField(max_length=230,blank=True,null=True)
    company_location2  = models.CharField(max_length=230,blank=True,null=True)
    company_experience2  = models.CharField(max_length=230,blank=True,null=True)
    add_date       = models.DateTimeField(auto_now_add = True)
    same_as_present         = models.BooleanField(default=False)
    status         = models.BooleanField(default=True)

    def __str__(self):
        return str(self.email)



class job_category(models.Model):
    
    category_name   = models.CharField(max_length=230,null=True,blank=True)
    status         = models.BooleanField(default=True)

    def __str__(self):
        return str(self.category_name)



class Organization(models.Model): 
    email  = models.CharField(max_length=230,blank=True,null=True)
    password  = models.CharField(max_length=230,blank=True,null=True)
    add_date       = models.DateTimeField(auto_now_add = True)
    status         = models.BooleanField(default=True)

    def __str__(self):
        return str(self.email)

class jobpost(models.Model):
    user          = models.ForeignKey(Organization, on_delete=models.CASCADE,blank=True,null=True)
    post_name   = models.CharField(max_length=230,null=True,blank=True)
    category_name   = models.ForeignKey(job_category, on_delete=models.CASCADE,blank=True,null=True)
    company_name   = models.CharField(max_length=230,null=True,blank=True)
    vacency   = models.CharField(max_length=230,null=True,blank=True)
    workplace   = models.CharField(max_length=230,null=True,blank=True)
    job_location   = models.CharField(max_length=230,null=True,blank=True)
    salary  = models.CharField(max_length=230,null=True,blank=True)
    deadline  = models.CharField(max_length=230,null=True,blank=True)
    job_context  = RichTextField(blank=True)
    education_requirment  = RichTextField(blank=True)
    experience_requirment  = RichTextField(blank=True)
    additional_requirment  = RichTextField(blank=True)
    other_benifit_requirment  = RichTextField(blank=True)
    add_date       = models.DateTimeField(auto_now_add = True)
    status         = models.BooleanField(default=True)

    def __str__(self):
        return str(self.post_name)


        
class user_application(models.Model):

    jobpost   = models.ForeignKey(jobpost, on_delete=models.CASCADE,blank=True,null=True)
    applicant   = models.ForeignKey(applicant, on_delete=models.CASCADE,blank=True,null=True)
    expected_salary   = models.CharField(max_length=230,null=True,blank=True)
    add_date       = models.DateTimeField(auto_now_add = True)
    skill_match       = models.IntegerField(default=0)
    shortlist         = models.BooleanField(default=False)
    interviewlist         = models.BooleanField(default=False)
    status         = models.BooleanField(default=True)

    def __str__(self):
        return str(self.jobpost)