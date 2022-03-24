from django.core import exceptions
from django.core.management.base import BaseCommand, CommandError



class Command(BaseCommand):
    help = 'Create Dummy Box locations'


    def handle(self, *args, **options):
        
        
        
        self.stdout.write(self.style.SUCCESS("Successfully added superuser"))