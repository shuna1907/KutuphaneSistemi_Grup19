from src.book_service import BookService

def main():
    service = BookService()

    print("📚 Kütüphane Otomasyonu\n")
    print("1- Kitap ekle")
    secim = input("Seçim: ")

    if secim == "1":
        service.add_book()

if __name__ == "__main__":
    main()
