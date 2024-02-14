import tkinter as tk
from dat import EditFile
import tkinter.messagebox






class MainWindow:
    def __init__(self, window):
        self.window = window
        self.window.geometry("600x600")
        self.data = EditFile("bucketlist.dat").read_from_file()
        self.setup_ui()
        self.selected_country = None
        self.selected_place = None

    def setup_ui(self):
        self.window.title("MY BUCKETLIST")

        self.title_app = tk.Label(self.window, text="My Bucketlist Places",fg="white",
                               bg="black", relief="solid", font=("arial",16,"bold"))
        self.title_app.pack(fill=tk.BOTH, pady=20, padx=0, expand=False)

        self.country_label = tk.Label(self.window, text="Country")
        self.country_label.place(x=20, y=60)

        self.country_entry = tk.Entry(self.window)
        self.country_entry.pack(fill=tk.BOTH, pady=15, padx=20, expand=False)

        self.place_label = tk.Label(self.window, text="Place")
        self.place_label.place(x=20, y=110)

        self.place_entry = tk.Entry(self.window)
        self.place_entry.pack(fill=tk.BOTH, pady=15, padx=20, expand=False, )

        self.add_button_frame = tk.Frame(self.window)
        self.add_button_frame.pack(side=tk.LEFT, fill=tk.Y, padx=20)

        self.add_button = tk.Button(self.add_button_frame, text='ADD', command=self.add_item)
        self.add_button.pack(anchor=tk.E)

        self.delete_button_frame = tk.Frame(self.window)
        self.delete_button_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=20)

        self.delete_button = tk.Button(self.delete_button_frame, text="DELETE", command=self.delete_place)
        self.delete_button.pack(anchor=tk.E)

        self.country_listbox = tk.Listbox(self.window)
        self.country_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.country_scroller = tk.Scrollbar(self.country_listbox, command=self.country_listbox.yview)
        self.country_scroller.pack(side=tk.RIGHT, fill=tk.Y)
        self.country_listbox.config(yscrollcommand=self.country_scroller.set)

        for item in sorted(self.data.keys()):
            self.country_listbox.insert(tk.END, item)

        self.place_listbox = tk.Listbox(self.window)
        self.place_listbox.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.place_scroller = tk.Scrollbar(self.place_listbox, command=self.place_listbox.yview)
        self.place_scroller.pack(side=tk.RIGHT, fill=tk.Y)
        self.place_listbox.config(yscrollcommand=self.place_scroller.set)

        # Bind the selection event to the on_select function
        self.country_listbox.bind("<<ListboxSelect>>", self.place_list)



          
    def add_item(self):

        country = self.country_entry.get().title()
        place = self.place_entry.get().title()

        if country != "":
            if country.lower() not in [x.lower() for x in self.data.keys()]:
                self.data[country] = []

            if place=="":
                tkinter.messagebox.showinfo("Warning!", 'Place is not given.')
            elif place.lower() in [x.lower() for x in self.data[country]]:
                tkinter.messagebox.showinfo("Warning!", 'Place already in the bucketlist.')
            else:
                self.data[country].append(place)

                self.country_entry.delete(0, tk.END)
                self.place_entry.delete(0, tk.END)

            


        else:
            tkinter.messagebox.showinfo("Warning!", 'Give the country name please!')

        EditFile("bucketlist.dat", self.data).overwrite_file()

        self.update_country_list()



    def update_country_list(self):

        self.country_listbox.delete(0, tk.END)
        for item in sorted(self.data.keys()):
            self.country_listbox.insert(tk.END, item)



    def place_list(self, event):


        i = self.country_listbox.curselection()
        self.selected_country = self.country_listbox.get(i)

        self.place_listbox.delete(0, tk.END)

        for item in sorted(self.data[self.selected_country]):
            self.place_listbox.insert(tk.END, item)

        self.place_listbox.bind("<<ListboxSelect>>", self.on_select)



    def on_select(self, event):
        
        i = self.place_listbox.curselection()
        self.selected_place = self.place_listbox.get(i)



    def delete_place(self):

        if self.selected_place != None:

            self.data[self.selected_country].remove(self.selected_place)

            EditFile("bucketlist.dat", self.data).overwrite_file()


        self.update_country_and_place_lists()



    def update_country_and_place_lists(self):

        self.place_listbox.delete(0, tk.END)
        for item in sorted(self.data[self.selected_country]):
            self.place_listbox.insert(tk.END, item)



