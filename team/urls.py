from django.conf.urls import url
from team import views
from team.views import IndexView, CalendarView, ChatView, ClientView, ComponentCalendarView, ProjectView, ReportView, \
    TimeView, WorkspaceView, SignUp, RoomView
from django.contrib.auth import views as auth_views
from django.contrib import admin
from team import views as core_views

urlpatterns = [

    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^calendar/$', CalendarView.as_view(), name='calendar'),
    url(r'^chat/$', ChatView.as_view(), name='chat'),
    url(r'^client/$', ClientView.as_view(), name='client'),
    url(r'^component/$', ComponentCalendarView.as_view(), name='component'),
    url(r'^help/$', CalendarView.as_view(), name='help'),
    url(r'^project/$', ProjectView.as_view(), name='project'),
    url(r'^report/$', ReportView.as_view(), name='report'),
    url(r'^team/$', CalendarView.as_view(), name='team'),
    url(r'^time/$', TimeView.as_view(), name='time'),
    url(r'^workspace/$', WorkspaceView.as_view(), name='workspace'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^signup/$', SignUp.as_view(), name='signup'),
    url(r'^room/$', RoomView.as_view(), name='room')

]
