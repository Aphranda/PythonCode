from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from books.models import Book
# Create your views here.


def add_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        price = request.POST.get("price")
        date = request.POST.get("date")
        publish = request.POST.get("publish")

        book_object = Book.objects.create(title=title, price=price, pub_date=date, publish=publish)
        return redirect("/books/")

    return render(request, "addbook.html")


def books(request):
    book_list = Book.objects.all()

    return render(request, 'books.html', {"book_list": book_list})


def delbook(request, id):
    Book.objects.filter(id=id).delete()
    return redirect("/books/")


def changebook(request, id):
    book_object = Book.objects.filter(id=id).first()
    if request.method == "POST":
        title = request.POST.get("title")
        price = request.POST.get("price")
        date = request.POST.get("date")
        publish = request.POST.get("publish")

        Book.objects.filter(id=id).update(title=title, price=price, pub_date=date, publish=publish)
        return redirect('/books/')
        
    return render(request, "changebook.html", {"book_object": book_object})




