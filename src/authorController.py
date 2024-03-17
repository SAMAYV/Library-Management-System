from authorBookType import AuthorBookType

class AuthorController:
    def __init__(self, database):
        self.database = database
    
    @staticmethod
    def get_type_cost(book_type):
        if AuthorBookType[book_type] == AuthorBookType.FICTION:
            return 3
        elif AuthorBookType[book_type] == AuthorBookType.REGULAR:
            return 1.5
        elif AuthorBookType[book_type] == AuthorBookType.NOVEL:
            return 1.5
        else:
            return 1
