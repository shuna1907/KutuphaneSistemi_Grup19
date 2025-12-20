from src.book_service import BookService

def main():
    service = BookService()

    print("📚 Kütüphane Otomasyonu\n")
    print("1- Kitap ekle")
    print("2- Kitaplari Listele")
    print("3- Kitap Sil")

    secim = input("Seçim: ")

    if secim == "1":
        service.add_book()
    elif secim == "2":
        service.list_books()
    elif secim == "3":
        service.delete_book()



if __name__ == "__main__":
    main()
