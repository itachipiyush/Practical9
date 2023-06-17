from django.shortcuts import render
from data8.models import Book
from . my_model_form import Form_Book

def db_open_model_form_way(request):
    context={}
    form_book_to_disp = Form_Book(request.POST or None, request.FILES or None)
    if form_book_to_disp.is_valid():
        form_book_to_disp.save()
    context['form_book_to_disp']= form_book_to_disp

    return render(request, "model_form.html",context)