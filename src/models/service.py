from src.models.transaction import Transaction
from datetime import datetime

class BorrowService:
    def init(self, book_service, member_service):
        self.book_service = book_service
        self.member_service = member_service
        self.borrow_file = "data/borrows.txt"

    def borrow_book(self):
        member_id = input("Üye ID giriniz: ")
        book_id = input("Kitap ID giriniz: ")
        
        print(f"İşlem Onaylandı: {member_id} ID'li üye {book_id} ID'li kitabı ödünç aldı.")
        
        # Dosyaya kaydetme mantığı buraya gelecek
        with open(self.borrow_file, "a", encoding="utf-8") as f:
            f.write(f"{member_id},{book_id},{datetime.now().strftime('%d-%m-%Y')}\n")