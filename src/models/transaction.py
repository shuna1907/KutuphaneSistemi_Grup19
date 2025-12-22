class Transaction:
    def init(self, member_id, book_id, borrow_date, return_date=None):
        self.member_id = member_id
        self.book_id = book_id
        self.borrow_date = borrow_date
        self.return_date = return_date # Henüz iade edilmediyse None olur