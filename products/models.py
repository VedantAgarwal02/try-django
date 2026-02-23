from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=40)  # max_length = required
    description = models.TextField(blank=True, null=True) # blank has to do with field being required in admin, null has to do with database
    price = models.DecimalField(decimal_places=2, max_digits=1000)
    summary = models.TextField()

    featured = models.BooleanField(default=False)  # add null=True, or give Default value, 

    def get_absolute_url(self):
        # return f"/product/{self.id}"
        return reverse("products:product-details", kwargs={"id": self.id})