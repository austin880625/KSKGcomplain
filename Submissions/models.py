from django.db import models
from Pages.models import Page
import urllib
from .special_character_table import TABLE

def get_report_url(post_hashtag):
    return "http://c8763.webutu.com?hashtag="+str(post_hashtag)

# Create your models here.
class Record(models.Model):
    submit_type=models.IntegerField(default=0)
    post_id=models.IntegerField(blank=False)
    fb_post_id=models.TextField(blank=False)

class Report(models.Model):
    REPORTER_TYPE=(
        ("S","Submitter"),
        ("R","Related"),
        ("F","Friend"),
        ("O","Other")
    )
    reporter=models.CharField(max_length=10,choices=REPORTER_TYPE,default="S")
    reason=models.TextField(blank=False)
    post_hashtag=models.IntegerField(blank=False)
    fb_post_id=models.TextField(blank=False)
class Submission(models.Model):
    context=models.TextField(blank=False)
    submit_type=models.IntegerField(default=0)
    submit_time=models.DateTimeField(auto_now_add=True)
    def publish(self,manager):
        page=Page.objects.all()[0]
        fb_api_url="https://graph.facebook.com/"+page.page_id
        post_context="#"
        post_context+=page.prefix+str(page.post_count)
#        post_context+="\n檢舉這篇文章："
#        post_context+=get_report_url(page.post_count)
        page.post_count=page.post_count+1
        page.save()
        response=None
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
        else:
            fb_api_url+="/photos"
            image_text=self.context+"\n"
            watermark=manager
            for tup in TABLE:
                image_text=image_text.replace(tup[0],tup[1])
                watermark=watermark.replace(tup[0],tup[1])
            param=urllib.parse.urlencode({'text':image_text,'line_length':16,'watermark':watermark})
            image_url="http://texttoimage-kskg.rhcloud.com/?%s"%param

            values={
                'caption':post_context,
                'url':image_url,
                'access_token':page.access_token
            }
            data=urllib.parse.urlencode(values)
            byte_data=data.encode('utf8')
            response=urllib.request.urlopen(fb_api_url,byte_data)
        return response.read()
