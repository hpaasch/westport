from django.shortcuts import render
from django.shortcuts import render_to_response # added per youtube for pdf
from django.template import RequestContext # added per youtube for pdf
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User

from reportlab.pdfgen import canvas # for pdf output
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
from django.http import HttpResponse # for pdf output

from nabes_app.models import (PublicPost, BoardPost, MemberPost, Newsletter,
Profile, Officer)

from nabes_app.forms import ProfileUpdateForm



def directory_printed(request):
# see notes in OneNote for this app
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="directory.pdf"'
    directory = canvas.Canvas(response)
    # c = canvas.Canvas(response, pagesize=landscape(letter))
    # c.setFont('Helvetica', 48, leading=None).... see documentation
    # c.drawString(requires coordinates)
    # c.drawCentredString(415, 500, "Certificate of completion")
    # c.drawCentredString(415, 450, "presented to")
    # c.drawCentredString(415, 390, attendeename)

    directory.drawString(40,800, "Howdy, dammit!") # very top left on letter size
    directory.showPage()
    directory.save()
    return response


class IndexView(ListView):
    template_name = 'index.html'
    model = PublicPost


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
    fields = ['primary_last_name',  'primary_phone',
     'primary_email', 'family_member_names', 'house_number', 'street']

    def get_object(self, queryset=None):
        return self.request.user.profile


class NewsletterListView(ListView):
    template_name = 'newsletter.html'
    model = Newsletter


class LeadershipListView(ListView):
    template_name = 'leadership.html'
    model = Officer

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['officer_list'] = Officer.objects.filter(term='2016-17')
        return context


class DirectoryListView(ListView):
    template_name='directory.html'
    model = Profile
    # permission_required = 'profile.user.is_staff'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['directory_list'] = Profile.objects.filter(resident_status='Current').order_by('primary_last_name')
        return context


class StreetListView(ListView):
    template_name='street_list.html'
    model = Profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['street_list'] = Profile.objects.filter(resident_status='Current').order_by('street', 'house_number')
        printout = self.request.GET.get('make_pdf')
        if printout:
            directory_printed

        return context
