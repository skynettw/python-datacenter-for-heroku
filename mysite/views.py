from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth
import random
from mysite.models import Post, Country, City, TeamSite, StuSite

def index(request):
	posts = Post.objects.all()
	myname = "何敏煌"
	data = [i for i in range(1, 43)]
	random.shuffle(data)
	lotto_numbers = data[0:6]
	special_number = data[6]
	return render(request, 'index.html', locals())

def show(request, id):
	try:
		target = Post.objects.get(id=id)
	except:
		return redirect("/")
	return render(request, "showpost.html", locals())

def logout(request):
	auth.logout(request)
	return redirect("/")

def rank(request):
	cities = City.objects.all()
	return render(request, "rank.html", locals())

def chart(request):
	cities = City.objects.all()
	return render(request, "chart.html", locals())

def teampages(request):
	return render(request, 'team-pages.html', locals())

def stupages(request):
	sites = StuSite.objects.all()
	return render(request, 'stu-pages.html', locals())


