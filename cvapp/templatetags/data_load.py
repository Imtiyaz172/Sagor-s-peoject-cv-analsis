from django import template
from django.shortcuts import render, redirect
from django.db.models import Sum, Count, Q
from cvapp import models
register = template.Library()


@register.filter(name='gender_reg')
def gender(request):
    delivery  = models.Gender.objects.filter(status = True).order_by("id")
    return delivery


@register.filter(name='status_reg')
def status(request):
    delivery  = models.Status.objects.filter(status = True).order_by("id")
    return delivery


@register.filter(name='religion_reg')
def religion(request):
    delivery  = models.Religion.objects.filter(status = True).order_by("id")
    return delivery


@register.filter(name='nationality_reg')
def nationality(request):
    delivery  = models.Nationality.objects.filter(status = True).order_by("id")
    return delivery

@register.filter(name='sscBoard_reg')
def sscBoard(request):
    delivery  = models.sscBoard.objects.filter(status = True).order_by("id")
    return delivery


@register.filter(name='hscBoard_reg')
def hscBoard(request):
    delivery  = models.hscBoard.objects.filter(status = True).order_by("id")
    return delivery

@register.filter(name='ssc_group_reg')
def ssc_group(request):
    delivery  = models.ssc_group.objects.filter(status = True).order_by("id")
    return delivery

@register.filter(name='hsc_group_reg')
def hsc_group(request):
    delivery  = models.hsc_group.objects.filter(status = True).order_by("id")
    return delivery


@register.filter(name='Versity_reg')
def Versity(request):
    delivery  = models.Versity.objects.filter(status = True).order_by("id")
    return delivery


@register.filter(name='VersitySubject_reg')
def VersitySubject(request):
    delivery  = models.VersitySubject.objects.filter(status = True).order_by("id")
    return delivery

@register.filter(name='VersityDuration_reg')
def VersityDuration(request):
    delivery  = models.VersityDuration.objects.filter(status = True).order_by("id")
    return delivery

@register.filter(name='jobcatreg')
def jobcat(request):
    delivery  = models.job_category.objects.filter(status = True).order_by("id")
    return delivery


@register.filter(name='str2url')
def string_to_url_convert(data):
    #use in view: category = cat.replace('-', ' ')
    # use in html: text|str2url
    data = str(data)    
    return data.replace(' ', '-') 


@register.filter(name='replace')
def replace_load(obj):
    rep = obj.replace("%20"," ")
    return rep
