from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book
from pprint import pprint

class Author:
    def __init__(self ,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.books = []


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL('books_schema').query_db(query)
        data = []
        for author in results:
            data.append( cls(author) )
        return data

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM authors WHERE id = %(id)s;"
        results = connectToMySQL('books_schema').query_db( query, data )
        data = []
        for author in results:
            data.append( cls(author) )
        return data

    @classmethod
    def save(cls, data):
        query = "INSERT INTO authors (name, created_at, updated_at) VALUES ( %(name)s , NOW() , NOW() );"
        return connectToMySQL('books_schema').query_db( query, data )

    @classmethod
    def get_authors_favorites(cls, data):
        query = "SELECT * FROM authors LEFT JOIN favorites ON favorites.author_id = authors.id LEFT JOIN books ON favorites.book_id = books.id WHERE authors.id = %(id)s;"
        results = connectToMySQL('books_schema').query_db( query, data )
        author = cls(results[0])
        pprint(results, sort_dicts=False, width=1)
        for favorite in results:
            book_data = {
            'id': favorite['books.id'],
            'title': favorite['title'],
            'num_of_pages': favorite['num_of_pages'],
            'created_at': favorite['books.created_at'],
            'updated_at': favorite['books.updated_at']
            }
            author.books.append( book.Book(book_data) )
        return author

    @classmethod
    def new_favorite_book(cls, data):
        query = "INSERT INTO favorites (author_id, book_id) VALUES (%(author_id)s, %(book_id)s);"
        print(query)
        return connectToMySQL('books_schema').query_db(query, data)


