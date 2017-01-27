from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #Constructs a dictionary to pass to the template as context
    #boldmessage is the same as {{boldmessage}} in the template
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}

    #Returns a rendered response to send to the client
    #Shortcut function makes our lives easier
    #First parameter is the template we wish to use
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict_about = {'boldmessage': "This tutorial has been put together by Andrew McGeechan"}
    return render(request, 'rango/about.html', context=context_dict_about)