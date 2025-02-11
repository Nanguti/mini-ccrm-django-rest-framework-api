from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('leads.urls')),
    path('', include('contacts.urls')),
    path('', include('notes.urls')),
    path('', include('reminders.urls')),
]
