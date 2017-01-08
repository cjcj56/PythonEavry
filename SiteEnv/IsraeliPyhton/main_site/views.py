from django.shortcuts import render

def welcome(request):
	return render(request,'main_site/welcome.html',{})
