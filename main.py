# https://tkdocs.com/tutorial/canvas.html
import tkinter as ti
# It is not a class from tkinter.
# Therefore, we need to import `messagebox` independently
from tkinter import messagebox
from random import randint, choice, shuffle
# external lib.
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    password_list = [choice(letters) for _ in range(randint(8, 10))]
    # List + List
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    # List + List
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    # --------------------- It is also [IMPORTANT]!!! -----------------------
    # password_list = []
    #
    # for char in range(nr_letters):
    #     [IMPORTANT]
    #     We can use because String returned by `choice(letters)` is iterable.
    #     Think about we can use `for loop` for String object
    #     One thing we need to know `+=` must be used. `+` generates an error.
    #
    #     [Works] Same thing
    #     password_list += random.choice(letters)
    #     password_list.append(random.choice(letters))

    """
        [IMPORTANT!!!!]
        Other than String (The underlined case does not work because they are not the iterable type like String)
        test_list = []
        test_list += 1 ===> error because test_list is empty
        print("test_list: ", test_list)
        
        [Works]
        test_list = []
        test_list += '7'
        print("test_list: ", test_list)
    """

    # for char in range(nr_symbols):
    #     choice = random.choice(symbols)
    #     [IMPORTANT] Array + Iterable Element (Append)
    #     # we can concat the element by using `+=` operation with String object
    #     # instead of `append` above
    #     password_list += choice

    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)

    # shuffle the elements in the list
    shuffle(password_list)

    # [IMPORTANT]
    # 3) it works as well.
    password = "".join(password_list)

    # 2) IMPORTANT (join function from List to String)
    # password = str.join("", password_list)

    # 1)
    # password = ""
    # for char in password_list:
    #     password += char

    # Delete everything first just in case
    password_input.delete(first=0, last=len(password_input.get()))
    # Add input string
    password_input.insert(index=0, string=password)
    # copy the password in the clipboard!
    pyperclip.copy(password)

    # pyperclip to do clipboard
    # https://pypi.org/project/pyperclip/

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_data():
    website = website_input.get()
    email = username_input.get()
    password = password_input.get()

    # It works as well.
    # if len(website) == 0 || len(password) == 0:
    if website == "" or password == "":
        messagebox.showwarning(title="Oops", message="Some of the required information is empty.")
        return

    # Standard Dialogs (Popup window) in tkinter
    # [Message box] of Standard Dialogs
    # Yes or No with two buttons
    answer = messagebox.askokcancel(
        title=website,
        message=f"There are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?"
    )

    # We can just show info or yesno
    # messagebox.showinfo(title="Title", message="message")
    # messagebox.askyesno(title="Title", message="message")

    if answer:
        # "a" mode also creates a file if it does not exit.
        with open("data.txt", mode="a") as data:
            data.write(f"{website} | {email} | {password}\n")

            website_input.delete(first=0, last=len(website))
            website_input.focus()
            password_input.delete(first=0, last=len(password))

# ---------------------------- UI SETUP ------------------------------- #
# 1) Window


window = ti.Tk()
window.title("Password Manager")
# 200 * 190
window.config(padx=50, pady=50, bg="white")

# 2) Canvas and Image (Photo)
canvas = ti.Canvas(width=200, height=200, bg="white", highlightthickness=0)
lock_mage = ti.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_mage)
# should be changed
canvas.grid(column=1, row=0)

website_label = ti.Label(text="Website:", bg="white")
website_label.grid(column=0, row=1)

website_input = ti.Entry(width=35, justify="left")
# focus website_input
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2)


username_label = ti.Label(text="Email/Username:", bg="white")
username_label.grid(column=0, row=2)

username_input = ti.Entry(width=35, justify="left")
username_input.insert(index=0, string="jake@abc.com")
username_input.grid(column=1, row=2, columnspan=2)

password_label = ti.Label(text="Password:", bg="white")
password_label.grid(column=0, row=3)

password_input = ti.Entry(width=21, justify="left")
password_input.grid(column=1, row=3)

password_gen_button = ti.Button(
    bg="white",
    text="Generate Password",
    height=0,
    font=("Arial", 8, "normal"),
    padx=4,
    pady=2,
    justify="left",
    command=generate_password,
)
password_gen_button.grid(column=2, row=3)

add_button = ti.Button(bg="white", text="Add", width=32, justify="left", pady=2, command=add_data)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
