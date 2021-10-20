from django.urls import path
from . import views


app_name = 'abbracx'

urlpatterns = [
    path('', view.home_view, name='home_view'),
    path('', view.about_view, name='about_view'),
    path('', view.home_view, name='service_view'),
    path('', view.resume_view, name='resume_view'),
    path('', view.skills_view, name='skills_view'),
    path('', view.project_view, name='project_view'),
    path('', view.blog_view, name='blog_view'),
    ]