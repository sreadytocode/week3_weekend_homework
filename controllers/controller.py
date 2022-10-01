from crypt import methods
import datetime
from unicodedata import name
from flask import render_template, redirect, request
from app import app
from models.book import Book
from models.books import books, add_new_book, delete_book

@app.route('/')
def enter():
    return redirect ('/library')
    
@app.route('/library')
def index():
    return render_template('index.html', title='Home', books=books)

@app.route('/library/<index>')
def single_book(index):
    chosen_book = books[int(index)]

    return render_template('book.html', book=chosen_book)

@app.route('/library', methods=['POST'])
def add_book():
    bookTitle=request.form['title']
    bookAuthor=request.form['author']
    bookGenre=request.form['genre']
    checkedout = True if 'checkedout' in request.form else False
    date = request.form['return_by']
    split_date = date.split('-')
    date = datetime.date(int(split_date[0]), int(split_date[1]), int(split_date[2]))
    newBook = Book(title=bookTitle, author=bookAuthor, genre=bookGenre, checkedout=checkedout, return_by=date)
    add_new_book(newBook)

    return redirect('/library')

@app.route('/library/delete/<title>', methods=['POST'])
def delete(title):
   delete_book(title)
   return redirect('/library')


