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
    return render_to_response('index.html',locals(), context_instance=RequestContext(request))
