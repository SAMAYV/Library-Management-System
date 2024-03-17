from datetime import date

class QueryController:
    # Using customer, book and library controller which executes queries on individual tables.
    def __init__(self, database, customer_controller, book_controller, library_controller, author_controller):
        self.database = database
        self.customer_controller = customer_controller
        self.book_controller = book_controller
        self.library_controller = library_controller
        self.author_controller = author_controller
        
    def fetch_author_results(self, customer_id, as_of_date):
        cursor = self.database.connection.cursor()
        # Fetch the records from the database for the given customer and where lend date is <= queried date
        # and the last date on which user returns the book is >= queried date.
        cursor.execute((f'SELECT author.type, library.lend_date, library.days_to_return '
                        f'FROM library INNER JOIN book ON book.id = library.book_id '
                        f'INNER JOIN author ON author.id = book.author_id '
                        f'WHERE customer_id = {customer_id} AND lend_date <= "{as_of_date}" '
                        f'AND DATE_ADD(lend_date, INTERVAL days_to_return DAY) >= "{as_of_date}";'))
        return cursor.fetchall()

    def get_queried_date(self, as_of_date):
        split_date = list(map(int, as_of_date.split('-')))
        queried_date = date(split_date[0], split_date[1], split_date[2])
        return queried_date

    # Fetch the charges on the basis of customer id and as_of_date when the user returns the books.
    def get_customer_charges_v1(self, customer_id, as_of_date):
        results = self.library_controller.fetch_book_data(customer_id, as_of_date)
        cost = 0
        queried_date = self.get_queried_date(as_of_date)
        for result in results:
            cost += (queried_date - result[2]).days
        return cost

    def get_customer_charges_v2(self, customer_id, as_of_date):
        results = self.fetch_author_results(customer_id, as_of_date)
        cost = 0
        queried_date = self.get_queried_date(as_of_date)
        for result in results:
            cost += (queried_date - result[1]).days * self.author_controller.get_type_cost(result[0])
        return cost
