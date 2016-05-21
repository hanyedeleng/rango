from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage':"I am bold font from the context"}

    return render(request, 'rango/index.html', context_dict)

def about(request):
	new_context_dict = {'boldmessage':"I am the king of birds"}

	return render(request, 'rango/about.html', new_context_dict)
