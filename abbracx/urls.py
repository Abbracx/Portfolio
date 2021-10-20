from django.urls import path
from . import views


app_name = 'abbracx'

urlpatterns = [
    path('', view.home_view, name='home_view'),
    ]