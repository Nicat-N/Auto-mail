

from django.contrib import admin
from django.urls import path
from contact import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("contact/", views.contact_view, name="contact"),
]
