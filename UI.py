import tkinter as tk

class DropDownMenu:
    def __init__(self, parent):
        self.parent = parent
        self.options1 = ['ALL', 'BRONX', 'BROOKLYN', 'MANHATTAN', 'QUEENS', 'STATEN ISLAND']
        self.selected_option1 = tk.StringVar(parent)
        self.selected_option1.set(self.options1[0])

        self.options2 = ['HEAT', 'SCATTER']
        self.selected_option2 = tk.StringVar(parent)
        self.selected_option2.set(self.options2[0])

        self.label1 = tk.Label(parent, text="Select a city:")
        self.label1.pack(side=tk.TOP, padx=10, pady=5)

        self.menu1 = tk.OptionMenu(parent, self.selected_option1, *self.options1)
        self.menu1.pack(side=tk.TOP, padx=10, pady=5)

        self.label2 = tk.Label(parent, text="Select a pin type:")
        self.label2.pack(side=tk.TOP, padx=10, pady=5)

        self.menu2 = tk.OptionMenu(parent, self.selected_option2, *self.options2)
        self.menu2.pack(side=tk.TOP, padx=10, pady=5)

        self.clicked_submit = False  # flag for Submit button click

        self.selected_menu = 1  # default to menu1

        self.menu1_button = tk.Button(parent, text="Select City Menu", command=lambda: self.set_selected_menu(1))
        self.menu1_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.menu2_button = tk.Button(parent, text="Select Pin Menu", command=lambda: self.set_selected_menu(2))
        self.menu2_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.button = tk.Button(parent, text="Submit", command=self.on_options_select)
        self.button.pack(side=tk.TOP, padx=10, pady=10)

    def set_selected_menu(self, menu_number):
        self.selected_menu = menu_number

    def on_options_select(self):
        self.clicked_submit = True  # set flag to indicate Submit button has been clicked
        if self.selected_menu == 1:
            self.value = self.selected_option1.get()
        else:
            self.value = self.selected_option2.get()
        self.parent.after(0, self.parent.destroy)  # destroy window after the method has completed

    def get_selected_option(self):
        if self.clicked_submit:
            return self.value
        else:
            return None

root = tk.Tk()
ddm = DropDownMenu(root)
root.mainloop()

# Check if Submit button was clicked and print selected option
selected_option = ddm.get_selected_option()
if selected_option:
    print("Selected option:", selected_option)