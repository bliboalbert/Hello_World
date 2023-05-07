"""A simple form validator GUI with CustomTkinter
Pythonista Form validator by Blibo Albert"""

import customtkinter as ctk

class FormValidator(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Pythonista Form')
        self._set_appearance_mode('dark')
        self.geometry('600x600')
        self.configure(padx=50, pady=50)

        # Create a frame object to hold other widgets
        self.formFrame = ctk.CTkFrame(self,
                                      width=500,
                                      height=500,
                                      corner_radius=6,
                                      fg_color='orange'
                                      )
        self.formFrame.pack(anchor='center', fill='both', expand=True)

        # Place widgets in frame to compose form
        # Labels
        self.titleLable = ctk.CTkLabel(self.formFrame,
                                       text='Sign Up with Pythonista Hub',
                                       text_color='black',
                                         font=('Verdana', 20, 'bold'),
                                           anchor='center')
        self.titleLable.grid(column=0, row=0, columnspan=3)
        self.titleLable.configure(padx=50, pady=5)
        self.firstName = ctk.CTkLabel(self.formFrame, text='First Name:',
                                       text_color='white',
                                       font=('Verdana', 15, 'normal'))
        self.firstName.grid(column=0, row=1)
        self.firstName.configure(padx=20, pady=15)
        self.midName = ctk.CTkLabel(self.formFrame, text='Middle Name:',
                                     text_color='white',
                                     font=('Verdana', 15, 'normal'))
                                     
        self.midName.grid(column=0, row=2)
        self.midName.configure(padx=20, pady=15)
        self.lastName = ctk.CTkLabel(self.formFrame, text='Last Name:',
                                      text_color='white',
                                      font=('Verdana', 15, 'normal'))
                                     
        self.lastName.grid(column=0, row=3)
        self.lastName.configure(padx=20, pady=15)

        self.email = ctk.CTkLabel(self.formFrame, text='Email:',
                                   text_color='white',
                                   font=('Verdana', 15, 'normal'))
                                   
        self.email.grid(column=0, row=4)
        self.email.configure(padx=20, pady=15)
        self.userName = ctk.CTkLabel(self.formFrame, text='Username:',
                                      text_color='white',
                                      font=('Verdana', 15, 'normal'))
                                      
        self.userName.grid(column=0, row=5)
        self.userName.configure(padx=20, pady=15)
        self.phoneNumber = ctk.CTkLabel(self.formFrame, text='Phone:',
                                      text_color='white',
                                      font=('Verdana', 15, 'normal'))
                                      
        self.phoneNumber.grid(column=0, row=6)
        self.phoneNumber.configure(padx=20, pady=15)
        self.password = ctk.CTkLabel(self.formFrame, text='Password:',
                                      text_color='white',
                                      font=('Verdana', 15, 'normal'))
                                 
        self.password.grid(column=0, row=7)
        self.password.configure(padx=20, pady=15)
        self.confirmPassword = ctk.CTkLabel(self.formFrame, text='Confirm Password:',
                                      text_color='white',
                                      font=('Verdana', 15, 'normal'))
                                      
        self.confirmPassword.grid(column=0, row=8)
        self.confirmPassword.configure(padx=20, pady=15)

        # Create entries for user input
        self.firstNameEntry = ctk.CTkEntry(self.formFrame, corner_radius=4, width=180)
        self.firstNameEntry.grid(column=1, row=1, columnspan=2, sticky=ctk.EW)
        self.firstNameEntry.focus()
        self.firstNameEntry.insert(0, 'First Name')
        self.midNameEntry = ctk.CTkEntry(self.formFrame, corner_radius=4, width=180)
        self.midNameEntry.insert(0, 'Middle Name')
        self.midNameEntry.grid(column=1, row=2, columnspan=2, sticky=ctk.EW)
        self.lastNameEntry = ctk.CTkEntry(self.formFrame, corner_radius=4, width=180)
        self.lastNameEntry.insert(0, 'Last Name')
        self.lastNameEntry.grid(column=1, row=3, columnspan=2, sticky=ctk.EW)
        self.emailEntry = ctk.CTkEntry(self.formFrame, corner_radius=4, width=180)
        self.emailEntry.insert(0, 'example@gmail.com')
        self.emailEntry.grid(column=1, row=4, columnspan=2, sticky=ctk.EW)
        self.userNameEntry = ctk.CTkEntry(self.formFrame, corner_radius=4, width=180)
        self.userNameEntry.insert(0, 'Username')
        self.userNameEntry.grid(column=1, row=5, columnspan=2, sticky=ctk.EW)
        self.phoneNumberEntry = ctk.CTkEntry(self.formFrame, corner_radius=4, width=180)
        self.phoneNumberEntry.insert(0, '054-884-7490')
        self.phoneNumberEntry.grid(column=1, row=6, columnspan=2, sticky=ctk.EW)
        self.passwordEntry = ctk.CTkEntry(self.formFrame, corner_radius=4, width=180)
        self.passwordEntry.insert(0, '**************')
        self.passwordEntry.grid(column=1, row=7, columnspan=2, sticky=ctk.EW)
        self.confirmPasswordEntry = ctk.CTkEntry(self.formFrame, corner_radius=4, width=180)
        self.confirmPasswordEntry.insert(0, '**************')
        self.confirmPasswordEntry.grid(column=1, row=8, columnspan=2, sticky=ctk.EW)

        # Buttons
        self.signUpBtn = ctk.CTkButton(self.formFrame,
                                        text='Sign Up',
                                        corner_radius=4,
                                        bg_color='orange',
                                        hover_color='white',
                                        width=180,
                                          text_color='black',
                                          font=('Verdana', 15, 'normal'))
        self.signUpBtn.grid(column=0, row=9, sticky=ctk.E, padx=20)
        self.signInBtn = ctk.CTkButton(self.formFrame,
                                        text='Have an account? Sign In',
                                        corner_radius=4,
                                        bg_color='orange',
                                        hover_color='white',
                                        width=180, 
                                        text_color='black',
                                        font=('Verdana', 15, 'normal'))
        self.signInBtn.grid(column=1, row=9, sticky=ctk.EW)


form = FormValidator()
form.mainloop()
