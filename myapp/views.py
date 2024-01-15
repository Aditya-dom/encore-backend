from django.shortcuts import render, HttpResponse
from datetime import datetime
from myapp.models import ca

def index(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        ca = ca(name=email, password=password, date = datetime.now())
        ca.save()
        print(ca)
    HttpResponse("Thanks for submitting your response")
    return render(request, 'ca.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        login = login(name=email, password=password, date = datetime.now())
        login.save()
        print(login)
    HttpResponse("Thanks for submitting your response")
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        college = request.POST.get('college')
        year = request.POST.get('year')
        dob = request.POST.get('dob')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        referral = request.POST.get('referral')
        register = register(name=username, college=college, year=year, dob=dob, phone=phone, email=email, password=password, referral=referral)
        register.save()
        print(register)
    HttpResponse("Thanks for submitting your response")
    return render(request, 'register.html')



# Create your views here.
