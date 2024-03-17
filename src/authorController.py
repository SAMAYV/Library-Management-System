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

    @staticmethod
    def get_type_cost_v3(book_type, no_of_days):
        if AuthorBookType[book_type] == AuthorBookType.FICTION:
            return 3 * no_of_days
        elif AuthorBookType[book_type] == AuthorBookType.REGULAR:
            return 2 + max(0, no_of_days - 2) * 1.5
        elif AuthorBookType[book_type] == AuthorBookType.NOVEL:
            return 4.5 + max(0, no_of_days - 3) * 1
        else:
            return 1