from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contactus(request):
    return render(request, "contact.html")


def loan_program(request):
    return render(request, "loan_program.html")


def loan_program_detail(request):
    return render(request, "loan_program_detail.html")


def calculator(request):
    return render(request, "calculator.html")