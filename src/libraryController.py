import json
from createTables import CREATE_LIBRARY_TABLE

class LibraryController:
    def __init__(self, database):
        self.database = database
    
    # Populate the table "library" with the csv data.
    def populate_db(self, data):
        cursor = self.database.connection.cursor()
        cursor.execute(CREATE_LIBRARY_TABLE)
        for ind in data.index:
            customer_id = data['customer_id'][ind]
            books = json.loads(data['books'][ind])
            for book in books:
                book_id = book['book_id']
                lend_date = book['lend_date']
                days_to_return = book['days_to_return']
                command = (f'INSERT IGNORE INTO library (customer_id, book_id, lend_date, days_to_return)'
                           f' VALUES ({customer_id}, "{book_id}", "{lend_date}", {days_to_return})')
                cursor.execute(command)
        self.database.connection.commit()
        cursor.execute('SELECT * FROM library;')
        
    # Fetches the book data from the database for the given customer and the date on which the user returns the issued books.
    def fetch_book_data(self, customer_id, as_of_date):
        cursor = self.database.connection.cursor()
        # Fetch the records from the database for the given customer and where lend date is <= queried date
        # and the last date on which user returns the book is >= queried date.
        cursor.execute((f'SELECT * FROM library WHERE customer_id = {customer_id} AND lend_date <= "{as_of_date}" '
                        f'AND DATE_ADD(lend_date, INTERVAL days_to_return DAY) >= "{as_of_date}";'))
        return cursor.fetchall()
