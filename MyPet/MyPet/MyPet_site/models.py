from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class myPetText(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    title = models.CharField(max_length = 200)
    contents = models.CharField(max_length = 200)
    img_url = models.FileField(null = True)
    category = models.CharField(max_length = 200, null = True)
    board_text = RichTextUploadingField(null = True) 

    pet_title = models.CharField(max_length = 200, null = True)
    pet_video = models.CharField(max_length = 1000, null = True)

    def publish(self):
        self.save()
    
    def _str_(self):
        return self.title

class Comment(models.Model):
    pet = models.ForeignKey(myPetText, on_delete = models.CASCADE)
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, null = True)
    rate =  models.CharField(max_length = 200, null = True)
    comments = models.CharField(max_length = 200, null = True)

    def publish(self):
        self.save()

    def _str_(self):
        return self.comments