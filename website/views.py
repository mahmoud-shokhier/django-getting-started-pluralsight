from datetime import datetime
from django.http import HttpResponse
import datetime
from django.shortcuts import render
from meetings.models import Meeting
# Create your views here.
def welcome(request):
    return render(request, 'website/welcome.html', 
    {"meetings": Meeting.objects.all()}
    )
    # return HttpResponse('Welcome to the meeting rooms')

def date(request):
    return HttpResponse('the date is {}'.format(datetime.datetime.now()))

def about(request):
    return HttpResponse('my name is mahmoud ali')