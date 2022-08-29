from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.author import Author
from flask_app.models.book import Book

@app.route("/")
def authors_home():
    authors_dict = Author.get_all()
    print(authors_dict)
    return render_template("authors_home.html", authors = authors_dict)

@app.route('/save_author', methods=["POST"])
def save_author():
    data = {
        "name": request.form["name"],
    }
    Author.save(data)
    return redirect('/')

@app.route('/authors_page/<int:id>')
def authors_favorites(id):
    data = {
        "id": id
    }
    fav = Author.get_authors_favorites(data)
    book_list = Book.get_all()
    print(fav)
    print(fav.id)
    return render_template("authors_favorites.html", author = fav, books = book_list)


@app.route('/add_favorite_book/<int:id>', methods=["POST"])
def add_authors_favorite_book(id):
    data = {
        "author_id": request.form["author_id"],
        "book_id" : request.form["book_id"],
    }
    print(data)
    Author.new_favorite_book(data)
    return redirect(f"/authors_page/{id}")