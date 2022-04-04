from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.forms import model_to_dict

User = get_user_model()
# Create your models here.

class Post(models.Model):
    STATUS = (("draft", "Draft"),
              ("published", "Published"))
    
    title = models.CharField(max_length=250)
    slug = models.CharField(max_length=350, unique="publish")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publish = models.DateTimeField(default=timezone.now)
    body =  models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        ordering = ('-publish', )
        
    def __str__(self) -> str:
        return self.title
    
    
    @property
    def author_detail(self):
        return model_to_dict(self.author,["username", "first_name", "last_name", "email", "is_active"])
        
        
    
    