
"""
#REMINDERS
1. The data coming from the database is in a dictionary format and turned into an object instance (model) we access throughout the application.

#TO-DO:
1. Update the initialization attributes to fit data coming from the server.
2. Build out new queries and update the data in the template ones.
"""

from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self ,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('<- Database Name ->').query_db(query)
        data = []
        for user in results:
            data.append( cls(user) )
        return data

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name,last_name,email,created_at,updated_at) VALUES ( %(first_name)s , %(last_name)s , %(email)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('<- Database Name ->').query_db( query, data )

    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s;"
        print(query)
        return connectToMySQL('<- Database Name ->').query_db( query, data )

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL('<- Database Name ->').query_db( query, data )