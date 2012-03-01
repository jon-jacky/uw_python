from mailing_list.models import MailingList, PhoneNumbers
from django.contrib import admin

class MailingListAdmin(admin.ModelAdmin):
    fields = ['email', 'name']

class PhoneNumbersAdmin(admin.ModelAdmin):
    fields = ['email', 'number_type', 'phone_number']

admin.site.register(MailingList, MailingListAdmin)
admin.site.register(PhoneNumbers, PhoneNumbersAdmin)
