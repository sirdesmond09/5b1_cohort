from sys import stdout
from django.core.management import BaseCommand, CommandError
from ...models import Post
from faker import Faker
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = "Checks the entire Django project for potential problems."
    
    
    def handle(self, *args, **option):
        fake = Faker()
        
        posts = []
        
        user = get_user_model().objects.first()
        for i in range(4):
            posts.append(Post(author=user, 
                              title=fake.sentence(),
                              body=fake.text()))
            
        Post.objects.bulk_create(posts)
        
        self.stdout.write("Sucessfully added new posts")