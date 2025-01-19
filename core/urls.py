from django.urls import path
from .views import run_flow_view

urlpatterns = [
    path('', run_flow_view, name='home'),  # Handle the root URL
    path('run-flow/', run_flow_view, name='run_flow'),
]
