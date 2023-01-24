from func import run, save
import tkinter
import tkinter.messagebox
import customtkinter as ctk
from tkinter import filedialog
import os

ctk.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


class LetterSoupApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        w = self.winfo_screenwidth() // 2
        h = self.winfo_screenheight() // 2
        h_window = 930
        self.title("Суп из букв")
        self.geometry(f'{h_window}x110+{w - h_window // 2}+{h}')


        self.frame1 = ctk.CTkFrame(self)
        self.frame2 = ctk.CTkFrame(self)
        self.frame1.pack(anchor='w', pady=10, ipady=5)
        self.frame2.pack(anchor='w')

        self.entry_folder = ctk.CTkEntry(self.frame1, width=300)
        self.entry_filename = ctk.CTkEntry(self.frame1, placeholder_text='Введите имя файла')
        self.btn_folder = ctk.CTkButton(self.frame1, text='Выбрать папку', command=self.get_folder)
        self.entry_folder.pack(side=tkinter.LEFT, padx=10)
        self.btn_folder.pack(side=tkinter.LEFT, padx=10)
        self.entry_filename.pack(side=tkinter.LEFT, padx=10)


        self.btn_start = ctk.CTkButton(master=self.frame2, command=self.start_btn_event, text="Сгенерировать")
        self.btn_start.grid(row=1, column=1)
        self.entry = ctk.CTkEntry(self.frame2, width=750, placeholder_text='Введите слова через пробел')
        self.entry.grid(row=1, column=0, padx=10, pady=10)
        self.bind('<Return>', self.start_btn_event)

        self.fill_folder()

    def fill_folder(self):
        if os.path.exists('conf.txt'):
            with open('conf.txt') as f:
                folder = f.read().strip()
            self.entry_folder.insert(0, folder)

    def get_folder(self):
        self.entry_folder.insert(0, filedialog.askdirectory())

    def start_btn_event(self, *args):
        words = self.entry.get().split()
        words.sort(key=len, reverse=True)
        folder = self.entry_folder.get()
        filename = self.entry_filename.get()
        if not folder:
            tkinter.messagebox.showerror('Ошибка', 'Выберите папку!')
            return
        if not filename:
            tkinter.messagebox.showerror('Ошибка', 'Введите имя файла!')
            return

        path = f'{folder}/{filename}.docx'
        matrix = run(words)
        file_name = save(matrix, words, path)
        self.entry.delete(0, tkinter.END)
        with open('conf.txt', 'w') as f:
            f.write(folder)
        tkinter.messagebox.showinfo(title='Файл сохранён', message=f'Файл "{file_name}" сохранен в папке {path}')


def main():
    app = LetterSoupApp()
    app.mainloop()


if __name__ == '__main__':
    main()
