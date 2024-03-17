from datetime import date

class QueryController:
    # Using customer, book and library controller which executes queries on individual tables.
    def __init__(self, customer_controller, book_controller, library_controller):
        self.customer_controller = customer_controller
        self.book_controller = book_controller
        self.library_controller = library_controller

    # Fetch the charges on the basis of customer id and as_of_date when the user returns the books.
    def get_customer_charges_v1(self, customer_id, as_of_date):
        results = self.library_controller.fetch_book_data(customer_id, as_of_date)
        cost = 0
        split_date = list(map(int, as_of_date.split('-')))
        queried_date = date(split_date[0], split_date[1], split_date[2])
        for result in results:
            cost += (queried_date - result[2]).days
        return cost