from django.db import models
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    content = models.TextField(blank=True, verbose_name="Content")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Photo")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True, verbose_name="Published")   
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"post_id": self.pk})
    
    
    def __str__(self):
        return self.title 
