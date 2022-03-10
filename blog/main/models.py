from django.db import models
from django.urls import reverse

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    job_desc = models.TextField()
    age  = models.IntegerField()
    img = models.ImageField(null=True, blank=True)
    salary = models.FloatField()
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    
    def __str__(self):
        return self.email
    
    def delete(self):
        self.is_active=False
        self.save()
    
    
    def get_absolute_url(self):
        return reverse("employee_detail", kwargs={"employee_id": self.pk})
    