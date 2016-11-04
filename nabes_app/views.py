from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView

from nabes_app.models import (PublicPost, BoardPost, MemberPost, Newsletter,
Profile)


class IndexView(ListView):
    template_name = 'index.html'
    model = PublicPost


class NewsletterView(ListView):
    template_name = 'newsletter.html'
    model = Newsletter
