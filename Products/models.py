from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    name        = models.CharField(max_length=100) 
    description = models.TextField(blank=True)
    price       = models.DecimalField(max_digits=100, decimal_places=2, null=True)
    summary     = models.TextField(default="This is a sample Product")
    featured    = models.BooleanField(default=False)

    def get_absolute_url(self):
        # return f"/product/{self.id}/"
        return reverse("Products:view_product", kwargs={"my_id": self.id})