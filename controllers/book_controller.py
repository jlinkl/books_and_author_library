from flask import Flask, redirect, render_template, Blueprint, request
from repositories import author_repository
from repositories import book_repository
from models.book import Book

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route('/books')
def books():
    books = book_repository.select_all()
    return render_template("books/index.html", all_books=books)

@books_blueprint.route('/books/<id>/delete', methods=['POST'])
def delete(id):
    book_repository.delete(id)
    return redirect('/books')

@books_blueprint.route('/books/new')
def new():
    authors = author_repository.select_all()
    return render_template("books/new.html", all_authors=authors)

@books_blueprint.route('/books', methods=['POST'])
def create():
    title = request.form['title']
    genre     = request.form['genre']
    author_id    = request.form['author_id']
    author = author_repository.select(author_id)
    book = Book(title, genre, author)
    book_repository.save(book)
    return redirect('/books')

@books_blueprint.route('/books/<id>')
def show(id):
    book = book_repository.select(id)
    return render_template("books/show.html", book=book)