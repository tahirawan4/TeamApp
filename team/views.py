# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from chat.models import Room
from team.forms import SignUpForm

from django.shortcuts import render
from django.contrib.auth.decorators import login_required


class RoomView(generic.TemplateView):
    template_name = 'room.html'

    def get(self, request, *args, **kwargs):
        rooms = Room.objects.all().order_by('title')
        return render(request, self.template_name, {"rooms": rooms })


class IndexView(generic.TemplateView):
    template_name = 'index.html'


class CalendarView(generic.TemplateView):
    template_name = 'calendar.html'


class ChatView(generic.TemplateView):
    template_name = 'chat.html'


class ClientView(generic.TemplateView):
    template_name = 'client.html'


class ComponentCalendarView(generic.TemplateView):
    template_name = 'component_calendar.html'


class HelpView(generic.TemplateView):
    template_name = 'help.html'


class ProjectView(generic.TemplateView):
    template_name = 'projects.html'


class ReportView(generic.TemplateView):
    template_name = 'reports.html'


class TeamView(generic.TemplateView):
    template_name = 'team.html'


class TimeView(generic.TemplateView):
    template_name = 'time.html'


class WorkspaceView(generic.TemplateView):
    template_name = 'workspace.html'


class SignUp(generic.CreateView):
    form_class = SignUpForm
    # success_url = reverse_lazy('login')
    template_name = 'signup.html'

    def post(self, request):
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('login')
        else:
            form = SignUpForm()
        return render(request, 'signup.html', {'form': form})
