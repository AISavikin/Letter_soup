from func import run, save
import tkinter
import tkinter.messagebox
import customtkinter
from tkinter import filedialog

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


class LetterSoupApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        w = self.winfo_screenwidth() // 2
        h = self.winfo_screenheight() // 2
        h_window = 950
        self.title("Суп из букв")
        self.geometry(f'{h_window}x50+{w - h_window // 2}+{h}')
        self.btn_start = customtkinter.CTkButton(master=self, command=self.start_btn_event, text="Сгенерировать")
        self.btn_start.grid(row=0, column=1, sticky="e")
        self.entry = customtkinter.CTkEntry(self, width=750)
        self.entry.grid(row=0, column=0, padx=10, pady=10)

    def start_btn_event(self):
        words = self.entry.get().split()
        words.sort(key=len, reverse=True)
        path = filedialog.askdirectory()
        matrix = run(words)
        file_name = save(matrix, words, path)
        self.entry.delete(0, tkinter.END)
        tkinter.messagebox.showinfo(title='Файл сохранён', message=f'Файл "{file_name}" сохранен в папке {path}')

        print(self.winfo_screenwidth())


def main():
    app = LetterSoupApp()
    app.mainloop()


if __name__ == '__main__':
    main()
