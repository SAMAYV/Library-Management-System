CREATE_LIBRARY_TABLE = """
CREATE TABLE IF NOT EXISTS library (
    customer_id INT NOT NULL, 
    book_id VARCHAR(100) NOT NULL, 
    lend_date DATE NOT NULL, 
    days_to_return INT NOT NULL, 
    PRIMARY KEY (customer_id, book_id, lend_date, days_to_return),
    FOREIGN KEY (customer_id) REFERENCES customer(id) ON DELETE CASCADE ON UPDATE CASCADE, 
    FOREIGN KEY (book_id) REFERENCES book(id) ON DELETE CASCADE ON UPDATE CASCADE
);
"""

CREATE_BOOK_TABLE = """
CREATE TABLE IF NOT EXISTS book ( 
    id VARCHAR(100) NOT NULL, 
    name VARCHAR(100), 
    author VARCHAR(100), 
    PRIMARY KEY (id) 
);
"""

CREATE_CUSTOMER_TABLE = """
CREATE TABLE IF NOT EXISTS customer ( 
    id int NOT NULL, 
    name VARCHAR(100), 
    PRIMARY KEY (id) 
);
"""

CREATE_BOOK_TABLE_V2 = """
CREATE TABLE IF NOT EXISTS book ( 
    id VARCHAR(100) NOT NULL, 
    name VARCHAR(100), 
    author_id INT NOT NULL, 
    PRIMARY KEY (id),
    FOREIGN KEY (author_id) REFERENCES author(id) ON DELETE CASCADE ON UPDATE CASCADE
);
"""

CREATE_AUTHOR_TABLE = """
CREATE TABLE IF NOT EXISTS author ( 
    id int NOT NULL, 
    name VARCHAR(100),
    type VARCHAR(100), 
    PRIMARY KEY (id)
);
"""