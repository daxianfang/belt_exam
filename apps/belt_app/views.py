from django.shortcuts import render, HttpResponse, redirect
from .models import User, Friendship

# Create your views here.
def index(request):
	return render(request, 'belt_app/index.html')

def register(request):
	name = request.POST['name']
	alias = request.POST['alias']
	email = request.POST['email']
	password = request.POST['password']
	confirm_password = request.POST['confirm_password']
	if User.objects.register(request, name, alias, email, password, confirm_password):
		return redirect('/')
	else:
		return redirect('/')

def login(request):
	email = request.POST['email']
	password = request.POST['password']
	if User.objects.login(request, email, password):
		logged_in_user = User.objects.filter(email=email)[0]
		request.session['login_id'] = logged_in_user.id
		request.session['login_name'] = logged_in_user.name
		request.session['login_alias'] = logged_in_user.alias
		request.session['login_email'] = logged_in_user.email
		return redirect('/success')
	else:
		return redirect('/')

def success(request):
	context = {
		'topfriends': Friendship.objects.filter(user_id=request.session['login_id']),
		'friends': User.objects.exclude(id=request.session['login_id'])
	}
	return render(request, 'belt_app/success.html', context)

def add(request, id):
	user = User.objects.filter(id=request.session['login_id'])[0]
	friend = User.objects.filter(id=id)[0]
	Friendship.objects.create(user=user, friend=friend)
	return redirect('/success')

def remove(request, id):
	Friendship.objects.filter(id=id).delete()
	return redirect('/success')

def info(request, id):
	context = {
		'users': User.objects.filter(id=id)
	}
	return render(request, 'belt_app/info.html', context)
	

def logout(request):
	del request.session['login_id']
	return redirect('/')



