from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin


class KorisnikManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('E-mail adresa mora biti postavljena')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

    def create_korisnik_from_request(request):
        korisnik_data = {
            'ime': request.ime,
            'prezime': request.prezime,
            'email': request.email,
            'password': request.password,
        }
        korisnik = Korisnik.objects.create_user(**korisnik_data)
        korisnik.save()
        return korisnik


class Korisnik(AbstractBaseUser, PermissionsMixin):
    idkor = models.AutoField(db_column='idKor', primary_key=True)
    ime = models.CharField(max_length=20)
    prezime = models.CharField(max_length=20, unique=False)
    email = models.EmailField(max_length=50, unique=True)
    odobren = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True, blank=True)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    status = models.CharField(max_length=10, default='Pending')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['ime', 'prezime']

    def get_full_name(self):
        return f"{self.ime.capitalize()} {self.prezime.capitalize()}"

    objects = KorisnikManager()

    class Meta:
        managed = True
        db_table = 'korisnik'


class RegistrationRequest(models.Model):
    ime = models.CharField(max_length=20)
    prezime = models.CharField(max_length=20)
    password = models.CharField(max_length=100, default="password vrednost")
    email = models.EmailField(max_length=50, unique=True)
    status = models.CharField(max_length=10, default='Pending')

    def get_full_name(self):
        return f"{self.ime.capitalize()} {self.prezime.capitalize()}"

    class Meta:
        verbose_name_plural = 'Registration Requests'

    def __str__(self):
        return self.email


class Podaciotrzistu(models.Model):
    idpodtr = models.AutoField(db_column='idPodTr', primary_key=True)  # Field name made lowercase.
    idkor = models.ForeignKey(Korisnik, models.DO_NOTHING, db_column='idKor')  # Field name made lowercase.
    imefajla = models.CharField(db_column='imeFajla', max_length=150)  # Field name made lowercase.

    def __str__(self):
        # return self.imefajla
        return self.imefajla.split('/')[-1].split('\\')[-1]

    class Meta:
        managed = True
        db_table = 'podaciotrzistu'


class Strategija(models.Model):
    id_strat = models.AutoField(db_column='id_strat', primary_key=True)
    imefajla = models.CharField(db_column='imeFajla', max_length=150)  # Field name made lowercase.
    idkor = models.ForeignKey(Korisnik, models.DO_NOTHING, db_column='idKor')  # Field name made lowercase.

    def __str__(self):
        # return self.imefajla
        return self.imefajla.split('/')[-1].split('\\')[-1]

    class Meta:
        managed = True
        db_table = 'strategija'


class Simulacija(models.Model):
    id_sim = models.AutoField(db_column='id_sim', primary_key=True)
    ime = models.CharField(db_column='ime', max_length=50)
    id_pod_tr = models.ForeignKey(Podaciotrzistu, models.DO_NOTHING, db_column='idPodTr')
    id_strat = models.ForeignKey(Strategija, models.DO_NOTHING, db_column='idStrat')
    status = models.CharField(db_column='status', max_length=1000, null=False)

    class Meta:
        managed = True
        db_table = 'simulacija'


class RangLista(models.Model):
    id_rangliste = models.AutoField(db_column='id_rangliste', primary_key=True)
    naziv = models.CharField(max_length=100)
    id_pod = models.ForeignKey(Podaciotrzistu, models.DO_NOTHING, db_column='idPodTr')

    def __str__(self):
        return self.naziv

    class Meta:
        managed = True
        db_table = 'rang_lista'
