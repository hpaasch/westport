from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView

from nabes_app.models import (PublicPost, BoardPost, MemberPost, Newsletter,
Profile, Officer)


class IndexView(ListView):
    template_name = 'index.html'
    model = PublicPost

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['officer_list'] = Officer.objects.filter(term='2016-17')
        return context



class NewsletterListView(ListView):
    template_name = 'newsletter.html'
    model = Newsletter
