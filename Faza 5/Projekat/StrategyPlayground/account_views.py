from django.contrib.auth import login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from StrategyPlayground.forms import UserRegistrationForm, UpdateForm
from StrategyPlayground.models import Korisnik, RegistrationRequest

def user_login_(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if RegistrationRequest.objects.filter(email=email).exists():
            messages.info(request, "Vaš zahtev je već poslat, molimo sačekajte da vas administrator odobri.")
            return redirect('login')

        if email and password:  # Dodata provera da li su email i lozinka uneti
            if Korisnik.objects.filter(email=email).exists():
                korisnik = Korisnik.objects.get(email=email)
                if korisnik.check_password(password):
                    login(request, korisnik)
                    return redirect('/moj_profil/')
                else:
                    messages.info(request, "Neispravna lozinka")
                    return redirect('login')

        messages.info(request, "Korisnik sa unetom email adresom ne postoji. Molimo Vas napravite profil.")
        return redirect('login')

    return render(request, 'login.html')
def registration_(request):
    template = 'registration.html'
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            ime = form.cleaned_data['ime']
            prezime = form.cleaned_data['prezime']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']

            if Korisnik.objects.filter(email=email).exists():  # Provera da li već postoji korisnik sa istim emailom
                messages.info(request, "Već postoji korisnik sa unetim e-mailom.")
                return redirect('registration')

            if RegistrationRequest.objects.filter(email=email).exists(): # Provera da li već postoji zahtev sa istim emailom
                messages.info(request, "Vaš zahtev je već poslat, molimo sačekajte da vas administrator odobri.")
                return redirect('registration')

            registration_request = RegistrationRequest.objects.create(
                ime=ime,
                prezime=prezime,
                email=email,
                password=password
                )
            registration_request.save()

            #user = form.save()
            #login(request, user)  # Prijava korisnika nakon registracije

            messages.success(request, 'Zahtev za registraciju je uspešno poslat. Molimo sačekajte odobrenje od strane administratora.')
            return redirect('registration')

        else:
            print(form.errors)
    else:
        form = UserRegistrationForm()

    return render(request, template, {'form': form})


def approve_registration_(request, request_id):
    try:
        registration_request = RegistrationRequest.objects.get(id=request_id)
        # Kreiraj novog korisnika sa podacima iz zahteva
        #password = make_password(registration_request.password)
        korisnik_data = {
            'ime': registration_request.ime,
            'prezime': registration_request.prezime,
            'email': registration_request.email,
            'password': registration_request.password,
            'status': 'Approved',
        }
        korisnik = Korisnik.objects.create_user(**korisnik_data)
        registration_request.odobren = True
        registration_request.save()
        registration_request.delete()

        messages.success(request, f"Zahtev za registraciju korisnika {korisnik.email} je prihvaćen.")
    except RegistrationRequest.DoesNotExist:
        messages.error(request, "Zahtev za registraciju ne postoji.")
    return redirect('registration_requests')

def approve_registration_panel_(request, request_id):
    try:
        registration_request = RegistrationRequest.objects.get(id=request_id)
        # Kreiraj novog korisnika sa podacima iz zahteva
        #password = make_password(registration_request.password)
        korisnik_data = {
            'ime': registration_request.ime,
            'prezime': registration_request.prezime,
            'email': registration_request.email,
            'password': registration_request.password,
            'status': 'Approved',
        }
        korisnik = Korisnik.objects.create_user(**korisnik_data)
        registration_request.odobren = True
        registration_request.save()
        registration_request.delete()

        messages.success(request, f"Zahtev za registraciju korisnika {korisnik.email} je prihvaćen.")
    except RegistrationRequest.DoesNotExist:
        messages.error(request, "Zahtev za registraciju ne postoji.")
    return redirect('admin:StrategyPlayground_registrationrequest_changelist')

def reject_registration_(request, request_id):
    print("usao u reject")
    try:
        registration_request = RegistrationRequest.objects.get(id=request_id)
        # Obriši zahtev za registraciju
        registration_request.delete()
        messages.success(request, f"Zahtev za registraciju korisnika {registration_request.email} je odbijen.")
    except RegistrationRequest.DoesNotExist:
        messages.error(request, "Zahtev za registraciju ne postoji.")
    return redirect('registration_requests')

def reject_registration_panel_(request, request_id):
    print("usao u reject")
    try:
        registration_request = RegistrationRequest.objects.get(id=request_id)
        # Obriši zahtev za registraciju
        registration_request.delete()
        messages.success(request, f"Zahtev za registraciju korisnika {registration_request.email} je odbijen.")
    except RegistrationRequest.DoesNotExist:
        messages.error(request, "Zahtev za registraciju ne postoji.")
    return redirect('admin:StrategyPlayground_registrationrequest_changelist')


def registration_requests_(request):

    if request.method == 'POST':
        if 'approve' in request.POST:
            request_id = request.POST['approve']
            return approve_registration_(request, request_id)
        elif 'reject' in request.POST:
            request_id = request.POST['reject']
            return reject_registration_(request, request_id)

    registration_requests = RegistrationRequest.objects.all()

    context = {
        'registration_requests': registration_requests
    }

    return render(request, 'registration_requests.html', context)

def user_logout_(request):
    logout(request)
    return render(request, 'logout.html')

def updateinformations_(request):

    if request.method == 'POST':
        ime = request.POST['ime']
        prezime = request.POST['prezime']
        if not ime or not prezime:
            messages.error(request, 'Unesite ispravne podatke')
        else:
            korisnik = get_object_or_404(Korisnik, email=request.user.email)
            korisnik.ime = ime
            korisnik.prezime = prezime
            korisnik.save()

        return redirect('moj_profil')

