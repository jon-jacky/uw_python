from django.db import models

class MailingList(models.Model):
    email = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.email

class PhoneNumbers(models.Model):
    NUMBER_TYPE = (
        (u'work', u'work'),
        (u'home', u'home'),
        (u'cell', u'cell'),
        (u'beeper', u'beeper'),
        )
    email = models.ForeignKey(MailingList)
    number_type = models.CharField(max_length=6, choices=NUMBER_TYPE)
    phone_number = models.CharField(max_length=20) 

    def __unicode__(self):
        return self.phone_number
