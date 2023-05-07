
#:TODO: Create UI interface using classes
#:TODO: create password saving mechanism
#:TODO: Create password generator method
#TODO: create password search mechanism


# ------------------.. Import statements ..---------------------- #

import customtkinter as ctk
from random import randint, shuffle, choice
from CTkMessagebox import CTkMessagebox
from PIL import Image, ImageTk
import json
import pyperclip


# -----------------.. UI Design ..------------------------------- #
class passwordManager(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('800x800')
        self.configure(padx=50, pady=50)
        self.title('TryStar Password Manager')
        self.grid_columnconfigure((1, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)
        ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
        ctk.set_appearance_mode('system')
        self.canvas = ctk.CTkCanvas(width=300, height=300, highlightthickness=0)
        self.logo = './password.png'
        self.image = Image.open(self.logo)
        self.img = self.image.resize((200, 200))
        self.img = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(150, 200, image=self.img)
        self.canvas.create_text(150, 200, text='TryStar Password', font=('Verdana', 15, 'normal'), fill='indigo')
        self.canvas.grid(column=1, row=1, sticky=ctk.NS)

        # labels
        self.website = ctk.CTkLabel(self, text='Website:', fg_color='#6155A6', corner_radius=6, text_color='white')
        self.website.grid(column=0, row=2, sticky=ctk.E)
        self.email = ctk.CTkLabel(self, text='Email/Username:', fg_color='#6155A6', corner_radius=6, text_color='white')
        self.email.grid(column=0, row=3, sticky=ctk.E)
        self.password = ctk.CTkLabel(self, text='Password:', fg_color='#6155A6', corner_radius=6, text_color='white')
        self.password.grid(column=0, row=4, sticky=ctk.E)

        # entries
        self.website_entry = ctk.CTkEntry(self, width=21)
        self.website_entry.focus()
        self.website_entry.grid(column=1, row=2, padx=10, pady=10, sticky=ctk.EW)
        self.email_entry = ctk.CTkEntry(self, width=35)
        self.email_entry.insert(0, 'bliboalbert3@gmail.com')
        self.email_entry.grid(column=1, row=3, padx=10, pady=10, columnspan=2, sticky=ctk.EW)
        self.password_entry = ctk.CTkEntry(self, width=21)
        self.password_entry.grid(column=1, row=4, padx=10, pady=10, sticky=ctk.EW)

        # buttons
        # 9C2C77, CD104D
        self.generate_bt = ctk.CTkButton(self, text='Generate Password', hover_color='#80558C', command=self.generatePassword)
        self.generate_bt.grid(column=2, row=4, padx=10, pady=10, sticky=ctk.NE)
        self.add_bt = ctk.CTkButton(self, text='Add', width=35, hover_color='#80558C', command=self.save)
        self.add_bt.grid(column=1, row=5, padx=10, pady=10, columnspan=2, sticky=ctk.EW)
        self.search_bt = ctk.CTkButton(self, text='Search', hover_color='#80558C', command=self.search)
        self.search_bt.grid(column=2, row=2, padx=10, pady=10, sticky=ctk.NE)


    # -------------------.. Password Saving Mechanism ..------------------------- #
    def save(self):
        website = self.website_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        if len(website) == 0 or len(password) == 0:
            CTkMessagebox(title='Error', message='Please do not leave any fields empty.')
        else:
            credentials = {
                website: {
                'email': email,
                'password': password
                }
            }

            is_ok = CTkMessagebox(title='Crosscheck Credentials', message=f'Your credentials for {website} are:\n Email: {email}\n Password: {password}\n is it ok?',
                                   icon='question', option_1='cancel', option_2='yes', option_3='no').get()
            if is_ok == 'yes':
                try:
                    with open('credential.json', 'r') as file:
                        data = json.load(file)
                except FileNotFoundError:
                    with open('credential.json', 'w') as file:
                        json.dump(credentials, file, indent=4)
                else:
                    data.update(credentials)

                    with open('credential.json', 'w') as file:
                        json.dump(data, file, indent=4)
                finally:
                    self.website_entry.delete(0, ctk.END)
                    self.password_entry.delete(0, ctk.END)
            else:
                CTkMessagebox(title='Update Credentials', message='You can generate a new password anytime.')


    # ----------------------.. Password Generation Mechanism ..------------------- #
    def generatePassword(self):
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
        
        password_list = [choice(letters) for _ in range(randint(8, 12))]
        password_list += [choice(numbers) for _ in range(randint(3, 5))]
        password_list += [choice(symbols) for _ in range(randint(3, 5))]

        shuffle(password_list)
        password = "".join(password_list)
        self.password_entry.delete(0, ctk.END)
        self.password_entry.insert(0, password)
        pyperclip.copy(self.password_entry.get())

    # ----------------------.. Password search Mechanism ..------------------------ #
    def search(self):
        with open('credential.json', 'r') as file:
            data = json.load(file)

            website = self.website_entry.get()
            if website in data:
                email = data[website]['email']
                password = data[website]['password']
                CTkMessagebox(title=website, message=f'Email: {email}\n Password: {password}', icon='check')
            else:
                CTkMessagebox(title='Error', message=f'You do not have credentials about {website} in your database.')
            

        



passwordmanager = passwordManager()
passwordmanager.mainloop()