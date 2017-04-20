from django.http import HttpResponse
from django.template import loader

from .models import Kandydat


# Create your views her

def details(request, kandydat_id):
    return HttpResponse("Details of: " % kandydat_id)


def results(request, kandydat_id):
    return HttpResponse("Result for: " % kandydat_id)


def home(request):
    latest_question_list = Kandydat.objects.order_by('-imie')[:5]
    template = loader.get_template('home.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    # output = ', '.join([str(q.id) for q in latest_question_list])
    return HttpResponse(template.render(context, request))
