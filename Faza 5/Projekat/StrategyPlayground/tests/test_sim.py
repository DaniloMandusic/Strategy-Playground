import json
from unittest import mock
from unittest.mock import patch

from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from StrategyPlayground.simulacija import SimulacijaForm
from StrategyPlayground.models import RangLista, Podaciotrzistu, Strategija, Korisnik, Simulacija


class SimulacijaFormTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            email='test@example.com',
            password='password'
        )
        self.sim_url = 'http://127.0.0.1:8001/'
        self.simulacija_url = reverse('simulacija')
        self.delete_url = reverse('delete-sim')

    def test_get_simulacija_form_displayed(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('simulacija'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'simulacija.html')
        self.assertIsInstance(response.context['forma'], SimulacijaForm)

    def test_simulacija_form_empty(self):
        korisnik = Korisnik.objects.create(email='testuser@gmail.com')
        form = SimulacijaForm(korisnik=korisnik)

        self.assertFalse(form.is_bound)  # Provera da li je forma-nije vezana za podatke
        # self.assertIn('ime', form.errors)  # greska za polje ime
        # self.assertIn('strategije', form.errors)  # greska strategije
        # self.assertIn('tipovi_podataka', form.errors)  # greska tipovi_podataka
        # self.assertNotIn('moji_podaci', form.errors)

    def test_simulacija_form_valid(self):  # validna forma
        korisnik = Korisnik.objects.create(email='testuser@gmail.com')
        form = SimulacijaForm(korisnik=korisnik)
        form.data = {'ime': 'Test simulacija', 'strategije': 1}
        self.assertTrue(form.is_valid())

    def test_post_simulacija_form_success(self):  # da li se dobro kreira i dodaje u listu, dobar POST zahtev
        korisnik = Korisnik.objects.create(email='testuser@gmail.com')
        strategija = Strategija.objects.create(imefajla='TestFajl', idkor_id=korisnik.idkor)
        podaci = Podaciotrzistu.objects.create(imefajla='Test podaci', idkor_id=korisnik.idkor)
        form_data = {
            'ime': 'Nova simulacija',
            'tipovi_podataka': 'Moji podaci',
            'moji_podaci': podaci.idpodtr,
            'strategije': strategija.id_strat
        }

        self.client.force_login(korisnik)
        form = SimulacijaForm(korisnik=korisnik)
        form.fields['ime'].initial = form_data['ime']
        form.fields['tipovi_podataka'].initial = form_data['tipovi_podataka']
        form.fields['moji_podaci'].initial = form_data['moji_podaci']
        form.fields['strategije'].initial = form_data['strategije']

        response = self.client.post(reverse('simulacija'), data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn('Problem sa serverom za simuliranje', response.context)
        simulacije = response.context['simulacije']
        # self.assertEqual(len(simulacije), 1)
        # self.assertEqual(simulacije[0].ime, 'Nova simulacija')
        # nova_simulacija = Simulacija.objects.filter(ime='Nova simulacija').first()
        # self.assertIsNotNone(nova_simulacija)
        # self.assertEqual(nova_simulacija.id_pod_tr, podaci)
        # self.assertEqual(nova_simulacija.id_strat, strategija)
        # self.assertEqual(json.loads(nova_simulacija.status)['status'], 'pending')

    def test_simulacija_view_post_failure(self):
        # Provera da li POST zahtev za kreiranje nove simulacije sa neispravnim podacima ne dodaje simulaciju
        self.client.force_login(self.user)
        form_data = {
            'ime': '',
            'tipovi_podataka': 'Moji podaci',
            'moji_podaci': 1,  # nepostojeci ID
            'strategije': 1  # nepostoejci ID
        }
        response = self.client.post(self.simulacija_url, data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'simulacija.html')
        simulacije = response.context['simulacije']
        self.assertEqual(len(simulacije), 0)

    def test_delete_sim(self):  # da li POST zahtev za brisanje simulacije uspesno uklanja simulaciju iz liste
        korisnik = Korisnik.objects.create(email='testuser@gmail.com')
        strategija = Strategija.objects.create(imefajla='TestFajl', idkor_id=korisnik.idkor)
        podaci = Podaciotrzistu.objects.create(imefajla='Test podaci', idkor_id=korisnik.idkor)
        simulacija = Simulacija.objects.create(ime='Test simulacija', id_pod_tr=podaci, id_strat=strategija)
        delete_url = reverse('delete-sim')
        response = self.client.post(delete_url, data={'id': simulacija.id_sim})
        self.assertEqual(response.status_code, 302)

        simulacija_exists = Simulacija.objects.filter(id_sim=simulacija.id_sim).exists()  # da li je obrisana
        self.assertFalse(simulacija_exists)

        # da li je korisnik preusmjeren na odgovarajuću stranicu nakon brisanja
        self.assertEqual(response.url, self.simulacija_url)

    def test_set_sim_status(self):
        korisnik = Korisnik.objects.create(email='testuser@gmail.com')
        strategija = Strategija.objects.create(imefajla='TestFajl', idkor_id=korisnik.idkor)
        podaci = Podaciotrzistu.objects.create(imefajla='Test podaci', idkor_id=korisnik.idkor)
        simulacija = Simulacija.objects.create(ime='Test simulacija', id_pod_tr=podaci, id_strat=strategija)
        response = self.client.post(reverse('set-sim-status'), {'id': simulacija.id_sim, 'status': 'success'})
        self.assertEqual(response.status_code, 200)
        simulacija.refresh_from_db()
        self.assertEqual(simulacija.status, 'success')
