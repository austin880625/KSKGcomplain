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

def Manage_Post_Operation(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/login')
    op_type=request.POST.get('op_type')
    print(op_type)
    submissions=request.POST.getlist('submissions')
    print(submissions)
    for sub_id in submissions:
        submission=Submission.objects.get(id=sub_id)
        if op_type == "publish":
            submission.publish(request.user.profile.nickname)
        submission.delete()
    return HttpResponseRedirect('/manage')
