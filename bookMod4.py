from django.db import models


# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    is_favorite = models.BooleanField(help_text="True mean's favorite, False mean's not favorite")


def create_Book(name:str,  author:str, is_favorite:bool):
    new_Book = Book(name=name, author=author, is_favorite=is_favorite)
    new_Book.save()
    return new_Book


def all_Books():
    return Book.objects.all()

def favorite_Books() :
    return Book.objects.filter(is_favorite=True)


def find_Book_by_name(name):
    try:
        return Book.objects.get(name=name)
    except Book.DoesNotExist:
        return None

def delete_Book(name):
    Book = find_Book_by_name(name)
    Book.delete()
    

def update_Book_author(name, author):
    Book = find_Book_by_name(name=name)
    Book.author = author
    Book.save()

# def update_Book_email(name, author):
#     Book.objects.filter(name=name).update(author=author)