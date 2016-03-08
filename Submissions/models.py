from django.db import models
from Pages.models import Page
import urllib

# Create your models here.
class Submission(models.Model):
    context=models.TextField(blank=False)
    submit_time=models.DateTimeField(auto_now_add=True)
    def publish(self,manager):
        page=Page.objects.all()[0]
        fb_api_url="https://graph.facebook.com/"+page.page_id+"/feed"
        post_context="#"
        post_context+=page.prefix+str(page.post_count)+"\n\n"
        post_context+=self.context+"\n"
        post_context+=manager

        values={
        'message':post_context,
        'access_token':page.access_token
        }
        page.post_count+=1
        page.save()
        data=urllib.parse.urlencode(values)
        byte_data=data.encode('utf8')
        response=urllib.request.urlopen(fb_api_url,byte_data)
        print(response)
