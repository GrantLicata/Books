from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.book import Book
from flask_app.models.author import Author
            
@app.route('/book_home')
def show():
    book_dict = Book.get_all()
    return render_template("books_home.html", books = book_dict)

@app.route('/book_favorites/<int:id>')
def book_favorites(id):
    data = {
        'id': id
    }
    selected_book = Book.get_books_favorites(data)
    print("selected book", selected_book)
    all_authors = Author.get_all()
    return render_template("books_favorites.html", book = selected_book, authors = all_authors)

@app.route('/save_book', methods=["POST"])
def save_book():
    data = {
        "title": request.form["title"],
        "num_of_pages": request.form["num_of_pages"],
    }
    Book.save(data)
    return redirect('/book_home')

@app.route('/add_favorite_author/<int:id>', methods=["POST"])
def add_books_favorite_authors(id):
    data = {
        "author_id": request.form["author_id"],
        "book_id" : request.form["book_id"],
    }
    print(data)
    Book.new_favorite_author(data)
    return redirect(f"/book_favorites/{id}")

