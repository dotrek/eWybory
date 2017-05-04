from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404

from .models import Kandydat, Wybory


# Create your views here


def results(request, kandydat_id):
    return HttpResponse("Result for: " % kandydat_id)


def vote(request, kandydat_id):
    return HttpResponse("You're voting on question %s." % kandydat_id)


def home(request):
    latest_question_list = Wybory.objects.order_by('-typ')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    # output = ', '.join([str(q.id) for q in latest_question_list])
    return render_to_response('home.html', context)


def detail(request, kandydat_id):
    kandydat = get_object_or_404(Kandydat, pk=kandydat_id)
    return render_to_response('detail.html', {'kandydat': kandydat})


def detail_wybory(request, wybory_id):
    wybory = get_object_or_404(Wybory, pk=wybory_id)
    kandydat_list = Kandydat.objects.filter(wybory_id=wybory_id).order_by('nazwisko')[:5]
    context = {
        'wybory': wybory,
        'kandydat_list': kandydat_list,
    }
    return render_to_response('detail_wybory.html', context)

