class FileManager:
    @staticmethod
    def read_lines(file_path):
        """Dosyadaki tüm satırları liste olarak döner."""
        if not os.path.exists(file_path):
            return []
        with open(file_path, "r", encoding="utf-8") as f:
            return f.readlines()

    @staticmethod
    def append_line(file_path, data_list):
        """Veriyi virgülle birleştirip dosyanın sonuna ekler."""
        line = ",".join(map(str, data_list)) + "\n"
        with open(file_path, "a", encoding="utf-8") as f:
            f.write(line)

    @staticmethod
    def write_all_lines(file_path, lines):
        """Tüm listeyi dosyaya baştan yazar (Güncelleme işlemleri için)."""
        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(lines) 
            """file_manager eklendi"""