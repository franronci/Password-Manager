from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def genera_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for letra in range(randint(8, 10))]
    password_numbers = [choice(numbers) for letra in range(randint(2, 4))]
    password_symbols = [choice(symbols) for letra in range(randint(2, 4))]
    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    email_data = email_entry.get()
    website_data = website_entry.get()
    password_data = password_entry.get()

    if len(email_data) and len(password_data) and len(website_data) > 0:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email_data} \nPassword: {password_data} \nIs it ok to save it? ")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website_data} / {email_data} / {password_data}\n")
                password_entry.delete(0, END)
                website_entry.delete(0, END)
    else:
        messagebox.showwarning(title="OOPS", message="Please don't leave any fields empty!")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
foto = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=foto)
canvas.grid(row=0, column=1)

website = Label(text="Website:")
website.grid(row=1, column=0)

email_user = Label(text="Email/Username:")
email_user.grid(row=2, column=0)

password = Label(text="Password:")
password.grid(row=3, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "franronci@gmail.com")

password_entry = Entry(width=20)
password_entry.grid(row=3, column=1)

generate_pas = Button(text="Generate Password", width=21, command=genera_pass)
generate_pas.grid(row=3, column=2)

add = Button(text="Add", width=36, command=save)
add.grid(row=4, column=1, columnspan=2)




window.mainloop()
