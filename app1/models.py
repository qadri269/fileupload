from django.db import models
import datetime
import os
#Create your models here.
def filepath(request,filename):
    old_name=filename
    current_time=datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename="%s%s" % (current_time,old_name)
    return os.path.join('uploads/', filename)


class student(models.Model):
    std_Name=models.CharField(max_length=50,null=True,blank=True)
    std_reg_no=models.CharField(max_length=50,null=True,blank=True)
    std_address=models.CharField(max_length=50,null=True,blank=True)
   # img=models.ImageField(upload_to=filepath,null=True,blank=True)
    img=models.FileField(upload_to=filepath,null=True,blank=True)

    def __str__(self):
        return self.std_Name
