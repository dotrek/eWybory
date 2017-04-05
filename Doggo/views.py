from django.http import HttpResponse


# Create your views her

def index(request):
    return HttpResponse("Hello world!")
