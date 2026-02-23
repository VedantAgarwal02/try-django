from django.db import models
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    title       = models.CharField(max_length=20)
    summary     = models.TextField()
    description = models.TextField()
    timestamp   = models.DateTimeField()

    def get_details_url(self):
        # return f"/blogs/{self.id}"
        return reverse("blogs:article_details", kwargs={"article_id": self.id})

    def get_list_url(self): 
        return reverse("blogs:articles_list")