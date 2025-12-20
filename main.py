from src.book_service import BookService
from src.member_service import MemberService 

def main():
    book_service = BookService()
    member_service = MemberService()

    while True:
        print("\n--- KÜTÜPHANE OTOMASYONU ---")
        print("1- Kitap Ekle")
        print("2- Kitapları Listele")
        print("3- Kitap Sil")
        print("4- Üye Ekle")        
        print("5- Üyeleri Listele")
        print("0- Çıkış")

        secim = input("\nSeçiminiz: ")

        if secim == "1":
            book_service.add_book()
        elif secim == "2":
            book_service.list_books()
        elif secim == "3":
            book_service.delete_book()
        elif secim == "4":
            member_service.add_member()
        elif secim == "5":
            member_service.list_members()
        elif secim == "0":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()
    