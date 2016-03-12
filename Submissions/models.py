from django.db import models
from Pages.models import Page
import urllib

# Create your models here.
class Submission(models.Model):
    context=models.TextField(blank=False)
    submit_type=models.IntegerField(default=0)
    submit_time=models.DateTimeField(auto_now_add=True)
    def publish(self,manager):
        page=Page.objects.all()[0]
        fb_api_url="https://graph.facebook.com/"+page.page_id
        post_context="#"
        post_context+=page.prefix+str(page.post_count)
        if self.submit_type==0:
            fb_api_url+="/feed"
            post_context+="\n\n"+self.context+"\n\n"
            post_context+=manager

            values={
                'message':post_context,
                'access_token':page.access_token
            }
            data=urllib.parse.urlencode(values)
            byte_data=data.encode('utf8')
            response=urllib.request.urlopen(fb_api_url,byte_data)
            print(response)
        else:
            fb_api_url+="/photos"
            image_text=self.context+"\n\n"+manager
            image_text=image_text.replace('Ω','&#937;')
            param=urllib.parse.urlencode({'text':image_text})
            image_url="http://texttoimage-kskg.rhcloud.com/?%s"%param

            values={
                'caption':post_context,
                'url':image_url,
                'access_token':page.access_token
            }
            data=urllib.parse.urlencode(values)
            byte_data=data.encode('utf8')
            response=urllib.request.urlopen(fb_api_url,byte_data)
            print(response)
        page.post_count+=1
        page.save()
