# -*- coding: utf-8 -*-

#project import
from faraja.website.models import *

#python import
from datetime import *
from time import *
from random import choice

#django import
from django.contrib.sites.models import Site
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import SetPasswordForm, PasswordChangeForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.http import urlencode
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import SetPasswordForm, PasswordChangeForm
from django.contrib.auth.tokens import default_token_generator
from django.template import Context, loader
from django.utils.http import int_to_base36, urlquote, base36_to_int
from django.conf import settings
from django.forms.formsets import formset_factory
from django.contrib import messages
from django.core import serializers
import django.utils.simplejson as json

def index(request):
    news_list = MainNews.objects.all().order_by('order')
    return render_to_response('index.html',locals(), context_instance=RequestContext(request))

def who_we_are(request):
    text_list = WhoWeAre.objects.all()
    text = text_list[0]
    return render_to_response('who_we_are.html',locals(), context_instance=RequestContext(request))

def trustees(request):
    trustee_list = Trustee.objects.all()
    return render_to_response('trustees.html',locals(), context_instance=RequestContext(request))

def what_we_do(request):
    text_list = WhatWeDo.objects.all()
    text = text_list[0]
    activities_list = WhatWeDoActivity.objects.all()
    return render_to_response('what_we_do.html',locals(), context_instance=RequestContext(request))

def activity(request, id_activity):
    activity = WhatWeDoActivity.objects.get(id=id_activity)
    return render_to_response('activity.html',locals(), context_instance=RequestContext(request))

def therapists(request):
    therapists_list = Therapist.objects.all()
    return render_to_response('therapists.html',locals(), context_instance=RequestContext(request))

def involved(request):
    involved_list = Involved.objects.all()
    return render_to_response('involved.html',locals(), context_instance=RequestContext(request))

def cancer(request):
    treatments_list = CancerTreatment.objects.all()
    specific_list = CancerSpecific.objects.all()
    return render_to_response('cancer.html',locals(), context_instance=RequestContext(request))

def testimonials(request):
    testimonials_list = Testimonial.objects.all()
    return render_to_response('testimonials.html',locals(), context_instance=RequestContext(request))

def faq(request):
    faq_list = FAQ.objects.all()
    return render_to_response('faq.html',locals(), context_instance=RequestContext(request))

def contact_us(request):
    return render_to_response('contact_us.html',locals(), context_instance=RequestContext(request))

def donate(request):
    return render_to_response('donate.html',locals(), context_instance=RequestContext(request))

def news(request):
    news_list = News.objects.all().order_by('date')
    return render_to_response('news.html',locals(), context_instance=RequestContext(request))

def detail_news(request, id_news):
    news = News.objects.get(id=id_news)
    return render_to_response('detail_news.html',locals(), context_instance=RequestContext(request))