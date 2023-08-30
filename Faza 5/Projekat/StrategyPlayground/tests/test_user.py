from django.test import TestCase

from StrategyPlayground.models import Korisnik, RegistrationRequest


class UserRegistration(TestCase):
    def setUp(self):
        self.email = 'testuser@gmail.com'
        self.strong_password = 'this.is.a.strong.p@ssw0rd'

    def test_successful_registration(self):
        response = self.client.post('/registration/', {
            'ime': 'pera',
            'prezime': 'peric',
            'email': self.email,
            'password1': self.strong_password,
            'password2': self.strong_password,
        }, follow=True)

        messages = list(response.context['messages'])
        self.assertEqual(str(messages[0]), 'Zahtev za registraciju je uspešno poslat. '
                                           'Molimo sačekajte odobrenje od strane administratora.')

    def test_missing_data(self):
        response = self.client.post('/registration/', {
            'ime': '',
            'prezime': 'peric',
            'email': self.email,
            'password1': self.strong_password,
            'password2': self.strong_password,
        })

        self.assertContains(response, 'ime')
        self.assertContains(response, "This field is required.")

    def test_registration_already_pending(self):
        self.client.post('/registration/', {
            'ime': 'zika',
            'prezime': 'zikic',
            'email': self.email,
            'password1': self.strong_password,
            'password2': self.strong_password,
        }, follow=True)
        response = self.client.post('/registration/', {
            'ime': 'zika',
            'prezime': 'zikic',
            'email': self.email,
            'password1': self.strong_password,
            'password2': self.strong_password,
        }, follow=True)

        messages = list(response.context['messages'])
        self.assertEqual(str(messages[0]), 'Vaš zahtev je već poslat, molimo sačekajte da vas administrator odobri.')

    def test_user_already_exists(self):
        Korisnik.objects.create_user(email=self.email, password=self.strong_password)
        response = self.client.post('/registration/', {
            'ime': 'pera',
            'prezime': 'peric',
            'email': self.email,
            'password1': self.strong_password,
            'password2': self.strong_password,
        }, follow=True)

        self.assertContains(response, 'Korisnik with this Email already exists.')

    def test_weak_password(self):
        response = self.client.post('/registration/', {
            'ime': 'pera',
            'prezime': 'peric',
            'email': self.email,
            'password1': '12345',
            'password2': '12345',
        }, follow=True)

        self.assertContains(response, 'This password is too short. It must contain at least 8 characters.')
        self.assertContains(response, 'This password is too common.')
        self.assertContains(response, 'This password is entirely numeric.')

    def test_password_missmatch(self):
        response = self.client.post('/registration/', {
            'ime': 'pera',
            'prezime': 'peric',
            'email': self.email,
            'password1': self.strong_password,
            'password2': '12345',
        }, follow=True)

        self.assertContains(response, 'Sifre se ne podudaraju!')


class UserLogin(TestCase):
    def setUp(self):
        Korisnik.objects.create_user(email='pera@gmail.com', password='12345')

    def test_successfun_login(self):
        response = self.client.post('/login/', {
            'email': 'pera@gmail.com',
            'password': '12345'
        }, follow=True)

        self.assertRedirects(response, '/moj_profil/')

    def test_pending_login(self):
        RegistrationRequest.objects.create(
            email='newuser@example.com',
            password='password123',
        )

        response = self.client.post('/login/', {
            'email': 'newuser@example.com',
            'password': 'password123'
        }, follow=True)

        self.assertContains(response, 'Vaš zahtev je već poslat, molimo sačekajte da vas administrator odobri.')

    def test_unknown_user(self):
        response = self.client.post('/login/', {
            'email': 'unknown_user@example.com',
            'password': 'password123'
        }, follow=True)

        self.assertContains(response, 'Korisnik sa unetom email adresom ne postoji. Molimo Vas napravite profil.')

    def test_wrong_password(self):
        response = self.client.post('/login/', {
            'email': 'pera@gmail.com',
            'password': 'wrong_password'
        }, follow=True)

        self.assertContains(response, 'Neispravna lozinka')
