from django.shortcuts import render, HttpResponse, redirect
from .models import User

# Create your views here.
def index(request):
	return render(request, 'belt_app/index.html')

def register(request):
	first_name = request.POST['first_name']
	last_name = request.POST['last_name']
	email = request.POST['email']
	password = request.POST['password']
	confirm_password = request.POST['confirm_password']
	if User.objects.register(request, first_name, last_name, email, password, confirm_password):
		return redirect('/success')
	else:
		return redirect('/')

def login(request):
	email = request.POST['email']
	password = request.POST['password']
	if User.objects.login(request, email, password):
		return redirect('/success')
	else:
		return redirect('/')

def success(request):
	return render(request, 'belt_app/success.html')