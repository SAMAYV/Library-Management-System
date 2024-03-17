import os
import unittest
import pandas as pd
from database import MySQLConnection
from customerController import CustomerController
from bookController import BookController
from libraryController import LibraryController
from queryController import QueryController
from authorController import AuthorController
from dotenv import load_dotenv


class TestQueryControllerVersion1(unittest.TestCase):
    def setUp(self):
        load_dotenv()
        self.conn = MySQLConnection()
        self.conn.drop_tables()
        data = pd.read_csv(os.getenv('CUSTOMER_DATA_PATH'), delimiter = ',')

        self.customer_controller = CustomerController(self.conn)
        self.book_controller = BookController(self.conn)
        self.library_controller = LibraryController(self.conn)
        self.author_controller = AuthorController(self.conn)
        
        self.customer_controller.populate_db(data)
        self.book_controller.populate_db(data)
        self.library_controller.populate_db(data)
    
        self.query_controller = QueryController(self.conn, self.customer_controller, self.book_controller, 
                                                self.library_controller, self.author_controller)
    
    def test_get_customer_charges_with_one_book_to_return_v1(self):
        cost = self.query_controller.get_customer_charges_v1(498, '2023-02-16')
        self.assertEqual(cost, 2)
        
    def test_get_customer_charges_with_one_book_2_to_return_v1(self):
        cost = self.query_controller.get_customer_charges_v1(15, '2023-04-25')
        self.assertEqual(cost, 9)
        
    def test_get_customer_charges_with_multiple_books_to_return_v1(self):
        cost = self.query_controller.get_customer_charges_v1(3, '2023-09-25')
        self.assertEqual(cost, 6)
        
    def test_get_customer_charges_with_multiple_books_2_to_return_v1(self):
        cost = self.query_controller.get_customer_charges_v1(7, '2023-11-19')
        self.assertEqual(cost, 29)


class TestQueryControllerVersion2(unittest.TestCase):
    def setUp(self):
        load_dotenv()
        self.conn = MySQLConnection()
        self.conn.drop_tables()
        data = pd.read_csv(os.getenv('CUSTOMER_DATA_PATH'), delimiter = ',')
        
        self.customer_controller = CustomerController(self.conn)
        self.book_controller = BookController(self.conn)
        self.library_controller = LibraryController(self.conn)
        self.author_controller = AuthorController(self.conn)
        
        self.customer_controller.populate_db(data)
        self.book_controller.populate_db_v2(data, self.library_controller)
        
        self.query_controller = QueryController(self.conn, self.customer_controller, self.book_controller, 
                                                self.library_controller, self.author_controller)
    
    def test_get_customer_charges_with_one_book_to_return_v2(self):
        cost = self.query_controller.get_customer_charges_v2(498, '2023-02-16')
        self.assertEqual(cost, 3.0)
        
    def test_get_customer_charges_with_one_book_2_to_return_v2(self):
        cost = self.query_controller.get_customer_charges_v2(15, '2023-04-25')
        self.assertEqual(cost, 27.0)
        
    def test_get_customer_charges_with_multiple_books_to_return_v2(self):
        cost = self.query_controller.get_customer_charges_v2(3, '2023-09-25')
        self.assertEqual(cost, 9.0)
        
    def test_get_customer_charges_with_multiple_books_2_to_return_v2(self):
        cost = self.query_controller.get_customer_charges_v2(7, '2023-11-19')
        self.assertEqual(cost, 84.0)
        
    def test_get_customer_charges_with_one_book_to_return_v3(self):
        cost = self.query_controller.get_customer_charges_v3(498, '2023-02-16')
        self.assertEqual(cost, 2.0)
        
    def test_get_customer_charges_with_one_book_2_to_return_v3(self):
        cost = self.query_controller.get_customer_charges_v3(15, '2023-04-25')
        self.assertEqual(cost, 27.0)
        
    def test_get_customer_charges_with_multiple_books_to_return_v3(self):
        cost = self.query_controller.get_customer_charges_v3(3, '2023-09-25')
        self.assertEqual(cost, 9.5)
        
    def test_get_customer_charges_with_multiple_books_2_to_return_v3(self):
        cost = self.query_controller.get_customer_charges_v3(7, '2023-11-19')
        self.assertEqual(cost, 83.0)


if __name__ == '__main__':
    unittest.main()
