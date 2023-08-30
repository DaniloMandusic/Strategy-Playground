"""
URL configuration for Projekat project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from StrategyPlayground import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from StrategyPlayground.rang_lista import RangListaPregledView, rang_lista_single
from StrategyPlayground.strategy import StrategijaView, PregledStrategija, delete_strat
from StrategyPlayground.views import registration_requests
from StrategyPlayground.simulacija import SimulacijaView, delete_sim, set_sim_status

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index.as_view(), name='index'),

    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('registration/', views.registration, name='registration'),
    # path('registration_success/', views.registration, name='registration_success'),

    path('approve-registration-panel/<int:request_id>/', views.approve_registration_panel,
         name='approve_registration_panel'),
    path('reject-registration-panel/<int:request_id>/', views.reject_registration_panel,
         name='reject_registration_panel'),

    path('moj_profil/', views.MojProfil.as_view(), name='moj_profil'),
    path('moj_profil/updateinformations/', views.updateinformations, name='updateinformations'),

    path('prikaz_informacija/', views.PrikazInformacija, name='prikaz_informacija'),
    path('pregled_strategija/', PregledStrategija.as_view(), name='pregled_strategija'),
    # path('otvorena_strategija/', views.OtvorenaStrategija.as_view(), name='otvorena_strategija'),
    path('strategija/<int:id_strat>', StrategijaView.as_view(), name='strategija'),
    path('delete-strat/', delete_strat, name='delete-strat'),
    path('docs/', views.Docs.as_view(), name='docs'),
    path('simulacija/', SimulacijaView.as_view(), name='simulacija'),
    path('delete-sim/', delete_sim, name='delete-sim'),
    path('set-sim-status/', set_sim_status, name='set-sim-status'),

    path('registration_requests/', views.registration_requests, name='registration_requests'),

    path('rang-liste/', RangListaPregledView.as_view(), name='rang_lista'),
    path('rang-lista/<int:id_rang_liste>', rang_lista_single, name='rang_lista_single'),

]

urlpatterns += staticfiles_urlpatterns()
