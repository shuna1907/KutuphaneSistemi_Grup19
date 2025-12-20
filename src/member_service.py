from src.models.member import Member

class MemberService:
    def add_member(self):
        member_id = input("Üye ID: ")
        name = input("Üye Adı Soyadı: ")
        email = input("E-posta: ")

        member = Member(member_id, name, email)

        with open("data/members.txt", "a", encoding="utf-8") as f:
            f.write(str(member) + "\n")
        print("Üye başarıyla kaydedildi ✔")

    def list_members(self):
        try:
            with open("data/members.txt", "r", encoding="utf-8") as f:
                lines = f.readlines()
            
            if not lines:
                print("Kayıtlı üye bulunamadı.")
                return

            print("\n--- Kayıtlı Üyeler ---")
            for line in lines:
                print(line.strip())
        except FileNotFoundError:
            print("members.txt henüz oluşturulmamış.")