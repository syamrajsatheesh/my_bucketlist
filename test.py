import tkinter as tk

class AppGUI:
    def __init__(self, master):
        self.master = master
        self.setup_ui()

    def setup_ui(self):
        self.master.title("Two Listboxes Demo")

        # Create the first listbox
        self.listbox1 = tk.Listbox(self.master, width=25)
        self.listbox1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Insert items into the first listbox
        self.listbox1.insert(tk.END, "List 1", "List 2", "List 3")

        # Bind the selection event to the on_select function
        self.listbox1.bind("<<ListboxSelect>>", self.on_select)

        # Create the scrollbar for the first listbox
        scrollbar1 = tk.Scrollbar(self.master)
        scrollbar1.pack(side=tk.LEFT, fill=tk.Y)
        scrollbar1.config(command=self.listbox1.yview)
        self.listbox1.config(yscrollcommand=scrollbar1.set)

        # Create the second listbox
        self.listbox2 = tk.Listbox(self.master, width=25)
        self.listbox2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create the delete button
        self.delete_button = tk.Button(self.master, text="Delete", command=self.delete_item)
        self.delete_button.pack()

    def on_select(self, event):
        # Clear the second listbox
        self.listbox2.delete(0, tk.END)

        # Get the selected item from the first listbox
        selected_index = self.listbox1.curselection()[0]
        selected_item = self.listbox1.get(selected_index)

        # Display corresponding items in the second listbox
        items = ["Item 1", "Item 2", "Item 3"]  # Replace with actual corresponding items
        for item in items:
            self.listbox2.insert(tk.END, item)

    def delete_item(self):
        # Get the selected index from the second listbox
        selected_index = self.listbox2.curselection()
        if selected_index:
            # Delete the selected item from the second listbox
            self.listbox2.delete(selected_index)

def main():
    root = tk.Tk()
    app = AppGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
