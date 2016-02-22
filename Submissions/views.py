from django.shortcuts import render
from django.forms import Form
from django import forms
from django.http import HttpResponseRedirect
from .models import Submission
# Create your views here.
class Submission_Form(Form):
    submission_context=forms.CharField(widget=forms.Textarea)

def Create_Submission(request):
    if request.method=='GET':
        form=Submission_Form()
        return render(request,'Submissions/create_submission.html',{"form":form})
    elif request.method=="POST":
        #check if the form is valid first (which the code can't be empty)
        form=Submission_Form(request.POST)
        if not form.is_valid():
            return HttpResponseRedirect('')
        #create a new instance of Submission model and fill each field of the submission
        submission=Submission()
        submission.context=request.POST.get('submission_context')
        submission.save()
        return HttpResponseRedirect('/submit_success')

def Submit_Success(request):
    return render(request,'Submissions/submit_success.html',{})
