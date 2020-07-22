from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.contrib.auth import login, authenticate
from django.core.mail import send_mail
from django.http import HttpResponse
from photos.models import Photo
from feedback.forms import FeedbackForm
from django.conf import settings

from .tasks import sleepy
from .forms import SignupForm


class PhotoView(ListView):
    model = Photo
    template_name = 'photos/photo_list.html'
    paginate_by = 24

    def get_context_data(self, **kwargs):
        context = super(PhotoView, self).get_context_data(**kwargs)
        context['form'] = FeedbackForm()
        return context


def index(request):
    sleepy.delay(10)
    context = {
        "title": "Nestor",
        "content": " Welcome to the homepage phothos.",

    }
    if request.user.is_authenticated:
        context["premium_content"] = "Exa"
    return render(request, "photos/base.html", context)


def signup_view(request):
    ctx = {}
    subject = "Thank you for registering to our site"
    message = "You have succesfully created an account"
    email_from = settings.EMAIL_HOST_USER
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            recipient_list = [email, ]
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            send_mail(subject, message, email_from, recipient_list)
            login(request, user)
            return redirect('photos:index')
    else:
        form = SignupForm()
    ctx['form'] = form
    return render(request, 'photos/signup.html', ctx)

    # return render(request )


def emailsending(request):
    subject = "Thank you for otro"
    message = "You have otro"
    email_from = settings.EMAIL_HOST_USER
    toaddress = ['nestor.pruebas.02@gmail.com']
    send_mail(subject, message, email_from, toaddress)
    return render(request, 'photos/otro.html')
