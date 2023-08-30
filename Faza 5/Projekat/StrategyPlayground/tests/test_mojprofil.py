from django.test import TestCase

from StrategyPlayground.models import Korisnik


class UpdateInformationsTest(TestCase):
    def setUp(self):
        self.korisnik = Korisnik.objects.create_user(email='test@gmail.com', password='testpassword',
                                                     ime='Test korisnik', prezime='Test Prezime')

    def test_update_informations_success(self):
        self.client.login(email='test@gmail.com', password='testpassword')

        response = self.client.post('/moj_profil/updateinformations/', {
            'ime': 'Novo ime',
            'prezime': 'Novo prezime'
        }, follow=True)

        self.korisnik.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.korisnik.ime, 'Novo ime')
        self.assertEqual(self.korisnik.prezime, 'Novo prezime')

    def test_update_informations_invalid_data1(self):
        self.client.login(email='test@gmail.com', password='testpassword')
        response = self.client.post('/moj_profil/updateinformations/', {
            'ime': '',
            'prezime': 'Novo prezime'

        }, follow=True)
        self.korisnik.refresh_from_db()
        self.assertNotEqual(self.korisnik.ime, '')
        self.assertNotEqual(self.korisnik.prezime, 'Novo prezime')
        self.assertContains(response, 'Unesite ispravne podatke')

    def test_update_informations_invalid_data2(self):
        self.client.login(email='test@gmail.com', password='testpassword')
        response = self.client.post('/moj_profil/updateinformations/', {
            'ime': 'imetest',
            'prezime': ''

        }, follow=True)
        self.korisnik.refresh_from_db()
        self.assertNotEqual(self.korisnik.ime, 'imetest')
        self.assertNotEqual(self.korisnik.prezime, '')
        self.assertContains(response, 'Unesite ispravne podatke')

    def test_update_ime_success(self):
        self.client.login(email='test@gmail.com', password='testpassword')
        self.client.post('/moj_profil/updateinformations/', {
            'ime': 'Novo ime',
            'prezime': 'Test Prezime'
        }, follow=True)

        self.korisnik.refresh_from_db()
        self.assertEqual(self.korisnik.ime, 'Novo ime')
        self.assertEqual(self.korisnik.prezime, 'Test Prezime')
