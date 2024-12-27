from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list += [choice(letters) for _ in range(randint(8,10))]
    password_list += [choice(symbols) for _ in range(randint(2,4))]
    password_list += [choice(numbers) for _ in range(randint(2,4))]

    shuffle(password_list)

    password = ''.join(password_list)
    password_input.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    web_entry = website_input.get()
    email_entry = user_email_input.get()
    pass_entry = password_input.get()

    if len(web_entry) == 0 or len(email_entry) == 0 or len(pass_entry) == 0:
        messagebox.showinfo(message="Don't leave any field empty")
    else:
        is_okay = messagebox.askokcancel(title="Check", message=f"Please confirm: \n Website: {web_entry}\n Email: {email_entry}\n Password: {pass_entry}")
        if is_okay:
            with open("data.txt", "a") as file:
                file.write(f"{web_entry} | {email_entry} | {pass_entry}\n")



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20 )


canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_image = PhotoImage(file = "logo.png")
canvas.create_image(100,100, image=lock_image)
canvas.grid(column = 1, row = 0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

#LABELS

email_username = Label(text = "Email/Username:")
email_username.grid(column=0, row=2)

password = Label(text="Password:")
password.grid(column=0, row=3)

#ENTRIES

website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

user_email_input = Entry(width=35)
user_email_input.grid(column=1, row=2, columnspan=2)
user_email_input.insert(0, "youremail@domain.com")

password_input = Entry(width=35)
password_input.grid(column=1, row=3, columnspan=2)

#BUTTONS

gen_pass_button = Button(text="Generate Password", command=generate_pass)
gen_pass_button.grid(column=2, row=3, padx= 0 )

add_button = Button(text="Add", width=30, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()