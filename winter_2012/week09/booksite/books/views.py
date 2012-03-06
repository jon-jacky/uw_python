from django.template import Context, loader
from books.models import Books
from django.http import HttpResponse

def index(request):
    # return HttpResponse("books index to come ...") # placeholder
    # based on first example in Django tutorial03
    books = Books.objects.all()
    t = loader.get_template('index.html')
    c = Context({'books':books})
    return HttpResponse(t.render(c))

def detail(request, isbn):
    # return HttpResponse("books detail for isbn %s to come ..." % isbn) # placeholder
    book = Books.objects.get(pk=isbn)
    t = loader.get_template('detail.html')
    c = Context({'book':book})
    return HttpResponse(t.render(c))    
