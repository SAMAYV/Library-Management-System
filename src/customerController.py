import pandas as pd
from createTables import CREATE_CUSTOMER_TABLE

class CustomerController:
    def __init__(self, database):
        self.database = database
    
    # Populate the table "customer" with the csv data.
    def populate_db(self, data):
        cursor = self.database.connection.cursor()
        cursor.execute(CREATE_CUSTOMER_TABLE)
        for ind in data.index:
            customer_id = data['customer_id'][ind]
            customer_name = data['customer_name'][ind]
            command = f'INSERT IGNORE INTO customer (id, name) VALUES ({str(customer_id)}, "{customer_name}");'
            cursor.execute(command)
        self.database.connection.commit()
