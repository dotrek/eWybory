from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Kandydat, Wybory, Glosujacy, Glos


# Create your views here


class ResultsView(generic.DetailView):
    model = Wybory
    template_name = ''


def vote(request, wybory_id):
    wybory = get_object_or_404(Wybory, pk=wybory_id)
    try:

        selected_choice = get_object_or_404(Kandydat, pk=request.POST['choice'])
        user = Glosujacy.objects.filter(pesel=request.POST['pesel'])
        if user.exists():
            glos = Glos.objects.filter(wybory=wybory, glosujacy=user)
            if glos.exists():
                return render_to_response(request, 'detail_wybory.html', {
                    'error_message': "Ta osoba juz glosowala w tych wyborach"
                })
            else:
                glos.wybory = wybory
                glos.glosujacy = user
                glos.save()
                selected_choice.licznik += 1
                selected_choice.save()
                return HttpResponseRedirect(reverse('Doggo:results', args=(wybory.id,)))
        else:
            return render_to_response(request, 'detail_wybory.html', {
                'error_message': "Pesel nie znajduje sie w bazie glosujacych"
            })
    except (KeyError, Kandydat.DoesNotExist):
        return render_to_response(request, 'detail_wybory.html', {
            'kandydat': selected_choice,
            'error_message': "Nie wybrales kandydata.",
        })
    # except user.DoesNotExist:
    #     return render_to_response(request, 'detail_wybory.html', {
    #         'error_message': "Pesel nie znajduje sie w bazie glosujacych"
    #     })
    # else:
    #     glos.wybory = wybory
    #     glos.glosujacy = user
    #     glos.save()
    #     selected_choice.licznik += 1
    #     selected_choice.save()
    #     return HttpResponseRedirect(reverse('Doggo:results', args=(wybory.id,)))


class HomeView(generic.ListView):
    template_name = 'home.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Wybory.objects.all()


class DetailView(generic.DetailView):
    model = Kandydat
    template_name = 'detail.html'


def detail_wybory(request, wybory_id):
    wybory = get_object_or_404(Wybory, pk=wybory_id)
    kandydat_list = Kandydat.objects.filter(wybory_id=wybory_id).order_by('nazwisko')[:5]
    context = {
        'wybory': wybory,
        'kandydat_list': kandydat_list,
    }
    return render_to_response('detail_wybory.html', context)


def results(request, wybory_id):
    wybory = get_object_or_404(Wybory, pk=wybory_id)
    kandydat_list = Kandydat.objects.filter(wybory_id=wybory_id).order_by('nazwisko')[:5]
    context = {
        'wybory': wybory,
        'kandydat_list': kandydat_list,
    }
    return render_to_response('results.html', context)
