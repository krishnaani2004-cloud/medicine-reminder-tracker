"""
URL configuration for medtracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import (
    caretaker_register, home, patient_login, caretaker_login,
    patient_register, register_choice, admin_login,
    admin_dashboard, approve_caretaker, delete_caretaker,
    caretaker_dashboard, patient_dashboard,add_medicine
)

# ADD THESE TWO LINES
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('patient_login/', patient_login, name='patient_login'),
    path('caretaker_login/', caretaker_login, name='caretaker_login'),
    path('register_choice/', register_choice, name='register_choice'),
    path('patient_register/', patient_register, name='patient_register'),
    path('caretaker_register/', caretaker_register, name='caretaker_register'),
    path('admin_login/', admin_login, name="admin_login"),
    path('admin_dashboard/', admin_dashboard, name="admin_dashboard"),
    path('approve_caretaker/<int:caretaker_id>/', approve_caretaker, name="approve_caretaker"),
    path('delete_caretaker/<int:caretaker_id>/', delete_caretaker, name="delete_caretaker"),

    # you may already have these; just making sure:
    path('patient_dashboard/', patient_dashboard, name='patient_dashboard'),
    path('caretaker_dashboard/', caretaker_dashboard, name='caretaker_dashboard'),
    path("add_medicine/", add_medicine, name="add_medicine"),
]

# AT THE VERY BOTTOM
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)