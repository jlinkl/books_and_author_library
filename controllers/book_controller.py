from flask import Flask, redirect, render_template, Blueprint, request
from repositories import author_repository
from repositories import book_repository
# from models.task import Task

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route('/books')
def books():
    books = book_repository.select_all()
    return render_template("books/index.html", all_books=books)