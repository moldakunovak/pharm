from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core import mail




def send_code_email(user):
    context = {
        "text_detail": "Thank's for register",
        "email": user.email,
        "domain": " http://127.0.0.1:8080/",
        "activation_code": user.activation_code
    }

    msg = render_to_string("email.html", context)
    plain_message = strip_tags(msg)
    subject = "Active account"
    to = user.email
    mail.send_mail(subject, plain_message, "moldakunovakk@gmail.com", [to,], html_message=msg)