import json
from createTables import CREATE_BOOK_TABLE

class BookController:
    def __init__(self, database):
        self.database = database

    # Populate the table "book" with the csv data.
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
