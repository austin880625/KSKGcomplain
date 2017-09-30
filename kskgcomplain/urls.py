"""kskgcomplain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from kskgcomplain.views import Login,Logout

from Submissions.views import Create_Submission,Submit_Success,Ranklist,Update_Ranklist,Create_Report
from Manager.views import Manage_Main,Manage_Post_Operation,Fetch_Submission,Update_Submission

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',Create_Submission),
    url(r'^report/(?P<hashtag>[0-9]+)/$',Create_Report),
    url(r'^submit_success/$',Submit_Success),
    url(r'^ranklist/$',Ranklist,name="ranklist"),
    url(r'^ranklist/update$',Update_Ranklist,name="update_ranklist"),
    url(r'^manage/$', Manage_Main),
    url(r'^manage/fetch_submission/$',Fetch_Submission),
    url(r'^manage/update_submission/$',Update_Submission),
    url(r'^manage/post_operation$',Manage_Post_Operation,name="post_operation"),

    url(r'^accounts/login/$',Login,name='login'),
    url(r'^accounts/logout/$',Logout,name='logout'),
]
