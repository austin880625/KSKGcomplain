from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from Submissions.models import Submission
# Create your views here.
def Manage_Main(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/login')
    submissions=Submission.objects.all()
    return render(request,'Manager/submission_list.html',{'submissions':submissions})
