from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from applications.user.forms import RegistrationForm
from applications.user.models import User


class RegistrationView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'register_page.html'
    success_url = reverse_lazy('home-page')
