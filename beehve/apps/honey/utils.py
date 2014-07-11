from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

def send_email(request, recpts, subject, text_tmpl, context=None, html_tmpl=None):
    from_email = getattr(settings, 'DEFAULT_FROM_EMAIL', 'info@beehve.io')
    text_content = render_to_string(text_tmpl, context)

    msg = EmailMultiAlternatives(subject, text_content, from_email, recpts)
    if html_tmpl:
        html_content = render_to_string(html_tmpl)
        msg.attach_alternative(html_content, "text/html")

    msg.send()
