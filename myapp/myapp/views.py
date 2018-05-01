from django.http import HttpRespones

def index(request):
	return HttpRespones("Hello world")