import json
from Note import Note  # Импортируем класс Note из соответствующего файла


class NoteBook:
    def __init__(self, file_path):
        self.file_path = file_path
        self.notes = []
        self.load_notes()  # Осуществляется загрузка списка заметок в данном классе

    def load_notes(self):
        try:
            with open(self.file_path, 'NoteBook') as file:
                self.notes = json.load(file)
        except FileNotFoundError:  # Если файл не существует, то создается пустой список заметок
            self.notes = []

    def save_notes(self):
        with open(self.file_path, 'NoteBook') as file:
            json.dump(self.notes, file)

    def add_note(self, note):
        self.notes.append(note)
        self.save_notes()

    def edit_note(self, note_index, new_title, new_content):
        if 0 <= note_index < len(self.notes):
            self.notes[note_index].title = new_title
            self.notes[note_index].content = new_content
            self.save_notes()
        else:
            print("Заметка с данным индексом не существует!")

    def delete_note(self, note_index):
        if 0 <= note_index < len(self.notes):
            del self.notes[note_index]
            self.save_notes()
        else:
            print("Заметка с данным индексом не существует!")

    if __name__ == "__main__":
        file_path = "NoteBook.json"
        notebook_manager = Note(file_path)
            
    for i, note in enumerate(notebook_manager.notes):
        print(f"Заметка {i + 1}: {note.title}")

    new_note = Note("Тема", "Содержание", "2023-09-30")  # Передаётся: тема, содержание и дата заметки
    notebook_manager.add_note(new_note)
    notebook_manager.edit_note(0, "Новая тема", "Новое содержание")
    notebook_manager.delete_note(0)

    for i, note in enumerate(notebook_manager.notes):
        print(f"Заметка {i + 1}: {note.title}")

        
        
        
        
        
        
        
        
        
        
        
        

    