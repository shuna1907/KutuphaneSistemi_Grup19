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
        
                                                                                    def update_book_status(self, book_id, is_borrowed):  def update_book_status(self, book_id, is_borrowed):
            
    with open("data/books.txt", "r", encoding="utf-8") as f:
        books = f.readlines()

    # 2. Dosyayı yazma modunda aç ve satır satır güncelle
    with open("data/books.txt", "w", encoding="utf-8") as f:
        for line in books:
            data = line.strip().split(",")
            if data[0] == book_id:
                # Kitabın durumunu (stok/ödünç durumu) güncelliyoruz
                data[3] = str(is_borrowed) 
                f.write(",".join(data) + "\n")
            else:
                f.write(line)

 def return_book(self):
    member_id = input("Üye ID giriniz: ")
    book_id = input("İade edilecek Kitap ID giriniz: ")
    return_date = datetime.now().strftime('%d-%m-%Y')

    updated_borrows = []
    found = False

    # borrows.txt içindeki aktif kaydı bulup iade tarihini ekliyoruz
    with open(self.borrow_file, "r", encoding="utf-8") as f:
        for line in f:
            data = line.strip().split(",")
            # Üye ID ve Kitap ID eşleşiyorsa ve henüz iade tarihi yazılmamışsa
            if data[0] == member_id and data[1] == book_id and len(data) == 3:
                data.append(return_date) # İade tarihini 4. sütun olarak ekle
                updated_borrows.append(",".join(data) + "\n")
                found = True
            else:
                updated_borrows.append(line)

    if found:
        with open(self.borrow_file, "w", encoding="utf-8") as f:
            f.writelines(updated_borrows)
        
        # Kitabı kütüphaneye geri döndür (is_borrowed = False)
        self.update_book_status(book_id, False)
        print(f"\n✅ Başarılı: {book_id} ID'li kitap iade alındı.")
    else:
        print("\n❌ Hata: Bu üyeye ait aktif bir ödünç kaydı bulunamadı!")               