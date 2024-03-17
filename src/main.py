import pandas as pd
import os
from database import MySQLConnection
from customerController import CustomerController
from bookController import BookController
from libraryController import LibraryController
from queryController import QueryController
from dotenv import load_dotenv

def main():
    # Load all the environment variables.
    load_dotenv()
    
    conn = MySQLConnection()
    # Customer controller handles customer table data (DDL, DML commands) in the database.
    customer_controller = CustomerController(conn)
    # Book controller handles book table data (DDL, DML commands) in the database.
    book_controller = BookController(conn)
    # Library controller handles library table data (DDL, DML commands) in the database.
    library_controller = LibraryController(conn)
    
    data = pd.read_csv(os.getenv('CSV_DATA_PATH'), delimiter = ',')
    customer_controller.populate_db(data)
    book_controller.populate_db(data)
    library_controller.populate_db(data)
    
    # Query controller is used to perform queries on the library management system and uses 
    # all the above controllers for the same.
    query_controller = QueryController(customer_controller, book_controller, library_controller)
    # API query to fetch the customer charges based on the returning date of books.
    print(query_controller.get_customer_charges_v1(498, '2023-02-16'))

if __name__ == "__main__":
    main()
