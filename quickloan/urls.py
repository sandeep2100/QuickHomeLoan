from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("about/", about, name="about"),
    path("contact-us/", contactus, name="contact-us"),
    path("loan_program/", loan_program, name="loan_program"),
    path("loan_program_detail/", loan_program_detail, name="loan_program_detail"),
    path("calculator/", calculator, name="calculator"),

]