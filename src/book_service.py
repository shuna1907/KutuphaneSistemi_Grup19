from src.models.book import Book

class BookService:

    def add_book(self):
        book_id = input("Kitap ID: ")
        title = input("Kitap adi: ")
        category = input("Kategori: ")
        stock = input("Stok sayisi: ")

        book = Book(book_id, title, category, stock)

        with open("data/books.txt", "a", encoding="utf-8") as f:
            f.write(str(book) + "\n")

        print("Kitap başariyla kaydedildi ✔")

    def list_books(self):
        try:
            with open("data/books.txt", "r", encoding="utf-8") as f:
                lines = f.readlines()

            if len(lines) == 0:
                print(" Kayitli kitap bulunamadi.")
                return
            
            print("\n Kaydedilmiş Kitaplar:")
            for line in lines:
                print(line.strip())

        except FileNotFoundError:
            print("books.txt dosyasi bulunamadi!")

def delete_book(self):
    book_id = input("Silinecek kitap ID: ")

    try:
        with open("data/books.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()

        new_lines = [line for line in lines if not line.startswith(book_id + ",")]

        if len(new_lines) == len(lines):
            print(" Bu ID ile kayitli kitap bulunamadi.")
            return

        with open("data/books.txt", "w", encoding="utf-8") as f:
            f.writelines(new_lines)

        print("Kitap silindi.")

    except FileNotFoundError:
        print(" books.txt dosyasi bulunamadi!")
