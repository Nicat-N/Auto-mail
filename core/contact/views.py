from django.shortcuts import render
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from .forms import ContactForm
from django.conf import settings


def send_email(subject, body, to_email, from_email):
    email = EmailMessage(subject, body, to=to_email, from_email=from_email)
    email.content_subtype = "html"
    email.send()


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            send_email(
                subject="Mesajınız Uğurla Alındı ✔️",
                body=render_to_string("email_templates.html", {"name": data["name"]}),
                to_email=[data["email"]],
                from_email=settings.EMAIL_HOST_USER,
            )

            return render(
                request, "contact.html", {"form": ContactForm(), "success": True}
            )

    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form, "success": False})
