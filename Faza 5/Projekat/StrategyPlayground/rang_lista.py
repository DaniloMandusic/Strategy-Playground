import json

from django import forms
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from .models import RangLista, Podaciotrzistu, Simulacija, Korisnik, Strategija


class RangListaForm(forms.Form):
    ime = forms.CharField(
        label='Naziv',
        required=False,
        widget=forms.TextInput(attrs={})
    )

    def __init__(self, korisnik):
        super().__init__()

        self.fields['podaci'] = forms.ModelChoiceField(
            queryset=Podaciotrzistu.objects.filter(idkor=korisnik.idkor),
            label='Podaci za simuliranje',
            required=False,
            widget=forms.Select(attrs=
                                {'class': 'form-select'}
                                )
        )


class RangListaPregledView(View):
    template = 'rang_lista_pregled.html'

    def get(self, request):
        rang_liste = RangLista.objects.all()
        context = {'rang_liste': rang_liste}

        if request.user.is_superuser:
            context['forma'] = RangListaForm(request.user)

        return render(request, self.template, context=context)

    def post(self, request):
        rang_liste = RangLista.objects.all()
        context = {'rang_liste': rang_liste}

        if request.POST['ime'] and request.POST['podaci']:
            if request.POST['ime'] in [rang_lista.naziv for rang_lista in rang_liste]:
                context['error'] = 'Naziv rang liste mora biti jedinstven!'
            else:
                podaci = Podaciotrzistu.objects.filter(idpodtr=request.POST['podaci'])
                if not podaci:
                    return JsonResponse({'msg': 'podaci ne postoje!'}, status=400)

                rang_lista = RangLista(naziv=request.POST['ime'], id_pod=podaci.first())
                rang_lista.save()

                rang_liste = RangLista.objects.all()
                context = {'rang_liste': rang_liste}
        else:
            context['error'] = 'Podaci nisu ispravni!'

        if request.user.is_superuser:
            context['forma'] = RangListaForm(request.user)

        return render(request, self.template, context=context)


class Rang:
    def __init__(self, simulacija):
        status = json.loads(simulacija.status)

        self.score = status['score']
        self.korisnik = Korisnik.objects.filter(
            idkor=simulacija.id_strat.idkor.idkor
        ).first()
        self.strategija = str(Strategija.objects.filter(
            id_strat=simulacija.id_strat.id_strat
        ).first())
        self.broj = 0


def rang_lista_single(request, id_rang_liste):
    if request.method == 'GET':
        context = {}

        rang_lista = RangLista.objects.filter(id_rangliste=id_rang_liste).first()
        if not rang_lista:
            return JsonResponse({'msg': 'nepostojeca rang lista'}, status=400)

        context['naziv'] = rang_lista.naziv
        simulacije = Simulacija.objects.filter(id_pod_tr=rang_lista.id_pod)
        simulacije = [sim for sim in simulacije if json.loads(sim.status)['status'] == 'success']

        redovi = [Rang(sim) for sim in simulacije]
        redovi.sort(key=lambda red: red.score, reverse=True)

        filtrirani_redovi = []
        korisnici = []
        spot = 1
        for i in range(len(redovi)):
            if redovi[i].korisnik not in korisnici:
                redovi[i].broj = spot
                spot += 1
                korisnici.append(redovi[i].korisnik)
                filtrirani_redovi.append(redovi[i])

        redovi = filtrirani_redovi
        context['redovi'] = redovi

        return render(request, 'rang_lista.html', context=context)
    else:
        return JsonResponse({'msg': 'los zahtev'}, status=400)
