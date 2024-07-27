from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.http import HttpResponse
from .forms import ContactForm
from firstapp.models import Media
# Create your views here.


def send_email_view(request):
    suite = Media.objects.get(name='suite logo')
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            recipient = form.cleaned_data['recipient']

            #Render email subject and body

            subject_template = render_to_string('emails/subject.txt', {'subject': subject})
            body_template = render_to_string('emails/email_body.html', {'subject': subject, 'message': message, 'image': suite})
            #create an email

            email = EmailMultiAlternatives(
                subject=subject_template.strip(),
                body=message,
                from_email='your_email',
                to=[recipient]
            )
            email.attach_alternative(body_template, 'text/html')
            print('edible')
            email.send()

            return HttpResponse('Email sent successfuly')
    else:
        form = ContactForm()
    return render(request, 'emails/send_email.html', {'form': form})
