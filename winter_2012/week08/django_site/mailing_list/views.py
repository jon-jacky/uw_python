from django.template import Context, loader
from mailing_list.models import MailingList, PhoneNumbers
from django.http import HttpResponse

# placeholder, message just shows we reached this view
def index(request):
    return HttpResponse("mailing_list index to come ...")

# no template, just send a string of HTML
def name_list(request):
    #return HttpResponse("mailing_list name_list to come ...")
    items = MailingList.objects.all()
    # Why don't we see both fields?  We just see email not name
    output = '<br>'.join([ '%s' % i for i in items ])
    return HttpResponse(output)

# placeholder, message just shows we reached this view
def phone_numbers(request):
    return HttpResponse("mailing_list phone_numbers to come ...")

# placeholder, message just shows we reached this view
def query(request):
    return HttpResponse("mailing_list query to come ...")
