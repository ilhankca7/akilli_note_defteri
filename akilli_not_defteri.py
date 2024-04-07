''' Kullanıcıya bir not defteri uygulaması sunar.
    Kullanıcı notlar ekleyebilir, düzenleyebilir, 
    silebilir, listeyebilir ve kaydedebilir. 
    Ayrıca, notları bir dosyaya kaydedebilir ve bir dosyadan yükleyebilir
'''
import os

class Note:
    def __init__(self,title, content):
        self.title = title
        self.content = content

class Notebook:
    def __init__(self):
        self.notes = []
    def add_note(self, note):
        self.notes.append(note)
    def edit_note(self,title,content):
        for note in self.notes:
            if note.title == title:
                note.content = content
                break
            else:
                print("Başlık '{}' ile not bulunamadi.".format(title))
    def delete_note(self,title):
        for note in self.notes:
            if note.title == title:
                self.notes.remove(note)
                break
            else:
                print("Başlık '{}' ile not bulunamadi.".format(title))
    def list_notes(self):
        if not self.notes:
            print("not bulunamadi.")
        else:
            for note in self.notes:
                print("Baslık: {}\nIceril: {}\n\n".format(note.title,note.content))
    def save_notes(self, file_name):
        with open(file_name, 'w') as f:
            for note in self.notes:
                f.write("Başlık: {}\nİçerik: {}\n\n".format(note.title, note.content))

    def load_notes(self, file_name):
        if os.path.exists(file_name):
            with open(file_name, 'r') as f:
                lines = f.readlines()
                i = 0
                while i < len(lines):
                    if lines[i].startswith("Başlık:"):
                        title = lines[i][8:].strip()
                        content = lines[i + 1][9:].strip()
                        self.notes.append(Note(title, content))
                        i += 3
                    else:
                        i += 1
        else:
            print("Dosya '{}' bulunamadı.".format(file_name)) 


if __name__ == "__main__":
    notebook = Notebook()
    while True:
        print("\nNot Defteri Menüsü:")
        print("1. Not Ekle")
        print("2. Not Düzenle")
        print("3. Not Sil")
        print("4. Notları Listele")
        print("5. Notları Kaydet")
        print("6. Notları Yükle")
        print("7. Çıkış")

        choice = input("Seçiminizi girin (1-7): ")

        if choice == '1':
            title = input("Not başlığını girin: ")
            content = input("Not içeriğini girin: ")
            notebook.add_note(Note(title, content))
        elif choice == '2':
            title = input("Düzenlemek istediğiniz notun başlığını girin: ")
            content = input("Yeni içeriği girin: ")
            notebook.edit_note(title, content)
        elif choice == '3':
            title = input("Silmek istediğiniz notun başlığını girin: ")
            notebook.delete_note(title)
        elif choice == '4':
            notebook.list_notes()
        elif choice == '5':
            file_name = input("Notları kaydetmek için dosya adını girin: ")
            notebook.save_notes(file_name)
        elif choice == '6':
            file_name = input("Notları yüklemek için dosya adını girin: ")
            notebook.load_notes(file_name)
        elif choice == '7':
            break
        else:
            print("Geçersiz giriş")



