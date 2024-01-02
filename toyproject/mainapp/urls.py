from django.urls import path
from .views import *

# urlpatterns = [
#     path("", views.index, name="index"),
# ]

app_name='mainapp'

urlpatterns = [
    path('', index),
    path('blog/', blog),
]