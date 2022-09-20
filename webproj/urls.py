# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test),
]

# urlpatterns += staticfiles_urlpatterns()
