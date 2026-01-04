import os

class IDGenerator:
    @staticmethod
    def generate_id(file_path):
        """Dosyadaki satır sayısına göre yeni bir ID üretir."""
        if not os.path.exists(file_path):
            return "1"
        
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            if not lines:
                return "1"
            
            # Son satırdaki ID'yi al ve 1 artır
            last_line = lines[-1].strip().split(",")
            last_id = int(last_line[0])
            return str(last_id + 1)