from src.book_service import BookService
from src.member_service import MemberService

class MenuController:
    def __init__(self):
     
        self.book_service = BookService()
        self.member_service = MemberService()

    def show_menu(self):
        while True:
            print("\n--- KÜTÜPHANE OTOMASYONU ---")
            print("1- Kitap Ekle")
            print("2- Kitapları Listele")
            print("3- Üye Ekle")
            print("4- Üyeleri Listele")
            print("0- Çıkış")

            secim = input("\nSeçiminiz: ")

            if secim == "1":
                self.book_service.add_book()
            elif secim == "2":
                self.book_service.list_books()
            elif secim == "3":
                self.member_service.add_member()
            elif secim == "4":
                self.member_service.list_members()
            elif secim == "0":
                print("Sistemden çıkılıyor... İyi günler!")
                break
            else:
                print("Geçersiz seçim, lütfen tekrar deneyin.")