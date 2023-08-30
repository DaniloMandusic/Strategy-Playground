import json
import requests

from django import forms
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from StrategyPlayground.models import Podaciotrzistu, RangLista, Strategija, Simulacija


class StatusPrikaz:
    def __init__(self, simulacija):
        self.id = simulacija.id_sim
        self.ime = simulacija.ime
        parsed_status = json.loads(simulacija.status)

        self.status = parsed_status['status']
        if self.status == 'failure':
            self.msg = parsed_status['msg']
        elif self.status == 'success':
            self.score = parsed_status['score']
            self.open_pos = parsed_status['open_positions']
            self.closed_pos = parsed_status['closed_positions']

        # TODO: Statovi uspesne simulacije


@csrf_exempt
def delete_sim(request):
    if request.method == 'POST' and request.POST['id']:
        Simulacija.objects.filter(id_sim=request.POST['id']).delete()
        return redirect('simulacija')
    else:
        return JsonResponse({'msg': 'los zahtev'}, status=400)


@csrf_exempt
def set_sim_status(request):
    if request.method == 'POST' and request.POST['id'] and request.POST['status']:
        print(request.POST)
        simulacija = Simulacija.objects.filter(id_sim=request.POST['id']).first()
        simulacija.status = request.POST['status']
        simulacija.save()
        return JsonResponse({'msg': 'OK'})
    else:
        return JsonResponse({'msg': 'los zahtev'}, status=400)


class SimulacijaForm(forms.Form):
    ime = forms.CharField(
        label='Naziv simulacije',
        required=False,
        widget=forms.TextInput(attrs={})
    )

    tipovi_podataka = forms.ChoiceField(
        label='Tip simulacije',
        required=False,
        widget=forms.Select(attrs=
                            {'class': 'form-select'}
                            ),
        choices=[
            ("Moji podaci", "Moji podaci"),
            ("Rang liste", "Rang liste")
        ])

    rang_liste = forms.ModelChoiceField(
        queryset=RangLista.objects.all(),
        label='Podaci za simuliranje',
        required=False,
        widget=forms.Select(attrs=
                            {'class': 'form-select'}
                            )
    )

    def __init__(self, korisnik):
        super().__init__()

        self.fields['moji_podaci'] = forms.ModelChoiceField(
            queryset=Podaciotrzistu.objects.filter(idkor=korisnik.idkor),
            label='Podaci za simuliranje',
            required=False,
            widget=forms.Select(attrs=
                                {'class': 'form-select'}
                                )
        )

        self.fields['strategije'] = forms.ModelChoiceField(
            queryset=Strategija.objects.filter(idkor=korisnik.idkor),
            label='Strategija',
            required=False,
            widget=forms.Select(attrs=
                                {'class': 'form-select'}
                                )
        )

    def is_valid(self):
        return True


class SimulacijaView(View):
    template = 'simulacija.html'
    sim_url = 'http://127.0.0.1:8001/'

    def get(self, http_request):
        simulacije = Simulacija.objects.filter(id_strat__in=
                                               Strategija.objects.filter(idkor=http_request.user.idkor))
        forma = SimulacijaForm(http_request.user)
        return render(http_request, self.template, {'forma': forma,
                                                    'simulacije': [StatusPrikaz(simulacija)
                                                                   for simulacija in simulacije]
                                                    })

    def post(self, http_request):
        simulacije = Simulacija.objects.filter(id_strat__in=
                                               Strategija.objects.filter(idkor=http_request.user.idkor))
        forma = SimulacijaForm(http_request.user)
        error = None
        podaci = None
        strategija = None
        ime = None
        losi_parametri = 'Parametri simulacije nisu izabrani.'

        if http_request.POST['ime']:
            postojeca_imena = [sim.ime for sim in simulacije]
            if http_request.POST['ime'] in postojeca_imena:
                error = 'Ime vec postoji'
            else:
                ime = http_request.POST['ime']
        else:
            error = losi_parametri

        if http_request.POST['strategije']:
            strategija = Strategija.objects.filter(id_strat=http_request.POST['strategije']).first()
            if not strategija:
                error = losi_parametri
        else:
            error = losi_parametri

        if not error and http_request.POST['tipovi_podataka'] == 'Moji podaci':
            if http_request.POST['moji_podaci']:
                podaci = Podaciotrzistu.objects.filter(idpodtr=http_request.POST['moji_podaci']).first()
                if not podaci:
                    error = losi_parametri
            else:
                error = losi_parametri

        if not error and http_request.POST['tipovi_podataka'] == 'Rang liste':
            if http_request.POST['rang_liste']:
                podaci = Podaciotrzistu.objects.filter(
                    idpodtr=RangLista.objects.filter(id_rangliste=http_request.POST['rang_liste']).first().id_pod.idpodtr
                ).first()
                print(RangLista.objects.filter(id_rangliste=http_request.POST['rang_liste']).first().id_pod.idpodtr)
                if not podaci:
                    error = losi_parametri
            else:
                error = losi_parametri

        if podaci and strategija and ime:
            nova_simulacija = Simulacija(ime=ime,
                                         id_pod_tr=podaci,
                                         id_strat=strategija,
                                         status=json.dumps({
                                             'status': 'pending'
                                         }))
            nova_simulacija.save()

            try:
                body = {
                    'id': nova_simulacija.id_sim,
                    'csv_path': podaci.imefajla,
                    'module_path': strategija.imefajla
                }
                response = requests.post(self.sim_url + 'backtest/', data=json.dumps(body))

                if response.status_code != 200:
                    error = 'Greška čitanju podataka ili strategije.'
                    nova_simulacija.delete()

            except Exception:
                error = 'Problem sa serverom za simuliranje.'
                nova_simulacija.delete()

        simulacije = Simulacija.objects.filter(id_strat__in=
                                               Strategija.objects.filter(idkor=http_request.user.idkor))

        return render(http_request, self.template, {
            'forma': forma,
            'error': error,
            'success': True,
            'simulacije': [StatusPrikaz(simulacija)
                           for simulacija in simulacije]
        })
