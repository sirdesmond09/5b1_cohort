from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post


class BlogTests(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        #createuser
        test_user = User.objects.create(username='testuser1', password='abc123')
        
        # Create a blog post
        test_post = Post.objects.create(author=test_user, title='Blog title', body='Body content...')

    
    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEqual(author, 'testuser1')
        self.assertEqual(title, 'Blog title')
        self.assertEqual(body, 'Body content...')

    
