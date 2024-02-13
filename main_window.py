import tkinter as tk
from dat import EditFile


class App:
    def __init__(self):
        # Sample data for the lists
        self.items_lists = [
            ["Apple", "Banana", "Orange"],
            ["Carrot", "Potato", "Tomato"],
            ["Dog", "Cat", "Bird"]
        ]

    def get_items_lists(self):
        return self.items_lists

class MainWindow:
    def __init__(self, window):
        self.window = window
        self.window.geometry("600x600")
        self.data = EditFile("bucketlist.dat").read_from_file()
        self.setup_ui()

    def setup_ui(self):
        self.window.title("Listbox Demo")

        self.country_listbox = tk.Listbox(self.window)
        self.country_listbox.place(x=20, y=70, width=270, height=500)

        self.country_scroller = tk.Scrollbar(self.country_listbox, command=self.country_listbox.yview)
        self.country_scroller.pack(side=tk.RIGHT, fill=tk.Y)
        self.country_listbox.config(yscrollcommand=self.country_scroller.set)

        # Insert items into the first listbox
        for item in self.data.keys():
            self.country_listbox.insert(tk.END, item)

        # Bind the selection event to the on_select function
        self.country_listbox.bind("<<ListboxSelect>>", self.on_select)

        self.place_listbox = tk.Listbox(self.window)
        self.place_listbox.place(x=300, y=70, width=270, height=500)

        self.place_scroller = tk.Scrollbar(self.place_listbox, command=self.place_listbox.yview)
        self.place_scroller.pack(side=tk.RIGHT, fill=tk.Y)
        self.place_listbox.config(yscrollcommand=self.place_scroller.set)

    def on_select(self, event):
        # Clear the second listbox
        self.place_listbox.delete(0, tk.END)

        # Get the selected index from the first listbox
        index = self.country_listbox.curselection()[0]

        # Get the corresponding list
        selected_country = self.country_listbox.get(index)

        # Insert items into the second listbox
        for item in self.data[selected_country]:
            self.place_listbox.insert(tk.END, item)
