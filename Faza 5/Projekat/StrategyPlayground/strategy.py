import os

from django import forms
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from StrategyPlayground.models import Strategija, Simulacija


class NovaStrategijaForma(forms.Form):
    ime_fajla = forms.CharField(
        label="Naziv",
        required=True,
        widget=forms.TextInput(attrs={})
    )


def delete_strat(request):
    if request.method == 'POST' and request.POST['id']:
        Simulacija.objects.filter(id_strat=request.POST['id']).delete()

        strategija = Strategija.objects.filter(id_strat=request.POST['id']).first()
        if os.path.exists(strategija.imefajla):
            os.remove(strategija.imefajla)
        strategija.delete()
        return redirect('pregled_strategija')
    else:
        return JsonResponse({'msg': 'los zahtev'}, status=400)


class PregledStrategija(View):
    template = 'pregled_strategija.html'

    def get(self, request):
        context = {
            'strategije': Strategija.objects.filter(
                idkor=request.user.idkor
            ),
            'forma': NovaStrategijaForma()
        }
        return render(request, self.template, context=context)

    def post(self, request):
        context = {
            'strategije': Strategija.objects.filter(
                idkor=request.user.idkor
            ),
            'forma': NovaStrategijaForma()
        }

        if not request.POST['ime_fajla']:
            context['error'] = 'Naziv nije unet!'
        elif request.POST['ime_fajla'] in [str(strat) for strat in context['strategije']]:
            context['error'] = 'Naziv mora biti jedinstven'
        else:
            user_folder = request.user.email.replace('@', '_')

            valid = True
            for char in ['/', '\\', ':', '"', '<', '>', '|', '?', '*']:
                if char in request.POST['ime_fajla']:
                    valid = False
                    break

            if not valid:
                context['error'] = 'Naziv ne sme sadržati < > : / \\ | ? *'
            else:
                putanja = os.getcwd() + \
                           '\\StrategyPlayground\\static\\' + \
                           user_folder + \
                           '\\strategije\\'

                if not os.path.exists(putanja):
                    os.makedirs(putanja)

                ime_fajla = request.POST['ime_fajla']
                if not ime_fajla.endswith('.py'):
                    ime_fajla += '.py'
                imefajla = putanja + ime_fajla

                file = open(imefajla.replace('\\\\', '\\'), 'w+')
                code = 'class Strategy:\n\tdef process_tick(self, tick, buy, sell):\n\t\t# Process code\n'
                file.write(code)
                file.close()

                strategija = Strategija(
                    idkor=request.user,
                    imefajla=imefajla
                )
                strategija.save()
                context['strategije'] = Strategija.objects.filter(
                    idkor=request.user.idkor
                )

        return render(request, self.template, context=context)


class StrategijaView(View):
    template = 'strategija.html'

    def get(self, request, id_strat):
        strategija = Strategija.objects.filter(id_strat=id_strat).first()
        if not strategija:
            return JsonResponse({'msg': 'strategija ne postoji'}, status=400)

        try:
            file = open(strategija.imefajla, "r")
            code = file.read()
            file.close()

            context = {
                'strategija': strategija,
                'code': code
            }
            return render(request, self.template, context)

        except FileNotFoundError:
            return JsonResponse({'msg': 'fajl ne postoji!'}, status=400)

    def post(self, request, id_strat):
        if not request.POST['code']:
            return JsonResponse({'msg': 'nema prilozenog sadrzaja!'}, status=400)

        strategija = Strategija.objects.filter(id_strat=id_strat).first()
        if not strategija:
            return JsonResponse({'msg': 'strategija ne postoji'}, status=400)

        try:
            file = open(strategija.imefajla, "w")
            file.truncate(0)
            file.writelines(request.POST['code'].split('\n'))
            file.close()

            context = {
                'strategija': strategija,
                'code': request.POST['code'],
                'saved': True
            }
            return render(request, self.template, context)

        except FileNotFoundError:
            return JsonResponse({'msg': 'fajl ne postoji!'}, status=400)
