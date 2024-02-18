import tkinter as tk
from dat import EditFile
import tkinter.messagebox






class MainWindow:
    def __init__(self, window):
        self.window = window
        self.window.geometry("800x500")
        self.data = EditFile("bucketlist.dat").read_from_file()
        self.setup_ui()
        self.selected_country = None
        self.selected_place = None

    def setup_ui(self):
        self.window.title("MY BUCKETLIST")

        self.title_app = tk.Label(self.window, text="My Bucketlist Places",fg="white",
                               bg="black", relief="solid", font=("arial",16,"bold"))
        self.title_app.place(x=0, y=10, width=800)

        self.country_label = tk.Label(self.window, text="Country")
        self.country_label.place(x=20, y=50)

        self.country_entry = tk.Entry(self.window, width=50)
        self.country_entry.place(x=20, y=70, width=580)

        self.place_label = tk.Label(self.window, text="Place")
        self.place_label.place(x=20, y=90)

        self.place_entry = tk.Entry(self.window)
        self.place_entry.place(x=20, y=110, width=580)

        self.add_button = tk.Button(self.window, text='ADD', command=self.add_item)
        self.add_button.place(x=640, y=60, width=50)

        self.delete_button = tk.Button(self.window, text="DELETE", command=self.delete_place)
        self.delete_button.place(x=720, y=60, width=50)

        self.overwrite_button = tk.Button(self.window, text="OVERWRITE", command=self.overwrite_info)
        self.overwrite_button.place(x=640, y=105, width=130)

        self.listboxes()


    def listboxes(self):
        self.country_listbox = tk.Listbox(self.window)
        self.country_listbox.place(x=20, y=140, width=200, height=340)
        self.country_scroller = tk.Scrollbar(self.country_listbox, command=self.country_listbox.yview)
        self.country_scroller.pack(side=tk.RIGHT, fill=tk.Y)
        self.country_listbox.config(yscrollcommand=self.country_scroller.set)

        for item in sorted(self.data.keys()):
            if item !="INFO":
                self.country_listbox.insert(tk.END, item)

        self.place_listbox = tk.Listbox(self.window)
        self.place_listbox.place(x=240, y=140, width=200, height=340)
        self.place_scroller = tk.Scrollbar(self.place_listbox, command=self.place_listbox.yview)
        self.place_scroller.pack(side=tk.RIGHT, fill=tk.Y)
        self.place_listbox.config(yscrollcommand=self.place_scroller.set)

        self.info_box = tk.Text(self.window, wrap="word")
        self.info_box.place(x=460, y=140, width=310, height= 340)
        self.info_box_scroll = tk.Scrollbar(self.info_box, command=self.place_listbox.yview)
        self.info_box_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.info_box.config(yscrollcommand=self.info_box_scroll.set)

        # Bind the selection event to the on_select function
        self.country_listbox.bind("<<ListboxSelect>>", self.place_list)

          
    def add_item(self):

        country = self.country_entry.get().title()
        place = self.place_entry.get().title()

        if country != "":
            if country.lower() not in [x.lower() for x in self.data.keys()]:
                self.data[country] = []
                self.data["INFO"][country] = ""

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
            if item!="INFO":
                self.country_listbox.insert(tk.END, item)



    def place_list(self, event):

        try:
            i = self.country_listbox.curselection()
            self.selected_country = self.country_listbox.get(i)

        except:
            pass

        self.place_listbox.delete(0, tk.END)

        for item in sorted(self.data[self.selected_country]):
            self.place_listbox.insert(tk.END, item)

        self.info_box.delete("1.0", tk.END)


        self.place_listbox.bind("<<ListboxSelect>>", self.on_select)


        self.info_box.insert(tk.END, self.data["INFO"][self.selected_country] + "\n")

    


    def on_select(self, event):
        try:
        
            i = self.place_listbox.curselection()
            self.selected_place = self.place_listbox.get(i)

        except:
            pass



    def delete_place(self):

        if self.selected_place != None:

            self.data[self.selected_country].remove(self.selected_place)

            EditFile("bucketlist.dat", self.data).overwrite_file()


        self.update_country_and_place_lists()


    def overwrite_info(self):
        info = self.info_box.get("1.0", tk.END)
        self.data["INFO"][self.selected_country] = info
        EditFile("bucketlist.dat", self.data).overwrite_file()



    def update_country_and_place_lists(self):

        self.place_listbox.delete(0, tk.END)
        for item in sorted(self.data[self.selected_country]):
            self.place_listbox.insert(tk.END, item)



