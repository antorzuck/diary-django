from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from main.views import *
# Create your views here.

def home(request):
	return render(request, 'login.html')
	
def signup(request):
	if request.method == 'POST':
		username= request.POST['usern']
		password= request.POST['passw']
		password1= request.POST['passw1']
		
		if len(username) < 4:
			messages.error(request, "Username must be 5 characters long.")
			return redirect('signup')
		if password != password1:
			messages.error(request, "password not matched")
			return redirect('signup')
		try:
			usr= User.objects.get(username=username)
			messages.error(request, "Username Already Exist!")
			return redirect('signup')
		except User.DoesNotExist:
			usr=User.objects.create_user(username=username, password=password)
			usr.save()
			messages.info(request, "Account successfuly created. now please login!")
		return render (request, 'login.html')
	else:
		return render(request, 'signup.html')
		
def login(request):
	if request.method == 'POST':
		username= request.POST['username']
		password= request.POST['password']
		
		user= auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			return redirect('show')
		else:
			messages.error(request, "Incorrect username or password")
			return redirect(home)
			
def logout(request):
	auth.logout(request)
	messages.info(request, "Successfully Logout")
	return redirect(home)