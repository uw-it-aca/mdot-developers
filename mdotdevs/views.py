from django.conf import settings
from django.template.loader import get_template
from django.template import RequestContext, Context
from django.shortcuts import render_to_response, render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

import urllib
import json

from forms import ReviewForm


def home(request):
    return render_to_response(
        'mdotdevs/home.html',
        context_instance=RequestContext(request))


def guidelines(request):
    return render_to_response(
        'mdotdevs/guidelines.html',
        context_instance=RequestContext(request))


def process(request):
    return render_to_response(
        'mdotdevs/process.html',
        context_instance=RequestContext(request))


def review(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ReviewForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            campus_audience = form.cleaned_data['campus_audience']
            campus_need = form.cleaned_data['campus_need']
            sponsor_name = form.cleaned_data['sponsor_name']
            sponsor_netid = form.cleaned_data['sponsor_netid']
            sponsor_email = form.cleaned_data['sponsor_email']
            dev_name = form.cleaned_data['dev_name']
            dev_email = form.cleaned_data['dev_email']
            support_name = form.cleaned_data['support_name']
            support_email = form.cleaned_data['support_email']
            support_contact = form.cleaned_data['support_contact']
            ats_review = form.cleaned_data['ats_review']
            ux_review = form.cleaned_data['ux_review']
            brand_review = form.cleaned_data['brand_review']
            app_documentation = form.cleaned_data['app_documentation']
            app_code = form.cleaned_data['app_code']
            anything_else = form.cleaned_data['anything_else']
            try:
                send_mail(
                    sponsor_name,
                    get_template('mdotdevs/email.html').render(
                        Context({
                            'campus_audience': campus_audience,
                            'campus_need': campus_need,
                            'sponsor_name': sponsor_name,
                            'sponsor_netid': sponsor_netid,
                            'sponsor_email': sponsor_email,
                            'dev_name': dev_name,
                            'dev_email': dev_email,
                            'support_name': support_name,
                            'support_email': support_email,
                            'support_contact': support_contact,
                            'ats_review': ats_review,
                            'ux_review': ux_review,
                            'brand_review': brand_review,
                            'app_documentation': app_documentation,
                            'app_code': app_code,
                            'anything_else': anything_else
                        })),
                    sponsor_email, ['jcivjan@uw.edu'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return render_to_response(
                'mdotdevs/thanks.html',
                context_instance=RequestContext(request))
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ReviewForm()
    return render(request, 'mdotdevs/review.html', {'form': form})
