from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView

from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy


from django.contrib.auth.models import User


from nabes_app.models import (PublicPost, BoardPost, MemberPost, Newsletter,
Profile, Officer)

from nabes_app.forms import ProfileUpdateForm


class IndexView(ListView):
    template_name = 'index.html'
    model = PublicPost

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['officer_list'] = Officer.objects.filter(term='2016-17')
        return context


class CreateAccountView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('login')


class ProfileView(ListView):
    model = Profile

    def get_object(self, queryset=None):
        return self.request.user.profile


class ProfileUpdateView(UpdateView):
    model = Profile
    success_url = reverse_lazy('profile_view')
    fields = ['primary_last_name', 'primary_email', 'number', 'street', 'photo']

    def get_object(self, queryset=None):
        return self.request.user.profile

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["profile_form"] = ProfileUpdateForm(initial={
    #         "name": self.request.user.profile.primary_last_name,
    #         "email": self.request.user.profile.email,
    #         "number": self.request.user.profile.number,
    #         "street": self.request.user.profile.street,
    #         })
    #     return context


class NewsletterListView(ListView):
    template_name = 'newsletter.html'
    model = Newsletter
