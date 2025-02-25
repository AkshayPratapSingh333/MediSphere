from django.contrib import admin
from django.urls import path
from Hospital.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("about/", About, name='about'),
    path("contact/", Contact, name='contact'),
    path("", Index, name='home'),
    path("admin_login/", Login, name='login'),
    path("logout/", Logout_admin, name='logout'),
    path("view_doctor/", View_Doctor, name="view_doctor"),
    path("add_doctor/", Add_Doctor, name="add_doctor"),
    path("delete_doctor/<int:pid>/", Delete_Doctor, name="delete_doctor"),
    path("view_patient/", View_Patient, name="view_patient"),
    path("add_patient/", Add_Patient, name="add_patient"),
    path("delete_patient/<int:pid>/", Delete_Patient, name="delete_patient"),
    path("view_appointment/", View_Appointment, name="view_appointment"),
    path("add_appointment/", Add_Appointment, name="add_appointment"),
    path("delete_appointment/<int:pid>/", Delete_Appointment, name="delete_appointment"),
    path("add_item/", add_item, name="add_item"),
    path("view_items/", view_items, name="view_items"),
    path("edit_item/<int:id>/", edit_item, name="edit_item"),
    path("delete_item/<int:id>/", delete_item, name="delete_item"),
]
