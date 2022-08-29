from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author
from pprint import pprint

class Book:
    def __init__(self ,data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.authors = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL('books_schema').query_db(query)
        data = []
        for book in results:
            data.append( cls(book) )
        return data

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM books WHERE id = %(id)s;"
        results = connectToMySQL('books_schema').query_db( query, data )
        print(results)
        data = []
        for book in results:
            data.append( cls(book) )
        return data

    @classmethod
    def save(cls, data):
        query = "INSERT INTO books (title, num_of_pages, created_at, updated_at) VALUES ( %(title)s , %(num_of_pages)s , NOW() , NOW() );"
        return connectToMySQL('books_schema').query_db( query, data )

    @classmethod
    def get_books_favorites(cls, data):
        print("--------->", data)
        query = "SELECT * FROM books LEFT JOIN favorites ON favorites.book_id = books.id LEFT JOIN authors ON favorites.author_id = authors.id WHERE books.id = %(id)s;"
        results = connectToMySQL('books_schema').query_db( query, data )
        book = cls(results[0])
        pprint(results, sort_dicts=False, width=1)
        for favorite in results:
            author_data = {
            'id': favorite['author_id'],
            'name': favorite['name'],
            'created_at': favorite['authors.created_at'],
            'updated_at': favorite['authors.updated_at']
            }
            book.authors.append( author.Author(author_data) )
        return book

    @classmethod
    def new_favorite_author(cls, data):
        query = "INSERT INTO favorites (author_id, book_id) VALUES (%(author_id)s, %(book_id)s);"
        print(query)
        return connectToMySQL('books_schema').query_db(query, data)