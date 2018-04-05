from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import auth
from Submissions.models import Submission
import json
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
            raw_publish_state=submission.publish(request.user.profile.nickname)
            publish_state=json.loads(raw_publish_state.decode('utf-8'))
            if publish_state.get('error')==None:
                submission.delete()
            else:
                print(raw_publish_state.decode('utf-8'))
        else:
            submission.delete()
    return HttpResponseRedirect('/manage')
def Fetch_Submission(request):
    if not request.user.is_authenticated():
        return HttpResponse("error")
    sub_id=request.GET.get('id')
    submission=Submission.objects.get(id=sub_id)
    return HttpResponse(submission.context)
def Update_Submission(request):
    if not request.user.is_authenticated():
        return HttpResponse("error")
    sub_id=request.POST.get('id')
    new_cont=request.POST.get('context')
    submission=Submission.objects.get(id=sub_id)
    submission.context=new_cont
    submission.save()
    return HttpResponse("success")
