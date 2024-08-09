import slug
from django.shortcuts import render
from django.views.generic import DetailView

from .models import Book
# Create your views here.


def home_page(request):
    home_page_1 = ['Приветствуем на главную страницу!']
    books = Book.objects.all()
    response = render(request, 'home_page.html', {'home_page_1': home_page_1,'books':books})
    return response


class MyDetailView(DetailView):
    model = Book  # название класса из models.py
    template_name = 'detail.html'
    context_object_name = 'book'

