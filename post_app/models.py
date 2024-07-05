from django.db import models

from django.contrib.auth.models import User


class Create_text_post(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)

    def __str__(self) -> str:
        return self.post[:30]


class Create_Video_post(models.Model):
        user= models.ForeignKey(User, on_delete=models.CASCADE)
        user_video = models.FileField()
        video_title = models.CharField(max_length=1000,null=True,blank=True)
        created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
        updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)


        def __str__(self) -> str:
             return self.created_at
        
class Create_musuic_post(models.Model):
        user= models.ForeignKey(User, on_delete=models.CASCADE)
        user_musuic = models.FileField()
        musuic_text = models.CharField(max_length=1000,null=True,blank=True)
        created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
        updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)


        def __str__(self) -> str:
             return self.created_at
        
class Create_photo_post(models.Model):
        user= models.ForeignKey(User, on_delete=models.CASCADE)
        user_photo = models.ImageField(upload_to='user_images/Posts')
        photo_text = models.CharField(max_length=1000,null=True,blank=True)
        created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
        updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)


        def __str__(self) -> str:
             return self.created_at


    