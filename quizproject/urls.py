from django.contrib import admin
from django.urls import path, include
from quizapp import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('quizapp.urls')), # setting our app url
]
