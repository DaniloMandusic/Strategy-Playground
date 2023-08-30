from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.models import User

from .models import RegistrationRequest, Korisnik, RangLista
from django.urls import reverse
from django.utils.html import format_html


@admin.register(RegistrationRequest)
class RegistrationRequestAdmin(admin.ModelAdmin):
    list_display = ['ime', 'prezime', 'email', 'status', 'approve_button', 'reject_button']

    def approve_button(self, obj):
        return format_html('<a class="button" href="{}">Approve</a>',
                           reverse('approve_registration_panel', args=[obj.id]))
    approve_button.short_description = ''

    def reject_button(self, obj):
        return format_html('<a class="button" href="{}">Reject</a>',
                           reverse('reject_registration_panel', args=[obj.id]))

    reject_button.short_description = ''


class KorisnikAdmin(admin.ModelAdmin):
    list_display = ['ime', 'prezime', 'email', 'status']


admin.site.register(Korisnik, KorisnikAdmin)
admin.site.register(RangLista)


