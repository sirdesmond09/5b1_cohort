from django.core.management import BaseCommand, CommandError
from ...models import Post
from faker import Faker
from django.contrib.auth import get_user_model


User = get_user_model()

fake = Faker()

class Command(BaseCommand):
    
    
    help = 'Create Dummy posts'


    def handle(self, *args, **options):
        
        print("How many blog post should be created:")
        num = int(input(">"))
        
        posts = []
        for i in range(num):
            data = {}
            
            data['title'] = fake.sentence()
            data['slug'] = data.get("title").lower().replace(" ", "-")
            data['author'] = User.objects.first()
            data['body'] = fake.text()
            
            posts.append(Post(**data))
        
        
        Post.objects.bulk_create(posts)
            
        
        self.stdout.write(self.style.SUCCESS(f"Successfully added {num} posts"))