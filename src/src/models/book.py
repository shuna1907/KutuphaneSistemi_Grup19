class Book:
    def __init__(self, book_id, title, category, stock):
        self.book_id = book_id
        self.title = title
        self.category = category
        self.stock = stock

    def __str__(self):
        return f"{self.book_id} - {self.title} - {self.category} - Stok:{self.stock}"
