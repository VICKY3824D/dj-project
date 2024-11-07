from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request -> response
# request handler
# action

# def sapa(request):
#     # pull data form db
#     # trasform
#     # send email
    
#     return HttpResponse('Hello Cuyyy ');

def salam(request):
    return render(request, 'hello.html', {'asma' : 'Rohmat'});
