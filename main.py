# https://tkdocs.com/tutorial/canvas.html
import tkinter as ti

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_data():
    website = website_input.get()
    email = username_input.get()
    password = password_input.get()

    # "a" mode also creates a file if it does not exit.
    with open("data.txt", mode="a") as data:
        data.write(f"{website} | {email} | {password}\n")

        website_input.delete(first=0, last=len(website))
        website_input.focus()
        username_input.delete(first=0, last=len(email))
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
    justify="left"
)
password_gen_button.grid(column=2, row=3)

add_button = ti.Button(bg="white", text="Add", width=32, justify="left", pady=2, command=add_data)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
