from django.shortcuts import render
from django.forms import Form
from django import forms
from django.http import HttpResponseRedirect
from .models import Submission
# Create your views here.

def Create_Submission(request):
    if request.method=='GET':
        return render(request,'Submissions/create_submission.html')
    elif request.method=="POST":
        #create a new instance of Submission model and fill each field of the submission
        submission=Submission()
        submission.context=request.POST.get('submission_context')
        submission.submit_type=request.POST.get('submission_type')
        submission.save()
        return HttpResponseRedirect('/submit_success')

def Submit_Success(request):
    return render(request,'Submissions/submit_success.html',{})
