from django.conf import settings
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponseRedirect

import urllib
import json

from forms import ReviewForm

# create your views here

def home(request):
    return render_to_response('mdotdevs/home.html', context_instance=RequestContext(request))
    

def guidelines(request):
    return render_to_response('mdotdevs/guidelines.html', context_instance=RequestContext(request))
    
def process(request):
    return render_to_response('mdotdevs/process.html', context_instance=RequestContext(request))

def review(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ReviewForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ReviewForm()

    return render(request, 'mdotdevs/review.html', {'form': form})