# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test),
    # get three.html
    path('three/', views.three),
]

# urlpatterns += staticfiles_urlpatterns()
