import datetime

from captcha.fields import CaptchaField
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Kandydat, Wybory, Glos, Glosujacy


class CaptchaTestForm(forms.Form):
    captcha = CaptchaField()


# Create your views here


class ResultsView(generic.DetailView):
    model = Wybory
    template_name = ''


def vote(request, wybory_id):
    wybory = get_object_or_404(Wybory, pk=wybory_id)
    kandydat_list = Kandydat.objects.filter(wybory_id=wybory_id).order_by('nazwisko')[:5]
    try:
        selected_choice = get_object_or_404(Kandydat, pk=request.POST['choice'])
        user = Glosujacy.objects.get(pesel=request.POST['pesel'])
        glos = Glos.objects.filter(
            wybory__exact=wybory
        ).filter(
            glosujacy__exact=user
        )

        if glos.count() == 0:
            glos = Glos(wybory=wybory, glosujacy=user)
            glos.save()
            selected_choice.licznik += 1
            selected_choice.save()
            return HttpResponseRedirect(reverse('Doggo:home'))
        else:
            return render(request, 'detail_wybory.html', {
                'wybory': wybory,
                'kandydat_list': kandydat_list,
                'error_message': "Ta osoba juz glosowala w tych wyborach",
            })
    except (KeyError, Glosujacy.DoesNotExist, Kandydat.DoesNotExist):
        return render(request, 'detail_wybory.html', {
            'wybory': wybory,
            'kandydat_list': kandydat_list,
            'error_message': "Pesel nie znajduje sie w bazie glosujacych",
        })


class HomeView(generic.ListView):
    template_name = 'home.html'
    context_object_name = 'home_list'

    def get_queryset(self):
        return Wybory.objects.exclude(
            start_time__gte=datetime.date.today()
        ).filter(
            end_time__gte=datetime.date.today()
        )


class UpcomingView(generic.ListView):
    template_name = 'upcoming.html'
    context_object_name = 'upcoming_list'

    def get_queryset(self):
        return Wybory.objects.filter(
            start_time__gte=datetime.date.today()
        )


class PreviousView(generic.ListView):
    template_name = 'previous.html'
    context_object_name = 'previous_list'

    def get_queryset(self):
        return Wybory.objects.filter(
            end_time__lt=datetime.date.today()
        )


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


def introView(request):
    return render_to_response('intro.html')

def results(request, wybory_id):
    wybory = get_object_or_404(Wybory, pk=wybory_id)
    kandydat_list = Kandydat.objects.filter(wybory_id=wybory_id).order_by('nazwisko')[:5]
    liczba_dopuszczonych = Glosujacy.objects.all().count()
    liczba_glosujacych = Glos.objects.filter(wybory_id=wybory_id).count()
    frekwencja = liczba_glosujacych / liczba_dopuszczonych * 100
    context = {
        'wybory': wybory,
        'kandydat_list': kandydat_list,
        'frekwencja': frekwencja,
    }
    return render_to_response('results.html', context)


def creatorsview(request):
    creators = {"Marek Jakubowski", "Piotr Otapowicz", "Karol Wojciula"}
    context = {'creators': creators}
    return render_to_response("creators.html", context)
