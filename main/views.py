from django.shortcuts import render, redirect
from accounts.views import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
# Create your views here.
@login_required(login_url="/signin/")
def show(request):
	loguser= request.user
	memories= memory.objects.filter(user=loguser).order_by('-date')
	paginator= Paginator(memories,5)
	page_num=request.GET.get('page',1)
	memories= paginator.page(page_num)
	return render(request, 'show.html', {'m':memories},)
	
@login_required(login_url="/signin/")
def add(request):
	if request.method == 'POST':
		datas = request.POST['data']
		sav = memory(content=datas, user=request.user)
		sav.save()
		return redirect(show)
	else:
		return render(request, 'add.html')

def search(request):
	if request.method == "POST":
		query=request.POST['s']
		lu= request.user
		searched= memory.objects.filter(user=lu,content__icontains=query).order_by('-date')
		context={
			'query':query,
			'searched':searched,
		}
		return render(request, 'search.html', context)
	else:
		return render(request, 'search.html', context)
		