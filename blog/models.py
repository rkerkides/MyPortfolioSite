from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = CKEditor5Field('Text', config_name='extends')
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='blog/images/')
    
    def __str__(self):
        return self.title
