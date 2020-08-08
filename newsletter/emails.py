from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_multiple_email(email):
    subject = 'Welcome to StarAid Newsletter'
    sender = 'noreply@staraid.ai'

    #passing in the context vairables
    text_template = render_to_string('email-subscribe.txt',{"email": email})

    message = EmailMultiAlternatives(subject,text_template,sender, [email])
    message.send()