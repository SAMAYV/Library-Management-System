import os
import json
from createTables import CREATE_BOOK_TABLE, CREATE_AUTHOR_TABLE, CREATE_BOOK_TABLE_V2
import pandas as pd

class BookController:
    def __init__(self, database):
        self.database = database

    # Populate the table "book" with the csv data for version 1 API.
    def populate_db(self, data):
        cursor = self.database.connection.cursor()
        cursor.execute(CREATE_BOOK_TABLE)
        for ind in data.index:
            books = json.loads(data['books'][ind])
            for book in books:
                book_id = book['book_id']
                book_name = book['book_name']
                author_name = book['author_name']
                command = (f'INSERT IGNORE INTO book (id, name, author) VALUES ('
                           f'"{book_id}", "{book_name}", "{author_name}");')
                cursor.execute(command)
        self.database.connection.commit()

    # Populate and update the database for version 2 API. Requires library controller as well since it is related to book table.
    # "book" table schema is updated and "author" table is created.
    # Added author_id in "book" table since multiple authors can have same names.
    def populate_db_v2(self, data, library_controller):
        cursor = self.database.connection.cursor()
        cursor.execute('DROP TABLE IF EXISTS library;')
        cursor.execute('DROP TABLE IF EXISTS book;')
        cursor.execute(CREATE_AUTHOR_TABLE)
        cursor.execute(CREATE_BOOK_TABLE_V2)
        
        unique_id = 1
        author_name_to_id = dict()
        author_name_to_type = dict()
        
        author_data = pd.read_csv(os.getenv('AUTHOR_DATA_PATH'), delimiter = ',')
        for ind in author_data.index:
            author_name = author_data['name'][ind]
            author_type = author_data['type'][ind]
            author_name_to_type[author_name] = author_type
        
        for ind in data.index:
            books = json.loads(data['books'][ind])
            for book in books:
                book_id = book['book_id']
                book_name = book['book_name']
                author_name = book['author_name']
                author_type = author_name_to_type[author_name]
                author_id = unique_id
                if author_name_to_id.get(book_name, None) is not None:
                    author_id = author_name_to_id[book_name]
                else:
                    author_name_to_id[book_name] = unique_id
                    unique_id += 1
                
                command = (f'INSERT IGNORE INTO author (id, name, type) VALUES ('
                           f'{author_id}, "{author_name}", "{author_type}");')
                cursor.execute(command)
                
                command = (f'INSERT IGNORE INTO book (id, name, author_id) VALUES ('
                           f'"{book_id}", "{book_name}", {author_id});')
                cursor.execute(command)
        
        library_controller.populate_db(data)
        self.database.connection.commit()
