import unittest
import pandas as pd
import os
from database import MySQLConnection
from customerController import CustomerController
from bookController import BookController
from libraryController import LibraryController
from queryController import QueryController
from dotenv import load_dotenv

class TestQueryController(unittest.TestCase):
    def setUp(self):
        load_dotenv()
        self.conn = MySQLConnection()
        self.customer_controller = CustomerController(self.conn)
        self.book_controller = BookController(self.conn)
        self.library_controller = LibraryController(self.conn)
        
        data = pd.read_csv(os.getenv('CSV_DATA_PATH'), delimiter = ',')
        self.customer_controller.populate_db(data)
        self.book_controller.populate_db(data)
        self.library_controller.populate_db(data)
    
        self.query_controller = QueryController(self.customer_controller, self.book_controller, self.library_controller)
    
    def test_get_customer_charges_v1_with_one_book_to_return(self):
        cost = self.query_controller.get_customer_charges_v1(498, '2023-02-16')
        self.assertEqual(cost, 2)
        
    def test_get_customer_charges_v1_with_multiple_books_to_return(self):
        cost = self.query_controller.get_customer_charges_v1(3, '2023-09-25')
        self.assertEqual(cost, 6)


if __name__ == '__main__':
    unittest.main()
