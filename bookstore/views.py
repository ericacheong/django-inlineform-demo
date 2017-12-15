from django.shortcuts import render
from django.http import HttpResponseRedirect
#from bookstore.forms import AuthorForm
from django.forms import modelformset_factory, inlineformset_factory
from bookstore.models import Author, Book


def edit_author(request):
    AuthorFormSet = modelformset_factory(Author, fields=('name', 'title'), extra=2)
    if request.method == 'POST':
        formset = AuthorFormSet(request.POST)

        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect('/bookstore/authors/')
    else:
        formset = AuthorFormSet()
    return render(request, 'bookstore/author.html', {'formset': formset})


def edit_book(request, id):
    BookFormSet = inlineformset_factory(Author, Book, fields=('title',))
    author = Author.objects.get(pk=id)
    if request.method == 'POST':
        formset = BookFormSet(request.POST, instance=author)

        if formset.is_valid():
            formset.save()
            path = '/bookstore/authors/'+ str(id) + '/books/'
            return HttpResponseRedirect(path)
    else:
        formset = BookFormSet(instance=author)

    return render(request, 'bookstore/author.html', {'formset': formset})
    

