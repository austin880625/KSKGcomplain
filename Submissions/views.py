from django.shortcuts import render
from django.forms import Form
from django import forms
from django.http import HttpResponseRedirect,HttpResponse
from .models import Submission
from Pages.models import Page
from operator import attrgetter
import logging
import urllib.error,urllib.request
import json,time
# Create your views here.

ranklist_type_name={
    'daily':"本日排行",
    'weekly':"本週排行",
    'monthly':"本月排行",
}
logger=logging.getLogger(__name__)
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
def Ranklist(request):
    ranklist_type=request.GET.get('ranklist_type')
    if not (ranklist_type=='daily' or ranklist_type=='weekly' or ranklist_type=='monthly'):
        ranklist_type='daily'
    return render(request,'Submissions/ranklist.html', \
                    {'ranklist_type':ranklist_type,'ranklist_type_name':ranklist_type_name[ranklist_type]})

def Update_Ranklist(request):
    ranklist_type=request.GET.get('ranklist_type')
    if not (ranklist_type=='daily' or ranklist_type=='weekly' or ranklist_type=='monthly'):
        ranklist_type='daily'
    data=None
    with open('data/ranklist.json','r') as data_file:
        data=json.load(data_file)
        update_peroid=0
        time_limit=0
        if ranklist_type=='daily':
            update_peroid=1800
            time_limit=86400
        elif ranklist_type=='weekly':
            update_peroid=43200
            time_limit=86400*7
        elif ranklist_type=='monthly':
            update_peroid=86400
            time_limit=86400*30
        logger.error(data[ranklist_type]["last_update"])
        if int(data[ranklist_type]["last_update"])>int(time.time()-update_peroid):
            return HttpResponse(json.dumps(data[ranklist_type]["data"][:101]))
        else:
            data[ranklist_type]["last_update"]=int(time.time())
            data[ranklist_type]["data"]=[];
            page=Page.objects.all()[0]
            fb_api_url="https://graph.facebook.com/"+page.page_id+ \
                        "/posts?fields=reactions.limit(1).summary(true),permalink_url,created_time&date_format=U&access_token="+page.access_token
            try:
                response=json.loads(urllib.request.urlopen(fb_api_url).read().decode('utf-8'))
            except urllib.error.HTTPError as e:
                logger.error(e)
                return HttpResponse(json.dumps(data[ranklist_type]["data"][:101]))
            while True:
                breaking=0
                for post in response["data"]:
                    if post["created_time"]<time.time()-time_limit:
                        breaking=1
                        break
                    data[ranklist_type]["data"].append({"permalink_url":post["permalink_url"],"likes":post["reactions"]["summary"]["total_count"]})
                if breaking==1:
                    break
                new_url=response["paging"]["next"]
                try:
                    response=json.loads(urllib.request.urlopen(new_url).read().decode('utf-8'))
                except urllib.error.HTTPError as e:
                    print(e)
            data[ranklist_type]["data"].sort(key=lambda x:-x["likes"])
            data_file.close()

    with open('data/ranklist.json','w') as data_file:
        json.dump(data,data_file)
        data_file.close()
        return HttpResponse(json.dumps(data[ranklist_type]["data"][:101]))
        #https://graph.facebook.com/KSKGcomplain/posts/?fields=likes,permalink_url
