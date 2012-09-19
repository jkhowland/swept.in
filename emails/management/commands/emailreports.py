from django.core.management.base import BaseCommand, CommandError
from django.core.mail import EmailMessage

class Command(BaseCommand):
  help = 'Sends out the report emails to all users'
  
  def handle(self, **options):
        msg = EmailMessage('Request Callback',
                       'Here is the message.', to=['jkhowland@me.com'])
        msg.send()
