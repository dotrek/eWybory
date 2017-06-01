from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Kandydat, Wybory, Glos, Glosujacy


# Create your views here


class ResultsView(generic.DetailView):
    model = Wybory
    template_name = ''


def vote(request, wybory_id):
    wybory = get_object_or_404(Wybory, pk=wybory_id)
    kandydat_list = Kandydat.objects.filter(wybory_id=wybory_id).order_by('nazwisko')[:5]
    context = {
        'error_message': "Pesel nie znajduje sie w bazie glosujacych",
    }
    try:

        selected_choice = get_object_or_404(Kandydat, pk=request.POST['choice'])
        user = Glosujacy.objects.get(pesel=request.POST['pesel'])
    except (KeyError, Kandydat.DoesNotExist):
        return render(request, 'detail_wybory.html', context)
    except (UnboundLocalError, Glosujacy.DoesNotExist):
        return render(request, 'detail_wybory.html', context)
    else:
        try:
            query = Glos.objects.filter(wybory=wybory)
            glos = get_object_or_404(query, glosujacy=user)
        except glos.DoesNotExist:
            glos.wybory = wybory
            glos.glosujacy = user
            glos.save()
            selected_choice.licznik += 1
            selected_choice.save()
            return HttpResponseRedirect(reverse('Doggo:results', args=(wybory.id,)))
        else:
            return render(request, 'detail_wybory.html', {
                'error_message': "Ta osoba juz glosowala w tych wyborach"
            })


class HomeView(generic.ListView):
    template_name = 'home.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Wybory.objects.all()


class DetailView(generic.DetailView):
    model = Kandydat
    template_name = 'creators.html'


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


def creatorsview(request):
    creators = {"Marek Jakubowski", "Piotr Otapowicz", "Karol Wojciula"}
    context = {'creators': creators}
    return render_to_response("creators.html", context)
