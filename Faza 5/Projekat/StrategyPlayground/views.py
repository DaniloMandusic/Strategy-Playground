from django.views import View

from StrategyPlayground.prikaz_informacija import prikaz_informacija
from StrategyPlayground.account_views import *


# Create your views here.
class Index(View):
    template = 'index.html'
    def get(self, request):
        return render(request, self.template)

def user_login(request):
    return user_login_(request)
def registration(request):
   return registration_(request)

def approve_registration(request, request_id):
    return approve_registration_(request)
def approve_registration_panel(request, request_id):
    return approve_registration_panel_(request, request_id)

def reject_registration(request, request_id):
    return reject_registration_(request, request_id)
def reject_registration_panel(request, request_id):
    return reject_registration_panel_(request, request_id)
def registration_requests(request):
    return registration_requests_(request)
def user_logout(request):
    return user_logout_(request)

def updateinformations(request):
    return updateinformations_(request)
class MojProfil(View):
    template = 'moj_profil.html'

    def get(self, request):
        return render(request, self.template)

def PrikazInformacija(request, ):
    return prikaz_informacija(request)


class PregledStrategija(View):
    template='pregled_strategija.html'

    def get(self, request):
        return render(request, self.template)

class Strategija(View):
    template='strategija.html'

    def get(self, request):
        return render(request, self.template)

class Docs(View):
    template='docs.html'

    def get(self, request):
        return render(request, self.template)


class AdminRangLista2(View):
    template='adminRangLista2.html'

    def get(self, request):
        return render(request, self.template)


