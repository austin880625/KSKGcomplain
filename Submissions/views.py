from django.shortcuts import render
from django.forms import Form
from django import forms
from django.http import HttpResponseRedirect,HttpResponse
from .models import Submission
from Pages.models import Page
# Create your views here.
def Create_Report(request,hashtag):
    return HttpResponse("YEE")
def Create_Submission(request):
    if request.method=='GET':
        page=Page.objects.all()[0]
        return render(request,'Submissions/create_submission.html',{'placehold':page.placehold})
    elif request.method=="POST":
        #create a new instance of Submission model and fill each field of the submission
        submission=Submission()
        submission.context=request.POST.get('submission_context')
        submission.submit_type=request.POST.get('submission_type')
        submission.save()
        return HttpResponseRedirect('/submit_success')

def Submit_Success(request):
    return render(request,'Submissions/submit_success.html',{})
