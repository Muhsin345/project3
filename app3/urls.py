from django.urls import path
from django.urls import path

from app3.models import student
from . import views
urlpatterns = [
    path('smpl/',views.fnOne),
    path('registration/',views.fnregistration,name='registration'),
    path('student/',views.fnstd,name='student'),
    path('password/',views.pword,name='password'),
    path('logout/',views.fnlogout,name='logout'),
    path('file/',views.fnfile,name='file'),
    path('ajax/',views.fnajax,name='ajax'),
    path('ajx2/',views.fnajx,name='ajx'),
    path('edit/',views.fnedit,name='edit'),
    path('update/',views.fupdate,name='update'),
    path('delete/',views.fndelete,name='delete'),
    path('drf/',views.fndrf,name='drf'),
    path('post/',views.fnpost,name='post'),
    path('del/',views.delapi,name='delapi'),
    path('profile/',views.fnprof,name='profile')
]